import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x, y, z, w)
def f(x, y, z, w):
    term1 = abs(np.cos(z * y))
    term2 = 0.25 - abs(np.cos(z * y + np.pi / 2))
    term3 = abs(np.cos(z * x + np.pi / 2)) * 8
    return w + ((term1 + term2) * 2) / (2 + term3)

# Define the curves parameters
curves_params = [
    (6, 3, 1, 'a1', 1),
    (6, 3, 2, 'a2', 2),
    (12, 6, 3, 'a3', 3),
    (12, 6, 4, 'a4', 4),
]

# Generate theta values
theta = np.linspace(0, 2 * np.pi, 1000)

# Set up the plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(10, 10))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Plot each curve with the specified color
for x, y, w, label, k in curves_params:
    r = f(x, y, theta, w)
    color = (0.8, 0.15, k / 4, 1 - 0.6 * k / 4)  # RGBA
    ax.plot(theta, r, label=label, color=color)

# Set plot properties
ax.grid(False)
ax.set_xticklabels([])
ax.set_yticklabels([])

# Display the plot
plt.show()
