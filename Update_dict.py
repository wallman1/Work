# 1. Create a dictionary with keys: 'Name', 'Age', and 'Subject'.
students = {
    "Name":"Alice",
    "Age":16,
    "Subject":"Math"
}

# 2. Update the student's age to 18.
students["Age"] = 18

# 3. Add a new key-value pair for 'Grade' with a value of 'A'.
students.update({"Grade": "A"})

# 4. Print the updated dictionary.
print(students)