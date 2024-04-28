#Task 1 Sort the list of grades in descending order and display the list.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

#Task 2 Calculate the average grade and display it.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
total = sum(grades)
average = total / len(grades)
print(average)

#Task 3 Replace and grades below 80 with the value "Failed."
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades[2] = "Failed"
grades[4] = "Failed"
grades[8] = "Failed"
print(grades)