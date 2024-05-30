import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image

# Define the function f(x)
def f(x):
    return x**3 - 7.254*x + 0.5

# Define the derivative of f(x)
def f_prime(x):
    return 3*x**2 - 7.254

# Newton-Raphson method implementation
def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
    x = x0
    roots = [x]
    tangent_lines = []
    for i in range(max_iter):
        x_new = x - f(x) / f_prime(x)
        roots.append(x_new)
        if abs(x_new - x) < tol:
            return roots, tangent_lines, i+1
        tangent_lines.append((x, f(x), x_new))
        x = x_new
    return roots, tangent_lines, max_iter

# Initial guess
x0 = -1.0

# Find the roots using Newton-Raphson method
roots, tangent_lines, iterations = newton_raphson(f, f_prime, x0)
root = roots[-1]

print(f"Root found at x = {root} after {iterations} iterations.")

# Visualization
fig, ax = plt.subplots()
x_values = np.linspace(-2, 4, 400)  # Move x_values definition outside of update function
ax.plot(x_values, f(x_values), label='f(x)')
root_line, = ax.plot([], [], 'ro', label='Root')
iter_point, = ax.plot([], [], 'bo', label='Iteration Point')
lines = []

# Fix x and y limits
ax.set_xlim(-2, 4)
ax.set_ylim(-10, 10)

def update(frame):
    ax.clear()
    ax.plot(x_values, f(x_values), label='f(x)')
    iter_point.set_data(roots[:frame], f(np.array(roots[:frame])))
    if frame > 0:
        for i in range(frame):
            if i == 0:
                continue
            x_values_iter = np.linspace(tangent_lines[i-1][0] - 1, tangent_lines[i-1][2] + 1, 100)
            y_values = f_prime(tangent_lines[i-1][0]) * (x_values_iter - tangent_lines[i-1][0]) + f(tangent_lines[i-1][0])
            ax.plot(x_values_iter, y_values, 'g--')
            ax.plot(roots[i-1], f(roots[i-1]), 'bo')

    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Newton-Raphson Method')
    ax.legend()
    ax.grid(True)

    # Stop animation when root is found and display root value
    """if root is not None:
        ax.text(root, f(root), f'Root: {root:.4f}', fontsize=12, ha='center')
        ani.event_source.stop()"""

# Create animation
ani = FuncAnimation(fig, update, frames=len(roots), interval=1000)

# Save animation as GIF
ani.save('newton_raphson_animation.gif', writer='pillow', fps=30)

plt.show()
