n = int(input("Enter number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")
    marks = []

    for j in range(3):
        mark = float(input("Enter exam mark: "))

        while mark < 0 or mark > 100:
            print("Marks must be between 0 and 100")
            mark = float(input("Enter mark again: "))

        marks.append(mark)

    improvement = marks[2] - marks[0]
    average = sum(marks) / 3

    print("\nStudent:", name)
    print("Exam marks:", marks)
    print("Average:", round(average, 2))
    print("Change from first to last exam:", improvement)

    if average >= 75:
        print("Classification: Excellent")
    elif average >= 50:
        print("Classification: Average")
    else:
        print("Classification: Needs Improvement")

    if improvement > 0:
        print("Performance trend: Improving")
    elif improvement < 0:
        print("Performance trend: Declining")
    else:
        print("Performance trend: Stable")