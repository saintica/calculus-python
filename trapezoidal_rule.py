import numpy as np
import matplotlib.pyplot as plt

def f(x):
    # Define the function to integrate
    return np.exp(-x)*np.sin(x)

def trapezoidal_integration(f, a, b, n):
    # Calculate the width of each trapezoid
    dx = (b - a) / n
    # Calculate the x values where the function will be evaluated
    x = np.linspace(a, b, n + 1)
    # Calculate the y values of the function at the x values
    y = f(x)
    # Sum up the areas of the trapezoids
    integral = (dx / 2) * np.sum(y[:-1] + y[1:])
    return integral, x, y

# Define the interval [a, b]
a = 0
b = np.pi

# Define the number of trapezoids
n = 10

# Calculate the integral
integral, x_partitions, y_partitions = trapezoidal_integration(f, a, b, n)
print(f"The integral of the function from {a} to {b} is approximately {integral:.6f}")

# Plot the function
x = np.linspace(a, b, 1000)
y = f(x)

plt.plot(x, y, label="f(x) = sin(x)")
plt.fill_between(x, y, alpha=0.2)

# Plot the partitions
for i in range(n + 1):
    plt.plot([x_partitions[i], x_partitions[i]], [0, y_partitions[i]], 'g--')

# Plot the trapezoids
for i in range(n):
    plt.plot([x_partitions[i], x_partitions[i+1]], [y_partitions[i], y_partitions[i+1]], 'g')

plt.title("Function f(x) = sin(x) and its Integral with Partitions (Trapezoidal Rule)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

# Display the result of the integration on the plot
plt.text(0.5 * (a + b), max(y)*0.5, f"Integral ≈ {integral:.6f}", horizontalalignment='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.show()
