#prompt the user to write monthly expenses type of expense and the amount
#use the reduce method to analyze the expenses and display the total expense
#can use separate functions for your calculations or lambda functions within the main function

from functools import reduce


def userExpenses():
    expenses = []
    while True:
        #prompt user to enter a type of expense
        expense_type = input("Enter type of expense or 'done' to end: ")

        #take expenses and move to next function
        if expense_type.lower() == 'done':
            break

        #prompt user to enter the amount for the expense they entered earlier
        try:
            amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses.append((expense_type, amount))

        #tell the user that they entered a number that will create an error
        except ValueError:
            print("Invalid. Enter a numeric value.")
    return expenses

def analyzeExpenses(expenses):

    #tell the user that there is no expenses to analyze
    if not expenses:
        print("No expenses to analyze.")
        return

#compute the expenses
    total_expenses = reduce(lambda acc, exp: acc + exp[1], expenses, 0)
    highest_expense = reduce(lambda acc, exp: exp if exp[1] > acc[1] else acc, expenses)
    lowest_expense = reduce(lambda acc, exp: exp if exp[1] < acc[1] else acc, expenses)

#display to the user the amount for the 3 expenses
    print (f"\nTotal expenses: ${total_expenses:.2f}")
    print(f"Highest expense: {highest_expense[0]} at ${highest_expense[1]:.2f}")
    print(f"Lowest expense: {lowest_expense[0]} at ${lowest_expense[1]:.2f}")

def main():
    expenses = userExpenses()
    analyzeExpenses(expenses)

if __name__ == "__main__":
    main()
