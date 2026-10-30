
import csv
import os
from datetime import date

FILE_NAME = "expenses.csv"


# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


# Add Expense
def add_expense():
    print("\n--- ADD EXPENSE ---")

    expense_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

    if expense_date == "":
        expense_date = str(date.today())

    try:
        date.fromisoformat(expense_date)
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter category: ").strip()
        description = input("Enter description: ").strip()

        if not category or not description:
            print("Category and description cannot be empty.")
            return

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([expense_date, category, description, amount])

        print("Expense added successfully!")

    except ValueError:
        print("Invalid date or amount!")


# View Expenses
def view_expenses():
    print("\n--- ALL EXPENSES ---")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("No expenses found.")
        return

    for row in rows:
        print(row[0], "|", row[1], "|", row[2], "| Rs.", row[3])


# Filter Expenses
def filter_expenses():
    print("\n--- FILTER EXPENSES ---")

    category = input("Enter category to filter: ").strip().lower()
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Category"].lower() == category:
                print(row)
                found = True

    if not found:
        print("No expenses found in this category.")


# Category Summary
def category_summary():
    print("\n--- CATEGORY SUMMARY ---")

    summary = {}
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            summary[category] = summary.get(category, 0) + amount
            total += amount

    if not summary:
        print("No expenses available.")
        return

    for category, amount in summary.items():
        print(category, ": Rs.", round(amount, 2))

    print("Total Expenses: Rs.", round(total, 2))


# Main Program
create_file()

while True:
    print("\n==============================")
    print(" PERSONAL EXPENSE TRACKER")
    print("==============================")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter by Category")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        filter_expenses()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Try again.")
