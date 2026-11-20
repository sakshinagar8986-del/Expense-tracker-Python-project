import os
import doctest
from datetime import datetime

# # Monthly expense record file
# expense_file=open("expenses.txt","w+")
# print(expense_file.read())
# expense_file.close()

#data structure
expenses=[]
categories=set()
category_totals={}
tracker={"expenses": expenses,"categories":categories,"budget":10000,"category_totals":category_totals}




#Function for valid date
def valid_date(date):
    """
    Valid date format.
    >>>valid_date("15-11-2026")
    True
    >>>valid_date("2026-11-15")
    False
    """
    
    try:
        datetime.strptime(date,"%d-%m-%y")
        return True
    except ValueError:
        return False
    
# Function Add expense

def add_expense(expenses,categories):
    print("\n---ADD NEW EXPENSE ---")
    date=input("Enter Date (DD-MM-YYYY):")
    date =valid_date(date)   
    category=input("Enter category :").strip().title()
    while not category:
        print("category cannot be empty")
        category=input("Enter category:").strip().title()
        
    amount=float(input("Enter amount:"))
    if amount<=0:
        print("Amount should be postive")
        return False
    
    expense=(date,category,amount)
    expenses.append(expense)
    categories.add(category)

    
    print("\n Expense added successfully")
    
    
#Function Display All Expense
def display_expenses(expenses):
    print("\n---ALL EXPENSES----")
    if (len(expenses)==0):
        print("No Expenses Found.")
    for expense in expenses:
        date,category,amount=expense
        print(date,category,amount)
    return len(expenses)
    
# Recurssion for Total Expense
def recursive_total(expenses, index=0):
    if index == len(expenses):
        return 0
    return expenses[index][2] + recursive_total(expenses, index + 1)


#dictionary for  total per category 
for category in categories:
    category_total=0
    for expense in expenses:
        if expense[1]==category:
            category_total+=expense[2]
    category_totals[category]=category_total
    
#function for access category spending
def category_total(category):
    if category not in category_totals:
        total_per_category=00
    else:
        total_per_category=category_totals[category]
    return total_per_category


print("=====CHOICES=====\n1.ADD EXPENSE\n2.DISPLAY_EXPENSE\n3.SHOW TOTAL SPENDING\n4.SHOW TOTAL PER CATEGORY")
print("5.SHOW HIGHEST AND LOWEST EXPENSE\n6.Exit\n=====================\n\n####>Make choices from(1,5)<####\n")
while True:
    user_choice=int(input("Enter your choice: "))
    if(user_choice==1):
        add_exp=add_expense(expenses,categories)
        print(add_exp)
    elif(user_choice==2):
        display_exp=display_expenses(expenses)
        print(display_exp)
    elif(user_choice==3):
        total_exp=recursive_total(expenses)
        print(total_exp)
        if tracker["budget"]<total_exp:
            print("Warning!\n You expense exceeded from your budget")
    elif(user_choice==4):
        category=input("Enter category for total spending:")
        catg_total=category_total(category)
        print(f"Total per {category} category:Rs{catg_total:.2f} ")
    elif(user_choice==5):
        max_exp=max(category_totals,key=category_totals.get)
        min_exp=min(category_totals,key=category_totals.get)
        print(f"Maximum expense is Rs{category_totals[max_exp]} of {max_exp}")
        print(f"Minimum expense is Rs{category_totals[min_exp]} of {min_exp}")
    elif(user_choice==6):
        print("Thank YOU!")
        break
    else:
        print("Please!,Enter correct Choice")



                