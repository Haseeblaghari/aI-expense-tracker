import sqlite3
from datetime import datetime

DB_PATH = r"C:\Users\Haseeb\OneDrive\Desktop\AGENT\expense.db"


# ---------- Create Table If Not Exists ----------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ---------- Add Expense ----------
def add_expense(amount: float, category: str, description: str):
    """Add a new expense to the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?, ?, ?, ?)
    """, (amount, category, description, date))

    conn.commit()
    conn.close()

    return "Expense added successfully."


# ---------- Get Monthly Expenses (Full List + Total) ----------
def get_monthly_expenses(month: str):
    """Get all expenses for a specific month in format YYYY-MM."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, amount, category, description, date
        FROM expenses
        WHERE strftime('%Y-%m', date) = ?
        ORDER BY date ASC
    """, (month,))

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return "No expenses found."

    total = sum(row[1] for row in rows)

    result = f"Total: {total}\n\n"

    for row in rows:
        result += f"ID:{row[0]} | {row[4]} | {row[2]} | {row[1]} | {row[3]}\n"

    return result


# ---------- Get Monthly Total Only ----------
def get_monthly_total(month: str):
    """Get total expense amount for a specific month in format YYYY-MM."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
        WHERE strftime('%Y-%m', date) = ?
    """, (month,))

    total = cursor.fetchone()[0]
    conn.close()

    if total is None:
        return "No expenses found for this month."

    return f"Total expense for {month} is {total}."


# ---------- Delete By ID ----------
def delete_by_id(expense_id: int):
    """Delete ONE expense record using its unique ID."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM expenses
        WHERE id = ?
    """, (expense_id,))

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return "No expense found with this ID."

    conn.close()
    return "Expense deleted successfully."


# ---------- Initialize Database ----------
if __name__ == "__main__":
    init_db()
