import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle
from PIL import Image

# Define the butterfly function in polar coordinates
def butterfly(theta):
    return np.exp(np.sin(theta)) - 2 * np.cos(4 * theta) + np.sin((2 * theta - np.pi) / 24)**5

# Set up the figure and axis for polar plot
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
theta = np.linspace(0, 2 * np.pi, 1000)
r = butterfly(theta)
ax.plot(theta, r, color='blue')

# Initialize a point on the butterfly curve
point, = ax.plot([], [], 'ro')

# Number of frames and intervals
num_frames = 200  # Number of frames in the animation
interval = 50  # Time between frames in milliseconds

# Update function for the animation
def update(frame):
    point_theta = 2 * np.pi * frame / num_frames
    point_r = butterfly(point_theta)
    point.set_data(point_theta, point_r)
    return point,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, blit=True, interval=interval, repeat=True
)

# Save the animation as a GIF
ani.save('butterfly_animation.gif', writer='pillow', fps=20)

plt.show()
