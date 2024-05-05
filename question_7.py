import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y1 = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

x2 = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y2 = np.array([100, 105, 84, 105, 98, 99, 90, 95, 94, 108, 79, 112, 91, 80, 85])

plt.scatter(x1, y1, color='red')
plt.scatter(x2, y2, color='blue')

# Sort data points based on y values
sorted_y1_indices = np.argsort(y1)
sorted_y2_indices = np.argsort(y2)

# Bold the top 4 data points for each dataset
top_4_indices_data1 = sorted_y1_indices[-4:]
top_4_indices_data2 = sorted_y2_indices[-4:]

plt.scatter(x1[top_4_indices_data1], y1[top_4_indices_data1], color='red', s=100, label='(4 brightness level): Dữ liệu 1')
plt.scatter(x2[top_4_indices_data2], y2[top_4_indices_data2], color='blue', s=100, label='(4 brightness level): Dữ liệu 2')

plt.xlabel('Tọa độ X')
plt.ylabel('Tọa độ Y')
plt.legend()
plt.grid(True)
plt.show()