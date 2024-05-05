import numpy as np

def cols(arr):
    n, m = arr.shape
    for i in range(m):
        total = 0
        for j in range(n):
            total += arr[j][i]
        print(total, end=" ")

A2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
A2D = np.array(A2D)

print("Mảng 2 chiều:")
print(A2D)
print("\nTổng các cột:")
cols(A2D)