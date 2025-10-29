# main.py
import os
from add_expense import add_expense
from show_totals import show_totals, parse_expenses

DATA_FILE = "expenses.txt"

def show_all_expenses(file_path=DATA_FILE):
    expenses = parse_expenses(file_path)
    if not expenses:
        print("No expenses.")
        return
    print("All expenses:")
    for i, (cat, amt) in enumerate(expenses, start=1):
        print(f"{i}. {cat} — {amt:.2f}")

def main_menu():
    os.makedirs(os.path.dirname(DATA_FILE) or ".", exist_ok=True)
    while True:
        print("\n--- Budget Buddy ---")
        print("1) Add expense")
        print("2) Show totals by category")
        print("3) Show all expenses")
        print("4) Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense(DATA_FILE)
        elif choice == "2":
            show_totals(DATA_FILE)
        elif choice == "3":
            show_all_expenses(DATA_FILE)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Unknown option. Enter 1-4.")

if __name__ == "__main__":
    main_menu()
