# Expense-tracker-Python-project
This is our python project
# Expense Tracker
#💰 Daily Expense Tracker

<p align="center">
  <strong>A Python-Based Daily Expense Management System</strong>
  <br>
  Track Expenses • Analyze Spending • Manage Your Budget
</p>

---

## 📌 Project Information

| Project Details | Information |
|---|---|
| **Project Title** | Daily Expense Tracker |
| **Project Number** | Project 5 |
| **Group Number** | Group 5 |
| **Programming Language** | Python 3 |
| **Application Type** | Console-Based Application |
| **Course** | Python Programming |
| **Project Weightage** | 40 Marks |

## 👥 Team Members

This project has been collaboratively developed by the following team members:

| S. No. | Name | Roll Number |
|---|---|---|
| 1 | Sakshi Nagar | 202610101200023|
| 2 | Aman Kumar Barnwal | 202610101200004 |
| 3 | Dipesh Kumar Kumawat | 202610101200037 |
| 4 | Harsh Kushwaha | 202610101200053 |

---

## 📖 Introduction

Managing daily expenses is an essential part of maintaining financial discipline. However, keeping track of everyday spending manually can become difficult when expenses are distributed across different categories.

The **Daily Expense Tracker** is a Python-based application developed to simplify expense management. It allows users to record daily expenses, organize spending categories, calculate total expenditure, analyze category-wise spending, and monitor their monthly budget.

The application provides a simple menu-driven interface that makes expense management easier and more organized.

This project demonstrates the practical implementation of fundamental Python programming concepts through a real-world application.

## 🎯 Project Objectives

The main objectives of this project are:

- To develop a system for recording daily expenses.
- To organize expenses into different categories.
- To calculate total spending and category-wise expenditure.
- To identify the highest and lowest expenses.
- To compare spending with a predefined monthly budget.
- To provide warnings when the monthly budget is exceeded.
- To save expense records in a file and retrieve them when the program starts.
- To demonstrate the practical application of Python programming concepts.

## ✨ Key Features

### 1. Add Expense
- Enter the expense date.
- Specify the expense category.
- Enter the expense amount.
- Store expense information for further calculations.

### 2. Expense Management
- Maintain a collection of expense records.
- Organize expenses using Python data structures.
- Manage expense categories without unnecessary duplication.

### 3. Total Expense Calculation
- Calculate the total amount spent.
- Use a recursive function to calculate the sum of all expense amounts.

### 4. Category-Wise Analysis
- Calculate total expenditure for each category.
- Store category totals using a dictionary.
- Display organized spending information.

### 5. Highest and Lowest Expense
- Identify the expense with the highest amount.
- Identify the expense with the lowest amount.

### 6. Monthly Budget Management
- Maintain a predefined monthly budget.
- Compare total expenditure with the budget.
- Display a warning when spending exceeds the available budget.

### 7. Expense Visualization
- Generate a category-wise expense bar chart.
- Represent spending using asterisks (`*`).
- Use nested loops to display the chart.

### 8. File Handling
- Save expense records in a text file.
- Load previously saved expenses when the program starts.
- Maintain records between different program executions.

### 9. Input Validation and Error Handling
- Handle invalid user inputs.
- Prevent the program from crashing because of incorrect input.
- Handle missing files using exception handling.
- Display appropriate error messages.

---

## 🛠️ Technologies and Python Concepts Used

The project uses Python programming concepts covered in Lectures 1–13.

| Python Concept | Application in Project |
|---|---|
| Variables and Data Types | Store dates, categories and expense amounts |
| Strings | Process and format user input |
| Operators | Perform expense calculations and comparisons |
| Lists | Store multiple expense records |
| Tuples | Represent individual expense records |
| Sets | Maintain unique expense categories |
| Dictionaries | Store category-wise expense totals |
| Conditional Statements | Apply validation and budget conditions |
| For and While Loops | Iterate through expenses and manage the menu |
| Nested Loops | Generate category-wise expense charts |
| Functions | Divide the application into reusable operations |
| Recursion | Calculate total expense amounts |
| File Handling | Save and load expense information |
| Doctests | Test functions using example inputs and outputs |
| Exception Handling | Handle invalid inputs and file-related errors |

## 📊 Data Structures

### 1. Main Dictionary

The dictionary acts as the main data store of the application.

```python
expenses = []
categories = set()

tracker = {
    "expenses": expenses,
    "categories": categories,
    "budget": 10000,
    "category_totals": {}
}
```

### 2. Expense Record Using Tuples

Each expense is represented using a tuple containing three values:

```python
expense = (date, category, amount)
```

Example:

```python
("20-11-2026", "Food", 250)
("20-11-2026", "Travel", 100)
("21-11-2026", "Shopping", 500)
```

### 3. Set for Unique Categories

A set is used to maintain unique expense categories and avoid duplicate entries.

```python
categories = {"Food", "Travel", "Shopping"}
```

### 4. Dictionary for Category Totals

A dictionary stores the total expenditure for each category.

```python
category_totals = {
    "Food": 2500,
    "Travel": 1200,
    "Shopping": 2000
}
```

---

## 📈 Expense Visualization

The application includes a category-wise bar chart using asterisks to represent expenditure.

Illustrative output:

```text
========== EXPENSE ANALYSIS ==========

Each * represents Rs.100.
Food : *************************  Rs.2535.00
Travel : *****************  Rs.1739.00
Saving : ************  Rs.1200.00
Electricity : ********  Rs.800.00
Movie : ******  Rs.600.00
Shopping : **********************************  Rs.3400.00

======================================
```

The chart is generated using nested loops, as required by the project guidelines.

## 🔁 Recursion Implementation

A recursive function is used to calculate the total amount of all recorded expenses.

The function processes expense amounts recursively until it reaches its base case.

This demonstrates the practical use of recursion in Python programming.

## 💾 File Handling

The application uses a text file to maintain expense records.

File handling provides the following functionality:

- Saving expense records.
- Loading previously saved records.
- Maintaining data between program executions.
- Handling missing files through exception handling.

## 🧪 Testing and Validation

The application is designed to handle normal and incorrect inputs.

The following test scenarios are considered:

| S. No. | Test Scenario | Expected Result |
|---|---|---|
| 1 | Enter a valid expense | Expense is recorded |
| 2 | Enter an invalid amount | Appropriate error message |
| 3 | Calculate total expenses | Correct total is displayed |
| 4 | Add an existing category | Duplicate category is avoided |
| 5 | Exceed the monthly budget | Budget warning is displayed |
| 6 | Display highest expense | Highest expense is identified |
| 7 | Display lowest expense | Lowest expense is identified |
| 8 | Load a missing data file | Error is handled without crashing |
| 9 | Save expense records | Records are saved successfully |
| 10 | Run doctest examples | Function examples are tested |

## ⚙️ Installation and Execution

### Prerequisites

- Python 3.x
- Visual Studio Code or another Python editor.
- Terminal or Command Prompt.

No external libraries, databases, or graphical interfaces are required.

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the Project Folder

```bash
cd Daily-Expense-Tracker
```

### Step 3: Run the Application

```bash
python daily_expense_tracker.py
```

If your system uses the `python3` command:

```bash
python3 daily_expense_tracker.py
```

### Step 4: Run Doctests

```bash
python -m doctest -v daily_expense_tracker.py
```

This command executes the doctest examples included in the functions.

---

## 📂 Project Structure

```text
Expense-tracker-Python-project
│
├── Expense_tracker.py
├── expenses.txt
└── README.md
```

**Note:** The program is designed as a single Python `.py` file, accompanied by its text data file, in accordance with the course guidelines.

## 🎓 Learning Outcomes

Through this project, the team gained practical experience in:

1. Understanding Python variables and data types.
2. Working with lists, tuples, sets and dictionaries.
3. Developing menu-driven applications.
4. Applying conditional statements and loops.
5. Implementing nested loops for text-based visualization.
6. Creating reusable functions with parameters and return values.
7. Understanding recursion and its base case.
8. Managing persistent data using file handling.
9. Testing functions using doctests.
10. Handling invalid inputs and exceptions.
11. Improving logical thinking and problem-solving skills.
12. Collaborating on a group programming project.

## 🚀 Future Scope

The project can be extended with additional functionalities in future versions, such as:

- Date-wise expense reports.
- Monthly and yearly spending summaries.
- More detailed budget analysis.
- Advanced expense visualization.
- Additional expense categories.
- Improved reporting features.

## ⚠️ Project Limitations

- The application uses a console-based interface.
- Expense information is maintained through local text-file storage.
- The application does not use an external database.
- The project focuses on fundamental expense management functionality.

---

## 🤝 Team Contributions

The project was developed collaboratively by all four members of Group 5.

| Team Member | Contribution |
|---|---|
| Sakshi Nagar | Project development and implementation |
| Aman Kumar Barnwal | Project development and implementation |
| Dipesh Kumar Kumawat | Project development and implementation |
| Harsh Kushwaha | Project development and implementation |

## 📜 Academic Information

This project is submitted as part of the **Python Programming Course Project**.

The project follows the official Project 5 brief and demonstrates the compulsory Python programming concepts specified in the course guidelines.

---

## 👨‍💻 Developed By

**Group 5 – Daily Expense Tracker**

- Sakshi Nagar
- Aman Kumar Barnwal
- Dipesh Kumar Kumawat
- Harsh Kushwaha

**Project:** Daily Expense Tracker  
**Project Number:** 5  
**Group Number:** 5  
**Course:** Python Programming

---

<p align="center">
  <strong>Made with ❤️ and Python 🐍</strong>
  <br>
  <em>Track Expenses. Understand Spending. Manage Money Better.</em>
</p>
