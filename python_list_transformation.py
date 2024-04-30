#Task 1 Sort the list of grades in descending order and display the list.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse = True)
print(f'This is my sorted list: {grades}')

#Task 2 Calculate the average grade and display it.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
total = sum(grades)
average = total / len(grades)
print(f'This is my average: {average}')

#Task 3 Replace and grades below 80 with the value "Failed."
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "Failed. "
print(f'This is my replaced list: {grades}')
