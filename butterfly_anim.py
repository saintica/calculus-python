import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the butterfly function in polar coordinates
def butterfly(theta):
    return np.exp(np.sin(theta)) - 2 * np.cos(4 * theta) + np.sin((2 * theta - np.pi) / 24)**5

# Set up the figure and axis for polar plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
theta = np.linspace(0, 2 * np.pi, 1000)
r = butterfly(theta)

# Initialize the butterfly curve
line, = ax.plot(theta, r, color='purple', linewidth=2)

# Initialize a point on the butterfly curve
point, = ax.plot([], [], 'ro')

# Add a title with LaTeX formatting
ax.set_title(r"$r = e^{\sin(\theta)} - 2 \cos(4 \theta) + \sin\left(\frac{2 \theta - \pi}{24}\right)^5$", va='bottom', fontsize=14)

# Number of frames and intervals
num_frames = 200  # Number of frames in the animation
interval = 50  # Time between frames in milliseconds

# Create a colormap
cmap = plt.get_cmap('hsv', num_frames)

# Update function for the animation
def update(frame):
    # Update point position
    point_theta = 2 * np.pi * frame / num_frames
    point_r = butterfly(point_theta)
    point.set_data([point_theta], [point_r])
    
    # Update the butterfly curve color
    color = cmap(frame / num_frames)
    line.set_color(color)
    return line, point

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, blit=True, interval=interval, repeat=True
)

ani.save('kupu-kupu.mp4', writer="ffmpeg", fps=60)

# Display the plot
plt.show()
