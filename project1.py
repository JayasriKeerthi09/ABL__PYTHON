MIN_AGGREGATE =int(input("min_aggregate"))
MIN_SUBJECT_MARK =int(input("max_sub_mark"))
MIN_ATTENDANCE =int(input("max_attendance"))
MAX_INCOME =int(input("max_income"))
TOTAL_SCHOLARSHIPS =int(input("total_scholarship"))
students = [
    {"id": 101, "name": "Asha",   "marks": [90, 85, 88, 92], "attendance": 92, "income": 300000},
    {"id": 102, "name": "Ravi",   "marks": [95, 90, 35, 92], "attendance": 90, "income": 200000},
    {"id": 103, "name": "Meena",  "marks": [88, 90, 86, 88], "attendance": 80, "income": 250000},
    {"id": 104, "name": "Kiran",  "marks": [88, 90, 86, 88], "attendance": 85, "income": 250000},
    {"id": 105, "name": "Sita",   "marks": [80, 82, 78, 80], "attendance": 70, "income": 150000},
    {"id": 106, "name": "Arjun",  "marks": [92, 91, 90, 91], "attendance": 95, "income": 800000},
    {"id": 107, "name": "Divya",  "marks": [88, 90, 86, 88], "attendance": 85, "income": 180000},
    {"id": 108, "name": "Suresh", "marks": [78, 76, 80, 79], "attendance": 88, "income": 400000},
]
def calculate_aggregate(marks):
    return sum(marks) / len(marks)
def check_eligibility(student):
    aggregate = calculate_aggregate(student["marks"])
    if aggregate < MIN_AGGREGATE:
        return False, f"Aggregate {aggregate:.2f} is below {MIN_AGGREGATE}"
    if min(student["marks"]) < MIN_SUBJECT_MARK:
        return False, f"A subject score is below {MIN_SUBJECT_MARK}"
    if student["attendance"] < MIN_ATTENDANCE:
        return False, f"Attendance {student['attendance']}% is below {MIN_ATTENDANCE}%"
    if student["income"] > MAX_INCOME:
        return False, f"Income {student['income']} is above {MAX_INCOME}"
    return True, ""
def ranking_key(student):
    return (
        -student["aggregate"],
        student["income"],
        -student["attendance"],
        -max(student["marks"]),
        student["id"],
    )
def allocate_scholarships():
    eligible = []
    rejected = []
    for student in students:
        is_ok, reason = check_eligibility(student)
        student["aggregate"] = calculate_aggregate(student["marks"])
        if is_ok:
            eligible.append(student)
        else:
            rejected.append((student, reason))
    eligible.sort(key=ranking_key)
    return eligible, rejected
eligible, rejected = allocate_scholarships()
print("=== REJECTED STUDENTS ===")
for student, reason in rejected:
    print(f"{student['name']:8} -> {reason}")
print("\n=== RANKED ELIGIBLE STUDENTS ===")
print(f"{'Rank':<5}{'Name':<8}{'Aggr%':<8}{'Attend%':<9}{'Income':<9}{'Result'}")
for rank, student in enumerate(eligible, start=1):
    result = "SCHOLARSHIP AWARDED" if rank <= TOTAL_SCHOLARSHIPS else "Waiting list"
    print(f"{rank:<5}{student['name']:<8}{student['aggregate']:<8.2f}"
          f"{student['attendance']:<9}{student['income']:<9}{result}")
