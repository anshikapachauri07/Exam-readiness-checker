
print("================================")
print("     EXAM READINESS CHECKER")
print("================================")

name = input("Enter your name: ")

while True:
    total_topics = int(input("Enter total number of topics: "))
    completed_topics = int(input("Enter number of topics completed: "))

    if total_topics > 0 and 0 <= completed_topics <= total_topics:
        break
    else:
        print("Invalid input! Please enter valid topic numbers.")

completion = (completed_topics / total_topics) * 100

if completion >= 80:
    syllabus_status = "Excellent"
elif completion >= 60:
    syllabus_status = "Good"
elif completion >= 40:
    syllabus_status = "Moderate"
else:
    syllabus_status = "Needs Improvement"

while True:
    attempted = int(input("Enter practice questions attempted: "))
    correct = int(input("Enter number of correct answers: "))

    if attempted > 0 and 0 <= correct <= attempted:
        break
    else:
        print("Invalid input! Please enter valid practice numbers.")

accuracy = (correct / attempted) * 100

if accuracy >= 80:
    practice_status = "Excellent"
elif accuracy >= 60:
    practice_status = "Good"
elif accuracy >= 40:
    practice_status = "Moderate"
else:
    practice_status = "Needs Improvement"

while True:
    mock_tests = int(input("Enter number of mock tests attempted: "))
    mock_score = float(input("Enter average mock test score: "))

    if mock_tests > 0 and 0 <= mock_score <= 100:
        break
    else:
        print("Invalid input! Please enter valid mock test details.")

if mock_score >= 80:
    mock_status = "Excellent"
elif mock_score >= 60:
    mock_status = "Good"
elif mock_score >= 40:
    mock_status = "Moderate"
else:
    mock_status = "Needs Improvement"

while True:
    revision_planned = int(input("Enter planned revision sessions: "))
    revision_completed = int(input("Enter completed revision sessions: "))

    if revision_planned > 0 and 0 <= revision_completed <= revision_planned:
        break
    else:
        print("Invalid input! Please enter valid revision details.")

revision_percentage = (revision_completed / revision_planned) * 100

if revision_percentage >= 80:
    revision_status = "Excellent"
elif revision_percentage >= 60:
    revision_status = "Good"
elif revision_percentage >= 40:
    revision_status = "Moderate"
else:
    revision_status = "Needs Improvement"

def overall_readiness(syllabus, practice, mock_test, revision):

    overall_score = (syllabus + practice + mock_test + revision) / 4

    if overall_score >= 80:
        status = "Excellent"
    elif overall_score >= 60:
        status = "Good"
    else:
        status = "Needs Improvement"

    return overall_score, status

score, status = overall_readiness(
    completion,
    accuracy,
    mock_score,
    revision_percentage
)

weak_areas = []

if completion < 60:
    weak_areas.append("Syllabus Completion")

if accuracy < 60:
    weak_areas.append("Practice Accuracy")

if mock_score < 60:
    weak_areas.append("Mock Test Performance")

if revision_percentage < 60:
    weak_areas.append("Revision")

print()
print("========================================")
print("          FINAL RESULT")
print("========================================")

print("Student Name:", name)

print()
print("---------- SYLLABUS ----------")
print("Completion:", round(completion, 2), "%")
print("Status:", syllabus_status)

print()
print("---------- PRACTICE ----------")
print("Accuracy:", round(accuracy, 2), "%")
print("Status:", practice_status)

print()
print("---------- MOCK TEST ----------")
print("Tests Attempted:", mock_tests)
print("Average Score:", round(mock_score, 2), "%")
print("Status:", mock_status)

print()
print("---------- REVISION ----------")
print("Completion:", round(revision_percentage, 2), "%")
print("Status:", revision_status)

print()
print("========================================")
print("Overall Readiness Score:", round(score, 2), "%")
print("Overall Status:", status)
print("========================================")

print()

if len(weak_areas) == 0:
    print("Areas Needing Improvement: None")
else:
    print("Areas Needing Improvement:")
    for area in weak_areas:
        print("-", area)

print("========================================")
print("       END OF READINESS REPORT")
print("========================================")