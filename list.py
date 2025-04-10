# 1. Create a list named 'students' with at least 4 student names.
students = ['Alice', 'Bob', 'Charlie', 'Diana']

# 2. Print the first and last student's name using indexing.
# Remember that the first item has an index of 0.
print(students[0])
print(students[3])

# 3. Add a new student to the end of the list.
# Use append() to add a new name to the list.
students.append('ohio')

# 4. Remove the second student from the list.
# Use pop()to delete an element by index.
students.pop(2)

# 5. Print the updated list.
print(students)

















import array  # Import the array module

# 1. Create an array named 'scores' that stores five test scores (integers).
scores = array.array('i', [85, 90, 88, 92, 87])

# 2. Print the third score in the array.
# Arrays use indexing just like lists.
print(scores[2])

# 3. Change the second score to a new value.
# Modify an element by accessing it through its index.
scores[2] = 12


# 4. Add a new score to the array.
# Use append() to add a new element.
scores.append(123)

# 5. Print the updated array.
# Should show: array('i', [85, 95, 88, 92, 87, 93])
print(scores)















# 1. Create a nested list named 'grades' where each inner list represents a student.
#    Each student should have grades for Math, Science, and English.
grades = [
    [85, 90, 88],  # Student 1's grades: Math, Science, English
    [78, 82, 85],  # Student 2's grades: Math, Science, English
    [92, 89, 91]   # Student 3's grades: Math, Science, English
]

# 2. Print the grades of the second student.
# Access the second student (index 1), then print their grades.
print(grades[0][1])

# 3. Change the Math grade of the first student.
# Modify the first grade in the first student's list.
grades[[0][0]] = 1

# 4. Add a new student with grades.
# Add a new list to the 'grades' list to represent a new student's grades.
grades.append([123,123,123])

# 5. Print the updated list
print(grades)













