
accounts = {
    1001: ["Roshan", 5000],
    1002: ["Rahul", 3000],
    1003: ["Ankit", 7000]
}

current_account = 0  


def switch_account():
    global current_account
    
    acc_no = int(input("Enter account number: "))
    
    if acc_no in accounts:
        current_account = acc_no
        print("Account switched successfully")
        print("Welcome", accounts[acc_no][0])
    else:
        print("Account not found")


def check_balance():
    if current_account == 0:
        print("First select account")
    else:
        print("Balance is:", accounts[current_account][1])


def deposit():
    if current_account == 0:
        print("First select account")
    else:
        amount = int(input("Amount to deposit: "))
        accounts[current_account][1] = accounts[current_account][1] + amount
        print("Money deposited")


def withdraw():
    if current_account == 0:
        print("select account")
    else:
        amount = int(input("Enter amount to withdraw: "))
        
        if amount <= accounts[current_account][1]:
            accounts[current_account][1] = accounts[current_account][1] - amount
            print("collect cash")
        else:
            print("Insufficient balance")


while True:
    print("\nATM MENU")
    print("1. Switch Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        switch_account()
    elif choice == "2":
        check_balance()
    elif choice == "3":
        deposit()
    elif choice == "4":
        withdraw()
    elif choice == "5":
        print("Thank you")
        break
    else:
        print("Wrong choice")