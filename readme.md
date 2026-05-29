# CLI Expense Tracker

A simple command-line Expense Tracker built using Python. The application allows users to add expenses, store them in a CSV file, and generate expense summaries by category while tracking the remaining budget.

## Features

* Add new expenses
* Categorize expenses
* Store expenses in a CSV file
* Read expenses from file
* Calculate total expenses
* Generate category-wise summaries
* Track remaining budget
* Input validation for expense amount and category selection

## Concepts Used

* Python Functions
* Function Parameters & Return Values
* Object-Oriented Programming (Classes & Objects)
* Constructors (`__init__`)
* Special Methods (`__repr__`)
* Lists and Dictionaries
* Loops (`for`, `while`)
* Conditional Statements
* File Handling (`open`, read, write, append)
* Exception Handling (`try`, `except`)
* List Type Hints
* Module Imports
* `if __name__ == "__main__"` Execution Flow

## What I Learned

* How to design and use custom Python classes
* How objects are created and stored in memory
* How to read from and write to files
* How to process and summarize data using dictionaries
* How to validate user input
* How function calls and parameter passing work
* How to handle runtime errors using exception handling
* How to organize Python code into reusable functions and modules
* How to debug and interpret Python error messages

## Debugging Challenges Solved

### Object Representation

* Implemented `__repr__()` to display meaningful expense information instead of memory addresses.

### Input Validation

* Fixed category validation logic by using the selected index correctly.

### Function Signature Errors

* Resolved argument mismatch issues between function definitions and function calls.

### Variable Scope Issues

* Fixed `UnboundLocalError` caused by incorrect variable references.

### Naming Conflicts

* Resolved conflicts caused by using parameter names that shadowed class names.

### File Formatting Issues

* Fixed CSV formatting problems caused by extra spaces and inconsistent data storage.

### Type Hint Errors

* Corrected incorrect list type hint syntax.

## Sample Expense Record

```csv
burger,Food,500
movie,Entertainment,300
travel,Transport,1000
```

## Future Improvements

* Edit existing expenses
* Delete expenses
* Monthly expense reports
* Data visualization using charts
* Database integration (SQLite/MySQL)
* GUI version using Tkinter or PyQt
