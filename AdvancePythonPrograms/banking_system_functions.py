balance = 0

def create_account():
    global balance
    name = input("Enter your name: ")
    balance = float(input("Enter initial deposit amount: "))
    print("Account created successfully for", name)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Updated balance:", balance)
    else:
        print("Invalid amount")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")

def check_balance():
    print("Current balance:", balance)

while True:
    print("\n1.Create 2.Deposit 3.Withdraw 4.Check 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        break