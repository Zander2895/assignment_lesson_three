#Task 1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

#Task 2
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
total = sum(grades)
average = total / len(grades)
print(average)

#Task 3
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades[2] = "Failed"
grades[4] = "Failed"
grades[8] = "Failed"
print(grades)