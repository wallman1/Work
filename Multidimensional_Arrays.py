import numpy as np  # Import NumPy library

# 1. Create a 2D NumPy array named 'matrix' with 3 rows and 3 columns of numbers.
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# 2. Print the entire second row.
print(matrix[0])
# The second row is at index 1 (remember, indexing starts at 0).
# Output will be [4, 5, 6]

# 3. Change the value in the first row, second column.
matrix[0,1] = 13
# The first row is at index 0, second column is at index 1.


# 4. Add a new row to the matrix.
x = np.array([10,11,12])
matrix = np.append(matrix,[x],axis=0)
# Use np.append to add a row to the existing matrix.
# use this code: new_row = np.array([10, 11, 12])
# use this code: matrix = np.append(matrix, [new_row], axis=0)

# 5. Print the updated matrix.
print(matrix)