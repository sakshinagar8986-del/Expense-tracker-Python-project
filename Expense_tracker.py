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

def recursive_total(expenses, index=0):
    if index == len(expenses):
        return 0
    return expenses[index][2] + recursive_total(expenses, index + 1)

category_totals={}
    if category in category_totals:
        category_totals[category]+=amount
    else:
        category_totals[category]=amount
def max_expense(category_totals):
    print("maximum expense:",max(category_totals  keys.get),":",max(category_totals))
def min_expense(category_totals):
    print("minimum expense:",min(category_totals  keys.get),":",min(category_totals))
a=recursive_total(expenses,index=0)
    print("WARNING!")
    print("Your montly budget has been exceeded")
    print("Spent:",a)
    print("Exceeded by:"tracker[buget]-a)
for category,amount in category_totals.items():
    print(category,end=" ")
    for i in range(amount//100):
        print("*",end="")
    print()




