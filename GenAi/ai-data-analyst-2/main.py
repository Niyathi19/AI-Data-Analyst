# Step 1: Extract Schema
from sqlalchemy import create_engine, inspect
import json
import re
import sqlite3

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


db_url = "sqlite:///amazon.db"


# -----------------------------
# Extract DB Schema
# -----------------------------
def extract_schema(db_url):
    engine = create_engine(db_url)
    inspector = inspect(engine)
    schema = {}

    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        schema[table_name] = [col["name"] for col in columns]

    return json.dumps(schema)


# -----------------------------
# Text → SQL using LLM
# -----------------------------
def text_to_sql(schema, prompt):

    SYSTEM_PROMPT = """
    You are an expert SQL generator. Given a database schema and a user prompt, generate a valid SQL query.
    Only use the tables and columns provided in the schema.
    Output ONLY the SQL query. No explanation. No <think> tags.
    """

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("user", "Schema:\n{schema}\n\nQuestion: {user_prompt}\n\nSQL Query:")
    ])

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    chain = prompt_template | llm

    # Call LLM
    raw_response = chain.invoke({
        "schema": schema,
        "user_prompt": prompt
    })

    # Convert response to text
    if hasattr(raw_response, "content"):
        raw_text = raw_response.content
    else:
        raw_text = str(raw_response)

    # Remove <think> tags (if any)
    cleaned_response = re.sub(
        r"<think>.*?</think>",
        "",
        raw_text,
        flags=re.DOTALL
    )

    # Return SQL
    return cleaned_response.strip()


# -----------------------------
# Run SQL on Database
# -----------------------------
def get_data_from_database(prompt):

    schema = extract_schema(db_url)

    sql_query = text_to_sql(schema, prompt)

    print("Generated SQL:", sql_query)  # Optional debug

    conn = sqlite3.connect("amazon.db")
    cursor = conn.cursor()

    results = cursor.execute(sql_query).fetchall()

    conn.close()

    return results

