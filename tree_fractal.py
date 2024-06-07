import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Function to draw the fractal tree
def draw_tree(ax, x, y, angle, length, depth, angle_diff, length_factor):
    if depth == 0 or length < 0.01:
        return
    x2 = x + length * np.cos(angle)
    y2 = y + length * np.sin(angle)
    ax.plot([x, x2], [y, y2], color='brown', lw=2 * depth / 10)
    
    draw_tree(ax, x2, y2, angle - angle_diff, length * length_factor, depth - 1, angle_diff, length_factor)
    draw_tree(ax, x2, y2, angle + angle_diff, length * length_factor, depth - 1, angle_diff, length_factor)

# Function to update the plot based on slider values
def update(val):
    angle_diff = angle_slider.val * np.pi / 180
    length_factor = length_slider.val
    depth = int(depth_slider.val)
    
    ax.cla()
    ax.set_xlim(-2, 2)
    ax.set_ylim(0, 2.5)
    ax.axis('off')
    
    draw_tree(ax, 0, 0, np.pi / 2, 1, depth, angle_diff, length_factor)
    fig.canvas.draw_idle()

# Create the plot
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
ax.set_xlim(-2, 2)
ax.set_ylim(0, 2.5)
ax.axis('off')

# Initial parameters
initial_angle = 30
initial_length_factor = 0.7
initial_depth = 10

# Draw the initial tree
draw_tree(ax, 0, 0, np.pi / 2, 1, initial_depth, initial_angle * np.pi / 180, initial_length_factor)

# Add sliders for angle, length factor, and depth
ax_angle = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_length = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_depth = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')

angle_slider = Slider(ax_angle, 'Angle', 0, 90, valinit=initial_angle)
length_slider = Slider(ax_length, 'Length Factor', 0.1, 0.9, valinit=initial_length_factor)
depth_slider = Slider(ax_depth, 'Depth', 1, 15, valinit=initial_depth, valstep=1)

# Register the update function with each slider
angle_slider.on_changed(update)
length_slider.on_changed(update)
depth_slider.on_changed(update)

# Display the plot
plt.show()
