import os
import doctest
from datetime import datetime

# Monthly expense record file
expense_file=open("expenses.txt","w+")
print(expense_file.read())
expense_file.close()

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
    date=input("Enter Date (DD-MM-YYYY):")
    try:
        datetime.striptime(date,"%d-%m-%y")
        return True
    except ValueError:
        return False
    
# Function Add expense

def add_expense(expenses,categories):
    print("\n---ADD NEW EXPENSE ---")
    
    date =valid_date()   
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

    expense_file=open("expenses.txt","w+")
    expense_file.write(tracker,expenses,categories)
    expense_file.close()

    print("\n Expense added successfully")
    return True
    
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
print("5.SHOW HIGHEST AND LOWEST EXPENSE\n=====================\n\n####>Make choices from(1,5)<####\n")
user_choice=int(input("Enter your choice: "))
if(user_choice==1):

    add_exp=add_expense(expenses,categories)
    print(add_exp)



        



    
# def categories_total(category,expenses):
#     categories_totals={}
#     category_total=0
#     for category in categories:
#         for expense in expenses:
#             if expense[1]==category:
#                 category_total+=expense[2]
#         categories_totals[category]=category_total
#     else:
#         print("Category not added")

                
            

#category_totals={}
# if category in category_totals:
#     category_totals[category]+=amount
# else:
#     category_totals[category]=amount
# def max_expense(category_totals):
#     print("maximum expense:",max(category_totals  keys.get),":",max(category_totals))
# def min_expense(category_totals):
#     print("minimum expense:",min(category_totals  keys.get),":",min(category_totals))
# a=recursive_total(expenses,index=0)
# print("WARNING!")
# print("Your montly budget has been exceeded")
# print("Spent:",a)
# print("Exceeded by:"tracker[buget]-a)
# for category,amount in category_totals.items():
#     print(category,end=" ")
#     for i in range(amount//100):
#         print("*",end="")
#     print()
