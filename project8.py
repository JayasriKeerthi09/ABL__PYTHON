CORRECT_PIN = 1234
MAX_PIN_ATTEMPTS = 3
MIN_BALANCE = 500
MAX_DEPOSIT = 100000
MAX_WITHDRAW = 20000
DAILY_WITHDRAW_LIMIT = 50000
MULTIPLE_OF = 100
balance = 10000
withdrawn_today = 0
transactions = []
def get_amount(prompt):
    """Keep asking until the user types a valid positive number."""
    while True:
        text = input(prompt)
        try:
            amount = float(text)
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
        if amount <= 0:
            print("Amount must be greater than 0.")
            continue
        if amount % MULTIPLE_OF != 0:
            print(f"Amount must be a multiple of {MULTIPLE_OF}.")
            continue
        return amount
def login():
    """Allow limited PIN attempts."""
    for attempt in range(1, MAX_PIN_ATTEMPTS + 1):
        try:
            pin = int(input("Enter your 4-digit PIN: "))
        except ValueError:
            pin = -1
        if pin == CORRECT_PIN:
            print("Login successful!\n")
            return True
        print(f"Wrong PIN. Attempts left: {MAX_PIN_ATTEMPTS - attempt}")
    print("Card blocked. Too many wrong attempts.")
    return False
def deposit():
    global balance
    amount = get_amount("Enter deposit amount: ")
    if amount > MAX_DEPOSIT:
        print(f"Limit exceeded! Maximum deposit is {MAX_DEPOSIT}.")
        return
    balance += amount
    transactions.append(("Deposit", amount, balance))
    print(f"Deposited {amount:.2f}. New balance: {balance:.2f}")
def withdraw():
    global balance, withdrawn_today
    amount = get_amount("Enter withdrawal amount: ")
    if amount > MAX_WITHDRAW:
        print(f"Limit exceeded! Maximum per withdrawal is {MAX_WITHDRAW}.")
    elif withdrawn_today + amount > DAILY_WITHDRAW_LIMIT:
        left = DAILY_WITHDRAW_LIMIT - withdrawn_today
        print(f"Daily limit exceeded! You can still withdraw {left:.2f} today.")
    elif balance - amount < MIN_BALANCE:
        print(f"Insufficient funds! You must keep a minimum balance of {MIN_BALANCE}.")
    else:
        balance -= amount
        withdrawn_today += amount
        transactions.append(("Withdrawal", amount, balance))
        print(f"Withdrew {amount:.2f}. New balance: {balance:.2f}")
def check_balance():
    print(f"Current balance: {balance:.2f}")
def show_summary():
    print("\n------ Transaction Summary ------")
    if not transactions:
        print("No transactions yet.")
        return
    total_dep = 0
    total_wd = 0
    for number, (kind, amount, bal) in enumerate(transactions, start=1):
        print(f"{number}. {kind:<11} {amount:>10.2f}   Balance: {bal:.2f}")
        if kind == "Deposit":
            total_dep += amount
        else:
            total_wd += amount
    print("---------------------------------")
    print(f"Total deposited : {total_dep:.2f}")
    print(f"Total withdrawn : {total_wd:.2f}")
    print(f"Current balance : {balance:.2f}")
def main():
    print("===== WELCOME TO THE ATM =====")
    if not login():
        return
    while True:
        print("\n------ ATM MENU ------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Inquiry")
        print("4. Transaction Summary")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            check_balance()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
main()