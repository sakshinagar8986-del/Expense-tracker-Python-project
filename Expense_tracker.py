expenses=[]
categories=set()
tracker={"expenses": expenses,"categories":categories,"budget":10000,"category_totals":{}}

def add_expense(expenses,categories):
    date=input("Enter date (DD-MM-YYYY):").strip()
    category=input("Enter category :").strip().title()
    amount=float(input("Enter amount:"))
    expense=(date,category,amount)
    expenses.append()
    categories.add(category)
    return expenses,categories

def display_expenses(expenses):
    print("\n---ALL EXPENSES----")
    for expense in expenses:
        date,category,amount=expense
        print(date,category,amount)
    return len(expenses)

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total = total + expense[2]
    return total



