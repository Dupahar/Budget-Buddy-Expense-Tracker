# add_expense.py
import os

def add_expense(file_path="expenses.txt", category=None, amount=None):
    """
    Appends an expense to file_path in the format: Category,amount
    Returns True on success, False on failure.
    """
    try:
        # validate or ask interactively
        if category is None:
            category = input("Enter category (e.g. Food, Transport): ").strip()
        if not category:
            print("Category cannot be empty.")
            return False

        if amount is None:
            amt_str = input("Enter amount (e.g. 12.50): ").strip()
        else:
            amt_str = str(amount)

        amt = float(amt_str)
        if amt < 0:
            print("Amount must be non-negative.")
            return False

        # ensure file exists
        os.makedirs(os.path.dirname(file_path) or ".", exist_ok=True)

        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"{category},{amt:.2f}\n")
        print(f"Saved: {category}, {amt:.2f}")
        return True
    except ValueError:
        print("Invalid amount. Please enter a number (e.g. 12.50).")
        return False
    except Exception as e:
        print(f"Failed to save expense: {e}")
        return False

if __name__ == "__main__":
    add_expense()
