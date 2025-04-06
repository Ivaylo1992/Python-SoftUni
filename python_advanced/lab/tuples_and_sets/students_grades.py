students_grades = {}

exams_count = int(input())

for exam in range(exams_count):
    student, grade = input().split(' ')
    grade = float(grade)

    if not students_grades.get(student):
        students_grades[student] = (grade, )
    else:
        students_grades[student] += (grade, )

for student, grades in students_grades.items():
    result = []
    list_grades = list(grades)
    avg_grade = sum([grade for grade in grades]) / len(list_grades)

    result.append(f"{student} ->")

    for grade in grades:
        result.append(f'{grade:.2f}')

    result.append(f"(avg: {avg_grade:.2f})")

    print(' '.join(result))