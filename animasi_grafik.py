import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image

# Set up the figure, axis, and plot element
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 1000)
line, = ax.plot(x, np.sin(x))

# Setting the limits of x and y axes
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)

# Number of frames and interval
num_frames = 100  # 20 frames per second for a 5-second animation
interval = 50  # Time between frames in milliseconds

# Function to update the frame
def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))  # Shift the sine wave
    return line,

# Creating the animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, blit=True, interval=interval, repeat=False
)

# Save the animation as a GIF
ani.save('sine_wave_animation.gif', writer='pillow', fps=20)

plt.show()
