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


