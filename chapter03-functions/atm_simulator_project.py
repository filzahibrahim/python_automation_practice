balance = 100 #initial balance

def deposit(current_balance):
    try: #code that might cause an error goes inside try
        amount = int(input("Enter Amount: ")) #asking for deposit amount
        if amount > 0: #conditions
            new_balance = current_balance + amount #adding the deposit amount in balance and updating balance 
            print(f"Your new balance is: {new_balance}") #printing the new balance
            return new_balance
        elif amount < 0:
            print("Amount can not be less than 0")
            return current_balance
        else:
            print("Amount can not be zero")
            return current_balance
    except ValueError:
        print("Please enter a number!")
        return current_balance

def withdraw(currentBalance):
    try: #code that might cause an error goes inside try
            amount = int(input("Enter Amount: ")) #asking for withdrawal amount
            if amount > currentBalance: #conditions
                print(f"Not enough money")
                return currentBalance
            elif amount <= 0:
                print("Amount can not be less than or equals to zero")
                return currentBalance
            else:
                new_balance = currentBalance - amount #substracting the deposit amount in current balance and updating balance 
                print(f"Your new balance is: {new_balance}") #printing the new balance
                return new_balance
    except ValueError:
        print("Please enter a number!")
        return currentBalance

while True:
    choice = int(input(""" 
    1. Deposit
    2. Withdraw
    3. Check Balance
    4. Exit

    """))
    if choice == 1:
        balance = deposit(balance)
    elif choice == 2:
        balance = withdraw(balance)
    elif choice == 3:
        print(f"Your current balance is: {balance}")
    elif choice == 4:
        print("Thank you for trying my ATM Simulator")
    else:
        print("Please choose from the given numbers!")
        break