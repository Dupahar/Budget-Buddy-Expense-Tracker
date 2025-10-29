# show_totals.py
from collections import defaultdict

def parse_expenses(file_path="expenses.txt"):
    """
    Returns list of (category, amount) tuples.
    Ignores malformed lines.
    """
    expenses = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for lineno, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) < 2:
                    # malformed line, skip or log
                    print(f"Skipping malformed line {lineno}: {line}")
                    continue
                category = parts[0].strip()
                try:
                    amount = float(parts[1].strip())
                except ValueError:
                    print(f"Skipping line with invalid amount {lineno}: {line}")
                    continue
                expenses.append((category, amount))
    except FileNotFoundError:
        # empty list if file not present
        return []
    return expenses

def show_totals(file_path="expenses.txt"):
    expenses = parse_expenses(file_path)
    if not expenses:
        print("No expenses found.")
        return {}

    totals = defaultdict(float)
    for cat, amt in expenses:
        totals[cat] += amt

    overall = sum(totals.values())

    print("Totals by category:")
    for cat, val in sorted(totals.items(), key=lambda x: x[0].lower()):
        print(f"  {cat}: {val:.2f}")
    print(f"Overall: {overall:.2f}")
    return dict(totals)

if __name__ == "__main__":
    show_totals()
