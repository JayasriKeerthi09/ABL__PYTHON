students = [
    {"id": "101", "name": "Anil", "marks": [36, 75, 82]},
    {"id": "102", "name": "Bhavana", "marks": [32, 60, 70]},
    {"id": "103", "name": "Charan", "marks": [85, 90, 92]},
    {"id": "104", "name": "Divya", "marks": [38, 37, 80]}
]

print(f"{'ID':<6}{'Name':<12}{'Original Marks':<18}{'Grace':<8}{'Final Marks':<18}{'Status'}")
print("-" * 75)

for s in students:
    orig = list(s["marks"])
    final = list(orig)
    hard_fail = any(m < 35 for m in orig)
    deficits = [40 - m for m in orig if 35 <= m < 40]
    tot_grace = sum(deficits)

    if all(m >= 40 for m in orig):
        status = "PASS"
        applied = 0
    elif not hard_fail and tot_grace <= 5:
        final = [40 if 35 <= m < 40 else m for m in orig]
        status = "PASS (With Grace)"
        applied = tot_grace
    else:
        status = "FAIL"
        applied = 0

    print(f"{s['id']:<6}{s['name']:<12}{str(orig):<18}{applied:<8}{str(final):<18}{status}")
