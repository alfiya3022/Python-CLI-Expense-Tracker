''' Well, it turns out that a lot of the times you
build Python apps and Python scripts, but then you have ideas to make it part of another
app or make it part of an automated workflow. So you end up kind of reusing your file or your code.
And if you just put it like this, as soon as you import that, this main is going to run
and we don't like that. To make sure that this runs only when we run this file and not when we run it as part of another file.
There's a trick we can do, which is to put a condition. And the condition we can use is if name equals main. if __main__ == "__main__":
Now to break down what this means, this underscore name is a special variable in Python, it will be equal to double underscore main when we run this as a file. So this will only be true when we run it directly instead of importing it. Therefore, by putting this condition, we can run our app only when we run it directly.
So if you ever see this structure in Python apps, this is what it's doing. So now we have our main function.
'''


from expense import Expense
import os


def main():
    print("Welcome to the Expense Tracker!")

    expense_file_name = "expenses.csv"
    budget = 10000.0

    expense = get_user_expense()
    print(f"\nYou entered: {expense}")

    save_expense_to_file(expense, expense_file_name)

    summarize_expense(expense_file_name, budget)


def get_user_expense():

    expense_name = input("Enter expense name: ")

    while True:
        try:
            expense_amount = float(input("Enter expense amount: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    expense_categories = [
        "Food",
        "Clothing",
        "Household",
        "Entertainment",
        "Transport",
        "Other"
    ]

    while True:

        print("\nSelect Category:")

        for i, category in enumerate(expense_categories, start=1):
            print(f"{i}. {category}")

        try:
            selected_index = int(
                input(f"Enter category number [1-{len(expense_categories)}]: ")
            ) - 1

            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]

                return Expense(
                    name=expense_name,
                    category=selected_category,
                    amount=expense_amount
                )

            print("Invalid category number.")

        except ValueError:
            print("Please enter a valid number.")


def save_expense_to_file(expense, expense_file_name):

    print("\nSaving expense...")

    print("File location:")
    print(os.path.abspath(expense_file_name))

    with open(expense_file_name, "a") as file:
        file.write(
            f"{expense.name},{expense.category},{expense.amount}\n"
        )

    print("Expense saved successfully.")


def summarize_expense(expense_file_name, budget):

    print("\nExpense Summary")

    expenses: list[Expense] = []

    try:

        with open(expense_file_name, "r") as file:

            for line in file:

                expense_name, expense_category, expense_amount = (
                    line.strip().split(",")
                )

                expense = Expense(
                    name=expense_name,
                    category=expense_category,
                    amount=float(expense_amount)
                )

                expenses.append(expense)

    except FileNotFoundError:
        print("No expense file found.")
        return

    total_expenses = sum(exp.amount for exp in expenses)

    amount_by_category = {}

    for expense in expenses:

        if expense.category in amount_by_category:
            amount_by_category[expense.category] += expense.amount
        else:
            amount_by_category[expense.category] = expense.amount

    print("\nExpenses by Category:")

    for category, amount in amount_by_category.items():
        print(f"{category}: ₹{amount}")

    print(f"\nTotal Expenses: ₹{total_expenses}")

    remaining_budget = budget - total_expenses

    print(f"Remaining Budget: ₹{remaining_budget}")


if __name__ == "__main__":
    main()