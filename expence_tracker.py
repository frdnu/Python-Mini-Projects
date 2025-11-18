#Expense Tracker
no_of_spendings = 0
list_of_type_of_expense = []
list_of_amount = []

#Code

print("Welcome to Expense Tracker!")
budget = input("Input your budget for today: ")
budget = int(budget)

def add_a_purchase():
    
    global no_of_spendings, list_of_amount, list_of_type_of_expense

    no_of_spendings += 1
    type_of_expense = input("Enter the type of expensive: ")
    amount = input("Input the amount in KWD: ")

    list_of_type_of_expense.append(type_of_expense)
    list_of_amount.append(int(amount))

    return

    
def remove_a_purchase():

    global no_of_spendings, list_of_type_of_expense, list_of_amount

    if no_of_spendings == 0:
        print("You have no spendings yet!")
        return
    else:  

        print("Your expenses:\n")

        for index in range(no_of_spendings):
            print(f"{index+1}. {list_of_type_of_expense[index]}\n")

        to_delete = input("\nEnter the expense you wanna delete: ")

        for index in range(no_of_spendings):
            if to_delete == list_of_type_of_expense[index]:
                list_of_type_of_expense.pop(index)
                list_of_amount.pop(index)
                no_of_spendings -= 1    
                return
        print("\nExpense does not exist!")
    return


def display():

    global no_of_spendings, list_of_amount, list_of_type_of_expense, budget
    
    if no_of_spendings == 0:
        print("You have no expenses yet!")
        return
    else:
        print("\nFollowing are your expenses:")

        for index in range(no_of_spendings):
            print(f"{index+1}. {list_of_type_of_expense[index]}   |   {list_of_amount[index]} kwd")

        
    return

run = True

while run:
    total_spent = 0
    for index in range(no_of_spendings):
        total_spent += list_of_amount[index]
    budget_remaining = budget - total_spent
        

    print(f"\nMenu: \nYour total budget: {budget}\nRemaining: {budget_remaining}\n")
    print("1. Add a purchase.\n2. Remove a purchase.\n3. Display the total spendings.\n4. Quit the program.")

    option = input("Choose an Option: ")

    if option == "1":
        add_a_purchase()
    elif option == "2":
        remove_a_purchase()
    elif option == "3":
        display()
    elif option == "4":
        print("Quiting Expense Tracker...")
        break
    else:
        print("Your option is invalid. ")