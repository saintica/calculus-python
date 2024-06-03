import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # Define the function to integrate
    return np.sin(x)

def rectangular_integration(f, a, b, n):
    # Calculate the width of each rectangle
    dx = (b - a) / n
    # Calculate the midpoints
    midpoints = np.linspace(a + dx/2, b - dx/2, n)
    # Sum up the areas of the rectangles
    integral = np.sum(f(midpoints) * dx)
    return integral

# Define the interval [a, b]
a = 0
b = np.pi

# Define the number of rectangles
n = 100

# Calculate the integral
integral = rectangular_integration(f, a, b, n)
print(f"The integral of the function from {a} to {b} is approximately {integral:.6f}")

# Plot the function
x = np.linspace(a, b, 1000)
y = f(x)

plt.plot(x, y, label="f(x) = sin(x)")
plt.fill_between(x, y, alpha=0.2)
plt.title("Function f(x) = sin(x) and its Integral")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

# Display the result of the integration on the plot
plt.text(0.5 * (a + b), 0.5, f"Integral ≈ {integral:.6f}", horizontalalignment='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.show()
