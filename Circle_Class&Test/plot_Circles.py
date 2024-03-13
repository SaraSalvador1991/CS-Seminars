import matplotlib.pyplot as plt
import numpy as np

# First Circle
r1 = 1  # radius of first circle
center1 = (0, 0)  # center of first circle

# Second circle
r2 = 2  # radius of second circle
center2 = (2, -1)  # center of second circle

# parametric points of the first circle
theta1 = np.linspace(0, 2*np.pi, 100)
x1 = center1[0] + r1 * np.cos(theta1)
y1 = center1[1] + r1 * np.sin(theta1)

# parametric points of the second circle
theta2 = np.linspace(0, 2*np.pi, 100)
x2 = center2[0] + r2 * np.cos(theta2)
y2 = center2[1] + r2 * np.sin(theta2)

# Plot
plt.figure(figsize=(6, 6))
plt.plot(x1, y1, label='Circle 1')
plt.plot(x2, y2, label='circle 2')
plt.axis('equal')  # axis
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plot of the two circles')
plt.legend()
plt.grid(True)
plt.show()
