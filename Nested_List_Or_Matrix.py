# 1. Create a nested list named 'grades' where each inner list represents a student.
#    Each student should have grades for Math, Science, and English.
grades = [
    [85, 90, 88],  # Student 1's grades: Math, Science, English
    [78, 82, 85],  # Student 2's grades: Math, Science, English
    [92, 89, 91]   # Student 3's grades: Math, Science, English
]

# 2. Print the grades of the second student.
print(grades[2])
# Access the second student (index 1), then print their grades.

# 3. Change the Math grade of the first student.
grades[0][0] = 90
# Modify the first grade in the first student's list.

# 4. Add a new student with grades.
grades.append([75,85,95])
# Add a new list to the 'grades' list to represent a new student's grades.

# 5. Print the updated list.
print(grades)