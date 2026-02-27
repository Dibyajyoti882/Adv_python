def login():
    user_id = "admin"
    password = "1234"
    attempts = 3

    while attempts > 0:
        print("\nLogin")
        if input("Enter ID: ") == user_id and input("Enter Password: ") == password:
            print("Login Successful")
            return True
        attempts -= 1
        print("Wrong ID or Password")
        print("Attempts left:", attempts)

    print("Account Locked")
    return False


def deposit(balance, transactions, amount):
    balance += amount
    transactions.append("Deposited: " + str(amount))
    return balance


def withdraw(balance, transactions, amount):
    if amount <= balance:
        balance -= amount
        transactions.append("Withdrew: " + str(amount))
    else:
        print("Insufficient Balance")
    return balance


def check_balance(balance):
    print("Current Balance:", balance)


def transaction_history(transactions):
    print("Transaction History:")
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print(t)
if login():
    balance = 0
    transactions = []

    while True:
        print("\n1.Deposit 2.Withdraw 3.Balance 4.History 5.Exit")
        choice = input("Choose: ")

        if choice == '1':
            amt = float(input("Enter amount: "))
            balance = deposit(balance, transactions, amt)

        elif choice == '2':
            amt = float(input("Enter amount: "))
            balance = withdraw(balance, transactions, amt)

        elif choice == '3':
            check_balance(balance)

        elif choice == '4':
            transaction_history(transactions)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice")
