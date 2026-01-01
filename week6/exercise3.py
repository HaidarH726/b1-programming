expense_records = []
category_totals = {}
unique_categories = set()


number_of_expenses = 5

for i in range(number_of_expenses):
    print(f"\nEnter expense {i + 1}")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    date = input("Enter date (YYYY-MM-DD): ")

    expense = (category, amount, date)
    expense_records.append(expense)

for category, amount, date in expense_records:
    unique_categories.add(category)
    category_totals[category] = category_totals.get(category, 0) + amount



print("\n=== PERSONAL EXPENSE TRACKER ===")
for expense in expense_records:
    print(expense)

print("\n=== UNIQUE CATEGORIES SPENT ON ===")
print(unique_categories)
print(f"Total unique categories: {len(unique_categories)}")

print("\n=== SPENDING BY CATEGORY ===")
for category, total in category_totals.items():
    print(f"{category}: ${total:.2f}")

