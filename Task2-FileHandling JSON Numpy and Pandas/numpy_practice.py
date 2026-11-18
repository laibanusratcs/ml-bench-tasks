
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])

arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("1D Array:", arr1)
print("2D Array:\n", arr2)

print("Dimensions:", arr2.ndim)
print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)

print("First Element:", arr1[0])
print("Slicing:", arr1[1:4])
print("2D Indexing:", arr2[1, 2])

a = np.array([10, 20, 30])
b = np.array([2, 4, 6])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Maximum:", np.max(arr1))
print("Minimum:", np.min(arr1))
print("Median:", np.median(arr1))
print("Standard Deviation:", np.std(arr1))

reshaped = arr1.reshape(2, 3)

print("Reshaped Array:\n", reshaped)
