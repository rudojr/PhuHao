import matplotlib.pyplot as plt

# Tạo dữ liệu cho đồ thị
x = range(-10, 11)
y = [2*i**2 - 3*i + 1 for i in x]

# Vẽ đồ thị
plt.plot(x, y)

# Đặt tiêu đề và nhãn trục
plt.title('Đồ thị hàm y = 2x^2 - 3x + 1')
plt.xlabel('Trục X')
plt.ylabel('Trục Y')

# Đặt giới hạn cho trục X và Y
plt.xlim(-10, 10)
plt.ylim(-20, 100)

# Hiển thị đồ thị
plt.grid(True)
plt.show()