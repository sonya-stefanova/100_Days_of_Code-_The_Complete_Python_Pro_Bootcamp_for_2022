student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
# This is the scoring criteria:
# > Scores 91 - 100: Grade = "Outstanding"
# > Scores 81 - 90: Grade = "Exceeds Expectations"
# > Scores 71 - 80: Grade = "Acceptable"
# > Scores 70 or lower: Grade = "Fail"
# # Expected Output
# ```
# '{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
# ```
grade = ""
for current_name in student_scores:
    current_score = student_scores[current_name]
    if current_score>=91:
        grade = "Outstanding"
    elif current_score>=81:
        grade = "Exceeds Expectations"
    elif current_score>=71:
        grade = "Acceptable"
    elif current_score<71:
        grade = "Fail"

    student_grades[current_name] = grade

# 🚨 Don't change the code below 👇
print(student_grades)



