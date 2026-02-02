AI Data Analyst is an intelligent application built using Generative AI and LangChain that allows users to interact with databases using natural language. Instead of writing complex SQL queries, users can ask questions in plain English and get meaningful insights from data.

This project demonstrates how Large Language Models (LLMs) can be integrated with databases to automate data analysis, query generation, and result interpretation.

📌 Key Features

🔹 Natural language to SQL query conversion

🔹 Database integration using SQLite

🔹 Powered by LangChain agents and tools

🔹 AI-driven data analysis and insights

🔹 User-friendly interface for interaction

🔹 Automated schema extraction and query execution

🛠️ Technologies Used

Python

Generative AI (LLM APIs)

LangChain

SQLite

UV Package Manager

Streamlit / Custom Frontend

📂 Project Structure
ai-data-analyst-2/
│── main.py              # Main application logic
│── frontend.py          # User interface
│── create_database.py   # Database setup
│── amazon.db            # Sample dataset
│── pyproject.toml       # Project configuration
│── README.md            # Documentation
│── uv.lock              # Dependency lock file
│── .venv/               # Virtual environment

⚙️ How It Works

User enters a question in natural language.

LangChain agent interprets the query.

GenAI converts it into SQL.

Database executes the query.

AI summarizes and presents results.

▶️ Getting Started
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
python main.py

🎯 Use Cases

Data exploration without SQL knowledge

Business analytics automation

Quick reporting

AI-powered dashboards

Educational AI projects

🌟 Future Enhancements

Support for multiple databases

Web-based dashboard

Advanced visualizations

Role-based access

Export reports (PDF/Excel)
