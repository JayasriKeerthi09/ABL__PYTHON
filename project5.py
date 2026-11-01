STARTING_BALANCE = 1000
MAX_PER_WITHDRAWAL = 500
DAILY_WITHDRAWAL_LIMIT = 1000
transactions = [
    ("deposit", 200),
    ("withdraw", 300),
    ("withdraw", 600),
    ("deposit", -50),
    ("withdraw", 400),
    ("transfer", 100),
    ("withdraw", 500),
    ("deposit", "abc"),
    ("withdraw", 2000),
    ("deposit", 150),
]
balance = STARTING_BALANCE
withdrawn_today = 0
accepted = []
rejected = []
def process_transaction(kind, amount):
    """Try to process one transaction.
    Returns (True, "OK") if accepted, or (False, reason) if rejected."""
    global balance, withdrawn_today
    if not isinstance(amount, (int, float)):
        return False, "Amount is not a number"
    if amount <= 0:
        return False, "Amount must be greater than zero"
    if kind == "deposit":
        balance += amount
        return True, "OK"
    if kind == "withdraw":
        if amount > MAX_PER_WITHDRAWAL:
            return False, f"Exceeds per-withdrawal limit of {MAX_PER_WITHDRAWAL}"
        if withdrawn_today + amount > DAILY_WITHDRAWAL_LIMIT:
            return False, f"Exceeds daily limit of {DAILY_WITHDRAWAL_LIMIT}"
        if amount > balance:
            return False, "Insufficient funds"
        balance -= amount
        withdrawn_today += amount
        return True, "OK"
    return False, f"Unknown transaction type '{kind}'"
print(f"Starting balance: {STARTING_BALANCE}\n")
for number, (kind, amount) in enumerate(transactions, start=1):
    success, message = process_transaction(kind, amount)
    if success:
        accepted.append((kind, amount))
        print(f"#{number} {kind} {amount}: ACCEPTED -> balance = {balance}")
    else:
        rejected.append((kind, amount, message))
        print(f"#{number} {kind} {amount}: REJECTED ({message})")
total_deposits = sum(amt for kind, amt in accepted if kind == "deposit")
total_withdrawals = sum(amt for kind, amt in accepted if kind == "withdraw")
print("\n===== TRANSACTION SUMMARY =====")
print(f"Starting balance     : {STARTING_BALANCE}")
print(f"Total transactions   : {len(transactions)}")
print(f"Accepted             : {len(accepted)}")
print(f"Rejected             : {len(rejected)}")
print(f"Total deposited      : {total_deposits}")
print(f"Total withdrawn      : {total_withdrawals}")
print(f"Final balance        : {balance}")
if rejected:
    print("\nRejected transactions:")
    for kind, amount, reason in rejected:
        print(f"  - {kind} {amount}: {reason}")