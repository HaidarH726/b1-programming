expense_records = []
category_totals = {}
unique_categories = {}

def personal_expense_count():
    print = input("Enter expense category :")
    print = input("Enter expense amount:")
    print  = input("Enter expense date :")


personal_expense_count()
personal_expense_count()
personal_expense_count()
personal_expense_count()
personal_expense_count()



for expense_record in expense_records:
    if expense_record not in category_totals:
        category_totals[expense_record] = 0
        unique_categories[expense_record] = 0

    else:
        category_totals[expense_record] += 1
        unique_categories[expense_record] += 1


print( "=== PERSONAL EXPENSE TRACKER ===")
print(category_totals)
print(expense_records)

