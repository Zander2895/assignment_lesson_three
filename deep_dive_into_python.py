#Task 1 Filter out students who have grades below 80. Print the name, grade, and activity. Expected Outcome "Jane", 78, "Art"
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

for i in range(len(students)):
    if grades[i] <= 80:
        print(f"This is my filtered out list: {students[i]}, {grades [i]}, {activities [i]}")

#Task 2 For the remaining students, add students name in a new list named students_approved. Expected outcome: students_approved = ["John", "Doe", "Smith"]
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

for i in range(len(students)):
    if grades[i] >= 80:
        print(f"students_approved = {students[i]}")

#Task 3 Print the list students_approved
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
