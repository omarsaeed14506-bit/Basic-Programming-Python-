students = {
"Ahmed": [70, 80, 90],
"Sara": [95, 88, 92],
"Omar": [40, 55, 45],
"Mona": [60, 75, 70]
}
passed_students = []
failed_students = []
for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 50:
        passed_students.append(name)
        print(f"{name} has passed with an average grade of {average_grade}.")
    else:
        failed_students.append(name)
        print(f"{name} has failed with an average grade of {average_grade}.")
print("Passed students:", passed_students)
print("Failed students:", failed_students)