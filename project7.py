ANSWER_KEY = "ABCDABCDAB"
MARKS_CORRECT = 4
MARKS_WRONG = -1
MARKS_UNANSWERED = 0
students = {
    "Ravi":   "ABCDABCDAB",
    "Sita":   "ABCD-BCD-B",
    "Anil":   "DCBADCBADC",
    "Meena":  "AB-D-B-DAB",
}
def evaluate(answer_key, student_answers):
    correct = 0
    incorrect = 0
    unanswered = 0
    for i in range(len(answer_key)):
        if i < len(student_answers):
            given = student_answers[i].upper()
        else:
            given = "-"
        if given == "-" or given == " ":
            unanswered += 1
        elif given == answer_key[i]:
            correct += 1
        else:
            incorrect += 1
    score = (correct * MARKS_CORRECT
             + incorrect * MARKS_WRONG
             + unanswered * MARKS_UNANSWERED)
    return correct, incorrect, unanswered, score
results = []
for name, answers in students.items():
    c, w, u, score = evaluate(ANSWER_KEY, answers)
    results.append((name, c, w, u, score))
print(f"Answer Key: {ANSWER_KEY}")
print(f"Marking: +{MARKS_CORRECT} correct, {MARKS_WRONG} wrong, "
      f"{MARKS_UNANSWERED} unanswered\n")
print(f"{'Student':<10}{'Correct':<10}{'Wrong':<8}{'Unanswered':<12}{'Score':<6}")
print("-" * 46)
for name, c, w, u, score in results:
    print(f"{name:<10}{c:<10}{w:<8}{u:<12}{score:<6}")
print("\nRank List:")
ranked = sorted(results, key=lambda r: r[4], reverse=True)
for rank, r in enumerate(ranked, start=1):
    print(f"{rank}. {r[0]} - {r[4]} marks")