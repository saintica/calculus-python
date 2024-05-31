import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the function and its derivative
def f(x):
    return np.sin(x)

def df(x):
    return np.cos(x)

# Generate x values
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y = f(x)

# Set up the figure, axis, and plot elements
fig, ax = plt.subplots()
ax.set_xlim((x[0], x[-1]))
ax.set_ylim((-1.5, 1.5))
line, = ax.plot(x, y, lw=2)
point, = ax.plot([], [], 'ro')
tangent_line, = ax.plot([], [], 'r--', lw=2)

# Initialization function: plot the background of each frame
def init():
    point.set_data([], [])
    tangent_line.set_data([], [])
    return point, tangent_line

# Animation function: this is called sequentially
def animate(i):
    # Get the current x value and the corresponding y value
    x0 = x[i]
    y0 = f(x0)
    
    # Set the point location
    point.set_data([x0], [y0])
    
    # Calculate the slope (derivative) at x0
    slope = df(x0)
    
    # Create the tangent line
    tangent_x = np.array([x0 - 1, x0 + 1])
    tangent_y = y0 + slope * (tangent_x - x0)
    
    # Set the tangent line data
    tangent_line.set_data(tangent_x, tangent_y)
    
    return point, tangent_line

# Create animation
ani = FuncAnimation(fig, animate, init_func=init, frames=len(x), interval=25, blit=True)

ani.save(filename="Konsep Turunan.gif", writer='pillow', fps=60)

# Show plot
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Visualisasi Konsep Turunan')
plt.show()
