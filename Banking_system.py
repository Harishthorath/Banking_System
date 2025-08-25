
class BankAccount:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ₹{amount}. New Balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrawn: ₹{amount}. New Balance: ₹{self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def check_balance(self):
        print(f"Account Balance for {self.name} (A/C: {self.account_number}): ₹{self.balance}")



def main():
    print("==== Welcome to Harish Bank ====")
    account_number = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    account = BankAccount(account_number, name)

    while True:
        print("\n--- Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for using Harish Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
