students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(students):
    row = []
    print("\nStudent", i + 1)

    for j in range(subjects):
        mark = float(input("Enter mark: "))

        while mark < 0 or mark > 100:
            print("Enter marks between 0 and 100")
            mark = float(input("Enter mark again: "))

        row.append(mark)

    marks.append(row)

print("\nStudent-wise averages:")

for i in range(students):
    average = sum(marks[i]) / subjects
    print("Student", i + 1, ":", round(average, 2))

print("\nSubject-wise averages:")

for j in range(subjects):
    total = 0

    for i in range(students):
        total += marks[i][j]

    average = total / students
    print("Subject", j + 1, ":", round(average, 2))

top_student = 0
highest_average = sum(marks[0]) / subjects

for i in range(1, students):
    average = sum(marks[i]) / subjects

    if average > highest_average:
        highest_average = average
        top_student = i

print("\nTop performer: Student", top_student + 1)
print("Highest average:", round(highest_average, 2))