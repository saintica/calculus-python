import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the function to be integrated
def f(x):
    return np.exp(-x/2) * np.sin(2 * x)

# Set up the figure, axis, and plot element
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 1000)
ax.plot(x, f(x), 'r', linewidth=2)
ax.set_xlim(0, 2 * np.pi)
# ax.set_ylim(0, 1.1)

# Number of frames and intervals
num_frames = 1000  # Number of frames in the animation
interval = 100  # Time between frames in milliseconds

# Update function for the animation
def update(frame):
    ax.clear()
    ax.plot(x, f(x), 'r', linewidth=2)
    n = frame + 1  # Number of rectangles
    width = (2 * np.pi) / n
    x_rectangles = np.linspace(0, 2 * np.pi - width, n)
    heights = f(x_rectangles + width / 2)
    bars = ax.bar(x_rectangles, heights, width=width, align='edge', color='blue', edgecolor='black')
    riemann_sum = np.sum(heights * width)
    ax.set_xlim(0, 2 * np.pi)
    # ax.set_ylim(0, 1.1)
    ax.set_title(f'Jumlah Reimann dengan {n} Bilah')
    ax.text(0.5, 0.95, f'Luas = {riemann_sum:.4f}', transform=ax.transAxes, ha='center', va='top', fontsize=12, bbox=dict(facecolor='white', alpha=0.6))
    return bars

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, blit=False, interval=interval, repeat=False
)

# Save the animation as a GIF
#ani.save('riemann_sum_animation.mp4', writer='ffmpeg', fps=30)

plt.show()
