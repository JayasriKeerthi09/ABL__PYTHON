MIN_LENGTH = 10
MAX_REPEAT = 2  # a character may appear at most 2 times in a row (so "aaa" fails)
PROHIBITED = ["password", "qwerty", "123456", "admin", "letmein"]
SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{};:,.<>?/"
def check_length(password):
    if len(password) < MIN_LENGTH:
        return [f"Too short: {len(password)} characters, but at least {MIN_LENGTH} are required."]
    return []
def check_character_categories(password):
    errors = []
    if not any(ch.isupper() for ch in password):
        errors.append("Missing an uppercase letter (A-Z).")
    if not any(ch.islower() for ch in password):
        errors.append("Missing a lowercase letter (a-z).")
    if not any(ch.isdigit() for ch in password):
        errors.append("Missing a digit (0-9).")
    if not any(ch in SPECIAL_CHARACTERS for ch in password):
        errors.append(f"Missing a special character (e.g. {SPECIAL_CHARACTERS[:8]}).")
    return errors
def check_repetition(password):
    # Walk through the password and count how long the current run of the same character is.
    run_length = 1
    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            run_length += 1
            if run_length > MAX_REPEAT:
                return [f"Character '{password[i]}' repeats more than {MAX_REPEAT} times in a row."]
        else:
            run_length = 1
    return []
def check_prohibited(password):
    errors = []
    lowered = password.lower()  # lowercase so "PassWord" is also caught
    for word in PROHIBITED:
        if word in lowered:
            errors.append(f"Contains the prohibited word/pattern '{word}'.")
    return errors
def validate_password(password):
    errors = []
    errors += check_length(password)
    errors += check_character_categories(password)
    errors += check_repetition(password)
    errors += check_prohibited(password)
    return errors
if __name__ == "__main__":
    samples = [
        "Tr0ub4dor&Horse",
        "short1A!",
        "alllowercase123!",
        "Passw0rd!!!!xyz",
        "AAAbbb111###",
        "MyAdmin#2024Safe",
    ]
    for pw in samples:
        problems = validate_password(pw)
        print(f"Password: {pw}")
        if problems:
            print("  RESULT: FAIL")
            for p in problems:
                print(f"   - {p}")
        else:
            print("  RESULT: PASS")
        print()