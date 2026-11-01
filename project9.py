MIN_ATTENDANCE = 75
MIN_LABS = 80
MIN_INTERNAL = 40
def check_eligibility(attendance, lab_completion, internal_marks, fee_cleared):
    """Checks all 4 conditions and returns a list of unmet requirements."""
    problems = []
    if attendance < MIN_ATTENDANCE:
        problems.append(f"Attendance is {attendance}% (minimum required: {MIN_ATTENDANCE}%)")
    if lab_completion < MIN_LABS:
        problems.append(f"Lab completion is {lab_completion}% (minimum required: {MIN_LABS}%)")
    if internal_marks < MIN_INTERNAL:
        problems.append(f"Internal marks are {internal_marks} (minimum required: {MIN_INTERNAL})")
    if not fee_cleared:
        problems.append("Fees are not cleared")
    return problems
def get_number(message, low, high):
    while True:
        try:
            value = float(input(message))
            if low <= value <= high:
                return value
            print(f"  Please enter a value between {low} and {high}.")
        except ValueError:
            print("  Invalid input. Please enter a number.")
def get_yes_no(message):
    """Keeps asking until the user types yes or no."""
    while True:
        answer = input(message).strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("  Please type yes or no.")
def main():
    print("=== Final Examination Eligibility Checker ===\n")
    name = input("Student name: ")
    attendance = get_number("Attendance percentage (0-100): ", 0, 100)
    lab_completion = get_number("Lab completion percentage (0-100): ", 0, 100)
    internal_marks = get_number("Internal assessment marks (0-100): ", 0, 100)
    fee_cleared = get_yes_no("Are all fees cleared? (yes/no): ")
    problems = check_eligibility(attendance, lab_completion, internal_marks, fee_cleared)
    print("\n--- RESULT for", name, "---")
    if len(problems) == 0:
        print("ELIGIBLE to appear for the final examination.")
    else:
        print("NOT ELIGIBLE. Unmet requirements:")
        for number, problem in enumerate(problems, start=1):
            print(f"  {number}. {problem}")
main()