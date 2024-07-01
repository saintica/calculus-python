import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import TextBox

# Global variables for function and animation
current_function = "1 - 2 * np.sin(2 * theta)"  # Initial polar function

# Function to evaluate polar function
def evaluate_polar_function(theta):
    try:
        r = eval(current_function)
        return r
    except Exception as e:
        print(f"Error evaluating function: {e}")
        return np.zeros_like(theta)

# Derivative of the polar function
def polar_function_derivative(theta):
    return -4 * np.cos(2 * theta)

# Define the tangent line function in polar coordinates
def tangent_line(theta, r, r_derivative):
    # Parametric representation of the tangent line
    t = np.linspace(-0.5, 0.5, 100)  # small interval around the point
    theta_tangent = theta + t
    r_tangent = r + r_derivative * t
    x_tangent = r_tangent * np.cos(theta_tangent)
    y_tangent = r_tangent * np.sin(theta_tangent)
    return x_tangent, y_tangent

# Set up the figure and axis
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_ylim(-3, 3)

# Compute the full polar function for plotting
theta_full = np.linspace(0, 2 * np.pi, 1000)
r_full = evaluate_polar_function(theta_full)

# Plot the full polar function
line_polar, = ax.plot(theta_full, r_full, 'b-', lw=1)  # Full polar function plot

# Initialize the line and point to be animated
line, = ax.plot([], [], 'r-', lw=2)  # Tangent line
point, = ax.plot([], [], 'bo')       # Point on the curve

# Initialization function
def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

# Animation function
def animate(theta):
    r = evaluate_polar_function(theta)
    r_derivative = polar_function_derivative(theta)
    
    # Compute the tangent line in Cartesian coordinates
    x_tangent, y_tangent = tangent_line(theta, r, r_derivative)
    
    # Set the data for the line and point
    line.set_data(x_tangent, y_tangent)
    point.set_data([r * np.cos(theta)], [r * np.sin(theta)])
    
    return line, point

# Create the animation
theta_values = np.linspace(0, 2*np.pi, 200)
ani = FuncAnimation(fig, animate, frames=theta_values, init_func=init, blit=True, interval=50)

# Function for updating the polar function
def update_function(text):
    global current_function
    current_function = text
    try:
        r_new = evaluate_polar_function(theta_full)
        line_polar.set_ydata(r_new)
    except Exception as e:
        print(f"Error updating function: {e}")
    
    fig.canvas.draw_idle()

# Add a textbox for user input
axbox = plt.axes([0.2, 0.05, 0.7, 0.075])
text_box = TextBox(axbox, 'Enter Polar Function:', initial=current_function)
text_box.on_submit(update_function)

# Show the plot
plt.show()
