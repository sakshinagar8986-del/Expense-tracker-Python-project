import os
import doctest
from datetime import datetime


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
        datetime.strptime(date,"%d-%m-%Y")
        return True
    except ValueError:
        return False


# function to save expenses
def save_expenses(expenses):
    with open("expenses.txt","w") as file:
        for expense in expenses:
            date,category,amount=expense
            file.write(f"{date}|{category}|{amount}\n")
    print("Expense saved successfully!")


# function to load expenses   
def load_expenses(expenses,categories):
    if os.path.exists("expenses.txt"):
        with open("expenses.txt","r") as file:
            for line in file:
                date,category,amount=line.strip().split("|")
                amount=float(amount)
                expense=(date,category,amount)
                expenses.append(expense)
                categories.add(category)
    else:
        print("File does not exist")

#function for access category spending
def update_category_totals(expenses,category_totals):
    category_totals.clear()

    for expense in expenses:
        category=expense[1]
        amount=expense[2]

        if category not in category_totals:
            category_totals[category]=0
        category_totals[category]+=amount


# Function Add expense

def add_expense(expenses,categories):
    print("\n---ADD NEW EXPENSE ---")

    date=input("Enter Date (DD-MM-YYYY):")
    while not  valid_date(date) : 
        print("Invalid date! Enter correct date.")
        date = input("Enter Date (DD-MM-YYYY):")

    category=input("Enter category :").strip().title()
    while not category:
        print("category cannot be empty")
        category=input("Enter category:").strip().title()
    try:    
        amount=float(input("Enter amount:"))
        if amount<=0:
            print("Amount should be postive")
            return 
    except ValueError:
        print("Please enter a valid number")
        return
    
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

    
    
# Recurssion for Total Expense
def recursive_total(expenses, index=0):
    if index == len(expenses):
        return 0
    return expenses[index][2] + recursive_total(expenses, index + 1)


#Function for every category spending
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
        if len(expenses)==0:
            print("No Expense found")
        else:
            max_exp=max(category_totals,key=category_totals.get)
            min_exp=min(category_totals,key=category_totals.get)
            print(f"Maximum expense is Rs{category_totals[max_exp]} of {max_exp}")
            print(f"Minimum expense is Rs{category_totals[min_exp]} of {min_exp}")
    elif(user_choice==6):
        print("Thank YOU!")
        break
    else:
        print("Please!,Enter correct Choice")

def save_expenses(expenses):
    with open("expenses.txt","w") as file:
        for expense in expenses:
            date,category,amount=expense
            file.write(f"{date}|{category}|{amount}\n")
    print("Expense saved successfully!")



                