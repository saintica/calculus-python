import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # Define the function to integrate
    return np.sin(x)

def trapezoidal_integration(f, a, b, n):
    # Calculate the width of each trapezoid
    dx = (b - a) / n
    # Calculate the x values where the function will be evaluated
    x = np.linspace(a, b, n + 1)
    # Calculate the y values of the function at the x values
    y = f(x)
    # Sum up the areas of the trapezoids
    integral = (dx / 2) * np.sum(y[:-1] + y[1:])
    return integral

# Define the interval [a, b]
a = 0
b = np.pi

# Define the number of trapezoids
n = 100

# Calculate the integral
integral = trapezoidal_integration(f, a, b, n)
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
