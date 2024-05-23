import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image

# Define the function to be integrated
def f(x):
    return np.sin(x)

# Set up the figure, axis, and plot element
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 1000)
ax.plot(x, f(x), 'r', linewidth=2)
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(0, 1.1)

# Number of frames and intervals
num_frames = 100  # Number of frames in the animation
interval = 100  # Time between frames in milliseconds

# Initialize a bar container for rectangles
bar_container = ax.bar([], [], width=0, align='edge', color='blue', edgecolor='black')

# Update function for the animation
def update(frame):
    ax.clear()
    ax.plot(x, f(x), 'r', linewidth=2)
    n = frame + 1  # Number of rectangles
    width = (2 * np.pi) / n
    x_rectangles = np.linspace(0, 2 * np.pi - width, n)
    heights = f(x_rectangles + width / 2)
    bars = ax.bar(x_rectangles, heights, width=width, align='edge', color='blue', edgecolor='black')
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(0, 1.1)
    ax.set_title(f'Riemann Sum Approximation with {n} Rectangles')
    return bars

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, blit=False, interval=interval, repeat=False
)

# Save the animation as a GIF
ani.save('riemann_sum_animation.gif', writer='pillow', fps=10)

plt.show()
