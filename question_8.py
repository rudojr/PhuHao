import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = np.sin(3*x)/x
y2 = np.sin(2*x)/x
y3= np.sin(x)/x

plt.plot(x, y, label='y = sin(3x)/x')
plt.plot(x, y2, label='y2 = sin(2x)/x')
plt.plot(x, y3, label='y3 = sin(x)/x')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Đồ thị của y, y2 và y3')
plt.legend()
plt.axhline(0, color='black', linewidth=1.5)
plt.axvline(0, color='black', linewidth=1.5)
plt.grid(False)
plt.xticks([-2*np.pi,-np.pi,  0,  np.pi, 2*np.pi],
           [r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$'])
plt.show()