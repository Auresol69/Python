# Python Banking Program

def show_balance(balance): # hien so tien
    print(f"Your balance is ${balance:.2f}")

def deposit(): # nap tien
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance): # rut tien
    amount = float(input("Enter an amount to be withdrawn: "))

    if amount < 0:
        print("Amount must be greater than 0")
        return 0
    elif amount > balance:
        print("Insufficient funds")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program\n1.Show Balance\n2.Deposit\n3.Withdraw\n4.Exit")
        choice = input("Enter your choice (1-4): ")

        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit()
            case "3":
                balance -= withdraw(balance)
            case "4":
                is_running = False
    print("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()