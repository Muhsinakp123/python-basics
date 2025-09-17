# Question 1: ATM System (OOP)

# Write a Python program using Object-Oriented Programming (OOP) concepts to create a simple ATM system

class Account:
    def __init__(self, account_number, holder_name, balance):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited successfully. Current Balance: {self.__balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.__balance:
            print("Insufficient Balance!")
        else:
            self.__balance -= amount
            print(f"${amount} withdrawn successfully. Remaining Balance: {self.__balance}")

    def check_balance(self):
        return self.__balance   

    def show_details(self):
        print(f"\n--- Account Details ---")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__holder_name}")
        print(f"Current Balance: ${self.__balance}")


class ATM(Account):
    def __init__(self, account_number, holder_name, balance, pin):
        super().__init__(account_number, holder_name, balance)
        self.__pin = pin

    def validate_pin(self, entered_pin):
        return self.__pin == entered_pin

    def show_details(self):
        print(f"\n--- ATM Account Details ---")
        super().show_details()


# Create ATM user
user = ATM(422322, "Muhsina", 6000, 43235)

# PIN authentication
user_pin = int(input("Enter the PIN: "))
if user.validate_pin(user_pin):
    while True:
        print("\nACCOUNT MENU")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Show Account Details")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            dep_amount = int(input("Enter the amount to deposit: "))
            user.deposit(dep_amount)
        elif choice == 2:
            with_amount = int(input("Enter the amount to withdraw: "))
            user.withdraw(with_amount)
        elif choice == 3:
            print(f"Current Balance: {user.check_balance()}")
        elif choice == 4:
            user.show_details()
        elif choice == 5:
            print("Exiting from ATM. Thank you!")
            break
        else:
            print("Invalid Choice")
else:
    print("Incorrect PIN")
