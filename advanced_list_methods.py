#Task 1 Find out wich students both submitted their assignments and attended the class 
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

completed_both = []
for student in submitted:
    if student not in attended:
        completed_both.append(student)
print(f'This is my matching list: {completed_both}')

#Task 2 Check if the two lists are identical in terms of their content, regardless of order.


#Task 3 using list methods, remove any student for the attended list who did not sumit their assignment.