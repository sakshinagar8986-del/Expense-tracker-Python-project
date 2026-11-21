import os
import doctest
from datetime import datetime

#============MAIN DATA STORE================

expenses=[]
categories=set()
category_totals={}
tracker={"expenses": expenses,"categories":categories,"budget":10000,"category_totals":category_totals}



#============VALIDATE DATE==============

def valid_date(date):
    """
    Valid date format.
    >>> valid_date("15-11-2026")
    True
    >>> valid_date("2026-11-15")
    False
    """
    
    try:
        datetime.strptime(date,"%d-%m-%Y")
        return True
    except ValueError:
        return False


#=================== SAVE EXPENSES ==================

def save_expenses(expenses):
    """Save all expenses in a text file."""
    try:
        with open("expenses.txt", "w", encoding="utf-8") as file:
            for expense in expenses:
                date, category, amount = expense
                file.write(f"{date}|{category}|{amount}\n")

        print("Expenses saved successfully!")
        return True

    except OSError:
        print("File error: Expenses could not be saved.")
        return False



#================= LOAD EXPENSES =================

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

#======================= UPDATE CATEGORY TOTAL ===================
def update_category_totals(expenses,category_totals):
    """
    >>> totals = {}
    >>> update_category_totals([("15-11-2026","Food",100.0),("16-11-2026","Food",50.0)],totals)
    >>> totals
    {'Food': 150.0}
    """
    category_totals.clear()

    for expense in expenses:
        category=expense[1]
        amount=expense[2]

        if category not in category_totals:
            category_totals[category]=0
        category_totals[category]+=amount


# ================= ADD EXPENSE =================

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
    
    
# ================= DISPLAY ALL EXPENSES =================

def display_expenses(expenses):
    """
    >>> display_expenses([])
    <BLANKLINE>
    ---ALL EXPENSES---
    No Expenses Found.
    >>> display_expenses([("15-11-2026","Food",250.0)])
    <BLANKLINE>
    ---ALL EXPENSES---
    15-11-2026 Food 250.0
    """
    print("\n---ALL EXPENSES---")
    if (len(expenses)==0):
        print("No Expenses Found.")
    for expense in expenses:
        date,category,amount=expense
        print(date,category,amount)

    
# ================= RECURSIVE TOTAL =================    

def recursive_total(expenses, index=0):
    """
    >>> recursive_total([])
    0
    >>> recursive_total([("15-11-2026", "Food", 100.0), ("16-11-2026", "Travel", 50.5)])
    150.5
    """
    if index == len(expenses):
        return 0
    return expenses[index][2] + recursive_total(expenses, index + 1)


# ================= CATEGORY TOTAL =================
def category_total(category,category_totals):
    """
    >>> category_total("Food", {"Food": 150.0})
    150.0
    >>> category_total("Travel", {"Food": 150.0})
    0
    """
    if category not in category_totals:
        total_per_category=00
    else:
        total_per_category=category_totals[category]
    return total_per_category

#Function for Highest and Lowest Expense
def highest_lowest(expenses):
    """
    >>> highest_lowest([])
    No expense found
    >>> highest_lowest([("15-11-2026", "Food", 100.0), ("16-11-2026", "Travel", 500.0)])
    <BLANKLINE>
     Highest Expense: ('16-11-2026', 'Travel', 500.0)
    <BLANKLINE>
     Lowest  Expense: ('15-11-2026', 'Food', 100.0)
    """
    if(len(expenses)==0):
        print("No expense found")
        return

    max_exp=max(expenses,key=lambda x:x[2])
    min_exp=min(expenses,key=lambda x:x[2])
    print("\n Highest Expense:",max_exp)
    print("\n Lowest  Expense:",min_exp)

# ================= MONTHLY BUDGET =================
def monthly_budget(expenses, budget):
    """
    >>> today = datetime.now().strftime("%d-%m-%Y")
    >>> monthly_budget([(today, "Food", 300.0)], 1000)
    <BLANKLINE>
    Monthly Budget: 1000
    Monthly Spending: 300.0
    You are within your budget.
    >>> monthly_budget([(today, "Food", 300.0)], 200)
    <BLANKLINE>
    Monthly Budget: 200
    Monthly Spending: 300.0
    WARNING! Your monthly budget has been exceeded.
    """
    current_month=datetime.now().month
    current_year=datetime.now().year
    monthly_total=0

    for expense in expenses:
        expense_date=datetime.strptime(expense[0],"%d-%m-%Y")
        if (expense_date.month==current_month and expense_date.year==current_year):
            monthly_total+=expense[2]

    print("\nMonthly Budget:",budget)
    print("Monthly Spending:",monthly_total)

    if monthly_total>budget:
        print("WARNING! Your monthly budget has been exceeded.")
    else:
        print("You are within your budget.")
            
# ================= CATEGORY BAR CHART =================

def category_bar_chart(category_totals):
    """Print category spending using nested loops."""

    print("\n--- CATEGORY SPENDING BAR CHART ---")
    print("Each * represents Rs.100.")

    if len(category_totals) == 0:
        print("No category expenses found.")
        return 0

    # Outer loop: categories
    for category in category_totals:

        amount = category_totals[category]
        star_count = int(amount // 100)

        if amount > 0 and star_count == 0:
            star_count = 1

        print(category, end=" : ")

        # Inner loop: print stars
        for count in range(star_count):
            print("*", end="")

        print(f"  Rs.{amount:.2f}")

    return len(category_totals)




#===MAIN PROGRAM====

#Load pervious expenses
load_expenses(expenses,categories)

#update category dictionary
update_category_totals(expenses,category_totals)


while True:
    print("\n========== EXPENSE TRACKER ==========")

    print("1. ADD EXPENSE")
    print("2. DISPLAY ALL EXPENSES")
    print("3. SHOW TOTAL SPENDING")
    print("4. SHOW TOTAL PER CATEGORY")
    print("5. SHOW HIGHEST AND LOWEST EXPENSE")
    print("6. CHECK MONTHLY BUDGET")
    print("7. EXIT")

    print("=====================================")
    try:
        user_choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 7.")
        continue


    if(user_choice==1):
        add_expense(expenses,categories)
        update_category_totals(expenses,category_totals)
        save_expenses(expenses)

    elif(user_choice==2):
        display_expenses(expenses)
        
    elif(user_choice==3):
        total_exp=recursive_total(expenses)
        print(f"Total Spending: Rs.{total_exp:.2f}")
        
    elif(user_choice==4):

        category=input("Enter category for total spending:").strip().title()
        total=category_total(category,category_totals)
        print(f"Total spending in {category} :Rs{total:.2f} ")

    elif(user_choice==5):
       highest_lowest(expenses)

    elif(user_choice==6):
        monthly_budget(expenses,tracker["budget"])

    elif(user_choice==7):
        save_expenses(expenses)
        print("Thank YOU!")
        break

    else:
        print("Please!,Enter correct Choice")

# ================= RUN DOCTEST =================

if __name__ == "__main__":

    doctest.testmod()

    main()







                
