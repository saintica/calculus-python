import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image

# Define the function and its derivative
def f(x):
    return np.sin(x)

def df(x):
    return np.cos(x)

# Set up the figure, axis, and plot element
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 1000)
ax.plot(x, f(x), 'r', linewidth=2)
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)

# Number of frames and intervals
num_frames = 200  # Number of frames in the animation
interval = 50  # Time between frames in milliseconds

# Initialize a line for the tangent
tangent_line, = ax.plot([], [], 'b', linewidth=2)

# Update function for the animation
def update(frame):
    ax.clear()
    ax.plot(x, f(x), 'r', linewidth=2)
    point_x = 2 * np.pi * frame / num_frames
    point_y = f(point_x)
    slope = df(point_x)
    tangent_x = np.linspace(point_x - 1, point_x + 1, 100)
    tangent_y = slope * (tangent_x - point_x) + point_y
    ax.plot(x, f(x), 'r', linewidth=2)
    ax.plot(tangent_x, tangent_y, 'b', linewidth=2)
    ax.plot(point_x, point_y, 'go')  # Mark the point of tangency
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1.5, 1.5)
    ax.set_title(f'Tangent Line at x = {point_x:.2f}')
    return tangent_line,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, blit=False, interval=interval, repeat=False
)

# Save the animation as a GIF
ani.save('tangent_line_animation.gif', writer='pillow', fps=20)

plt.show()
