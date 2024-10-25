import numpy as np

# Sample 2D array
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Step 1: Sum each row (keeping it as a 2D array so we can broadcast)
row_sums = array.sum(axis=1, keepdims=True)

# Step 2: Divide each element by its row's sum
normalized_array = array / row_sums

print("Original Array:\n", array)
print("Row-wise Normalized Array:\n", normalized_array)
