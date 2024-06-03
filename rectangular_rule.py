import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # Define the function to integrate
    return np.exp(-x)*np.sin(x)

def rectangular_integration(f, a, b, n):
    # Calculate the width of each rectangle
    dx = (b - a) / n
    # Calculate the midpoints
    midpoints = np.linspace(a + dx/2, b - dx/2, n)
    y = f(midpoints)
    # Sum up the areas of the rectangles
    integral = np.sum(y * dx)
    return integral, midpoints, dx

# Define the interval [a, b]
a = 0
b = np.pi

# Define the number of rectangles
n = 10

# Calculate the integral
integral, midpoints, dx = rectangular_integration(f, a, b, n)
print(f"The integral of the function from {a} to {b} is approximately {integral:.6f}")

# Plot the function
x = np.linspace(a, b, 1000)
y = f(x)

plt.plot(x, y, label="f(x) = sin(x)")
plt.fill_between(x, y, alpha=0.2)

# Plot the partitions and rectangles
for midpoint in midpoints:
    plt.plot([midpoint - dx/2, midpoint + dx/2], [f(midpoint), f(midpoint)], 'g')
    plt.plot([midpoint - dx/2, midpoint - dx/2], [0, f(midpoint)], 'g--')
    plt.plot([midpoint + dx/2, midpoint + dx/2], [0, f(midpoint)], 'g--')

plt.title("Function f(x) = sin(x) and its Integral with Partitions (Rectangular Rule)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

# Display the result of the integration on the plot
plt.text(0.5 * (a + b), max(y)*0.5, f"Integral ≈ {integral:.6f}", horizontalalignment='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.show()
