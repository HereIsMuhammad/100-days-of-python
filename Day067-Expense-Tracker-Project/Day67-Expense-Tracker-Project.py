# Day 67: Expense Tracker

import json


class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_expenses(self):
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, title, amount):
        self.expenses.append({
            "title": title,
            "amount": amount
        })
        self.save_expenses()
        print("Expense added!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        print("\nExpenses:")
        for i, exp in enumerate(self.expenses):
            print(f"{i + 1}. {exp['title']} - {exp['amount']}")

    def total_expense(self):
        total = sum(exp["amount"] for exp in self.expenses)
        print(f"\nTotal Expense: {total}")


# Menu-driven program
tracker = ExpenseTracker()

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter expense title: ")
        amount = float(input("Enter amount: "))
        tracker.add_expense(title, amount)

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.total_expense()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")