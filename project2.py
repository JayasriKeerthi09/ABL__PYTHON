SLABS = [
    (100, 3.00),
    (100, 5.00),
    (200, 7.00),
    (float("inf"), 9.00),
]
FIXED_CHARGE = 50
SURCHARGE_PERCENT = 5
REBATE_UNITS_LIMIT = 50
REBATE_PERCENT = 10
UNUSUAL_INCREASE_PERCENT = 30


def calculate_bill(units):
    remaining = units
    energy_charge = 0

    for slab_units, rate in SLABS:
        if remaining <= 0:
            break
        used = min(remaining, slab_units)
        energy_charge += used * rate
        remaining -= used

    surcharge = energy_charge * SURCHARGE_PERCENT / 100
    rebate = energy_charge * REBATE_PERCENT / 100 if units <= REBATE_UNITS_LIMIT else 0
    total = energy_charge + FIXED_CHARGE + surcharge - rebate

    return {
        "units": units,
        "energy": round(energy_charge, 2),
        "fixed": FIXED_CHARGE,
        "surcharge": round(surcharge, 2),
        "rebate": round(rebate, 2),
        "total": round(total, 2),
    }


def print_bill(month, bill):
    print(f"\n--- Bill for {month} ---")
    print(f"Units consumed : {bill['units']}")
    print(f"Energy charge  : Rs {bill['energy']}")
    print(f"Fixed charge   : Rs {bill['fixed']}")
    print(f"Surcharge      : Rs {bill['surcharge']}")
    print(f"Rebate         : -Rs {bill['rebate']}")
    print(f"TOTAL          : Rs {bill['total']}")


def compare_months_interactive():
    monthly_units = {}
    n = int(input("Enter number of months to analyze: "))

    for i in range(n):
        month = input(f"Enter name of month {i + 1} (e.g., Jan): ")
        units = int(input(f"Enter unit consumption for {month}: "))
        monthly_units[month] = units

    bills = {}
    for month, units in monthly_units.items():
        bills[month] = calculate_bill(units)
        print_bill(month, bills[month])

    print("\n========== MONTH-TO-MONTH COMPARISON ==========")
    print(f"{'Month':<10}{'Units':<10}{'Total (Rs)':<14}{'Change %':<12}Status")
    print("-" * 60)

    previous_total = None
    for month, bill in bills.items():
        total = bill["total"]
        if previous_total is None:
            print(f"{month:<10}{bill['units']:<10}{total:<14}{'-':<12}First month")
        else:
            change = (total - previous_total) / previous_total * 100
            status = "UNUSUAL INCREASE!" if change > UNUSUAL_INCREASE_PERCENT else "Normal"
            print(f"{month:<10}{bill['units']:<10}{total:<14}{change:<12.2f}{status}")
        previous_total = total

    if bills:
        highest = max(bills, key=lambda m: bills[m]["total"])
        lowest = min(bills, key=lambda m: bills[m]["total"])
        print(f"\nHighest bill: {highest} (Rs {bills[highest]['total']})")
        print(f"Lowest bill : {lowest} (Rs {bills[lowest]['total']})")
        compare_months_interactive()
