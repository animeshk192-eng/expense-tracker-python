expenses = []


def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense Added Successfully!")


def view_expenses():

    if not expenses:
        print("No expenses found.")
        return

    print("\nExpense List")

    for expense in expenses:
        print(f"{expense['category']} - ₹{expense['amount']}")


def total_expense():

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expense = ₹{total}")


while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid Choice")


import json

def save_expenses():

    with open("expenses.txt", "w") as file:
        json.dump(expenses, file)

    print("Expenses Saved Successfully!")

json.dump(expenses, file)

def load_expenses():

    global expenses

    try:
        with open("expenses.txt", "r") as file:
            expenses = json.load(file)

    except FileNotFoundError:
        expenses = []