import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the function r(θ) = sin(4θ) + 1.5
def r(theta):
    return np.sin(8 * theta) + 1.5

# Generate theta values from 0 to 2π
theta = np.linspace(0, 2 * np.pi, 1000)

# Create a colormap with distinct colors for each petal
cmap = plt.cm.hsv  # 'hsv' colormap

# Create a figure and a polar subplot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Function to draw and fill the polar plot with different colors
def draw_colored_petals(ax, theta, r_values, frame):
    for i in range(8):  # 8 petals for sin(4θ)
        # Define the start and end for each petal segment
        start = i * (np.pi / 4)
        end = (i + 1) * (np.pi / 4)
        # Create a mask for the current petal
        mask = (theta >= start) & (theta < end)
        # Plot the filled area for the current petal with a shifted theta
        ax.fill_between(theta[mask] + frame, 0, r_values[mask], color=cmap(i / 8), alpha=0.7)

# Function to update the plot for animation
def update(frame):
    ax.clear()
    ax.set_ylim(0, 3)
    ax.set_xticks([])  # Remove angular ticks for a cleaner look
    ax.set_yticks([])  # Remove radial ticks for a cleaner look
    draw_colored_petals(ax, theta, r(theta), frame)

# Create an animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 360), interval=50)

ani.save('rotating_petals1.mp4', writer='ffmpeg', fps=60)
# Show the plot
plt.show()
