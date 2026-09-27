# Welcome Message
print('Welcome to the Daily Expense Tracker!')

# Display Menu with a line break
print('\nMenu:')
print('1. Add a new expense')
print('2. View all expenses')
print('3. Calculate total and average expenses')
print('4. Clear all expenses')
print('5. Exit')

# Empty list to store expenses
expenses = []

while True:
    # Get the user choice
    choice = input('Enter your choice: ')

# 1. Add a new expense
    if choice == '1':
        amount = float(input('Enter expense amount: '))
        expenses.append(amount)
        print('Expense added successfully!')

# 2. View all expenses
    elif choice == '2':
        if len(expenses) == 0:
            print('No expenses recorded yet.')
        else:
            for index, exp in enumerate(expenses):
                print(f'{index + 1}. {exp}')

# 3. Calculate total and average expenses
    elif choice == '3':
        if len(expenses) == 0:
            print('No expenses recorded yet.')
        else:
            total = 0
            for exp in expenses:
                total += exp
            average = total / len(expenses)
            print(f'Total expense: {total}')
            print(f'Average expense: {average}')

# 4. Clear all expenses
    elif choice ==  '4':
        expenses = []
        print('All expenses cleared')

# 5. Exit the program
    elif choice == '5':
        print('Exiting the Daily Expense Tracker. Goodbye!')
        break
