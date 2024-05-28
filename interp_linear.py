import matplotlib.pyplot as plt

# Known points
x1, y1 = 1, 2
x2, y2 = 3, 3

# Point to estimate
x = 2

# Calculate the estimated y value
y = y1 + (x - x1) / (x2 - x1) * (y2 - y1)

# Plotting
plt.plot([x1, x2], [y1, y2], 'ro-', label='Known points')
plt.plot(x, y, 'bo', label='Interpolated point')
plt.text(x, y, f'  ({x}, {y:.1f})', ha='left')

# Annotate the known points
plt.text(x1, y1, f'  ({x1}, {y1})', ha='left')
plt.text(x2, y2, f'  ({x2}, {y2})', ha='left')

# Set up the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Interpolation')
plt.legend()
plt.grid(True)
plt.show()
