# AI Expense Tracker 💰

An AI-powered expense tracking application built with Streamlit, LangChain, and Ollama.  
This project allows users to manage expenses using natural language commands.

The assistant can:
- Add a new expense
- Show monthly expenses with total
- Show monthly total only
- Delete an expense by ID

The system uses SQLite as a local database.

---

## Project Structure

expense-tracker/
│
├── tools.py        # Database logic (CRUD operations)
├── db.py           # Database creation script
├── agent.py        # AI model + tool binding
├── ui.py           # Streamlit user interface
├── requirements.txt
├── .gitignore
└── README.md

---

## Installation

1. Clone the repository:

git clone https://github.com/Haseeblaghari/aI-expense-tracker.git
cd aI-expense-tracker


2. (Optional) Create requirements.txt automatically:

pip freeze > requirements.txt


3. Install dependencies:

pip install -r requirements.txt


4. Make sure Ollama is installed and running locally.

---

## Setup Database

Run the database setup script:

python db.py


This will create `expense.db` automatically.

---

## Run the Application

streamlit run ui.py


The app will open in your browser.

---

## Example Commands

You can type natural language instructions like:

- Add 500 for food with description lunch
- Show expenses for 2026-02
- Show total for 2026-02
- Delete the expense with expense_id 2

---

## Notes

- The database file (`expense.db`) is not included in this repository.
- It will be created automatically when you run the setup script.
- Ollama must be running locally with the required model (e.g., llama3.1).

---

## License

This project is for educational and portfolio purposes.
