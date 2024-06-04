import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import FancyArrowPatch
from matplotlib.widgets import TextBox, Button

# Initial polar function
polar_function = "1 + 0.5 * np.sin(3 * theta)"

# Convert string function to a lambda function
def get_polar_function(func_str):
    return eval("lambda theta: " + func_str)

r_func = get_polar_function(polar_function)

# Set up the figure and axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, polar=True)
fig.suptitle("Particle Moving Along a Polar Curve", va='top')

# Initial theta values
theta = np.linspace(0, 2 * np.pi, 1000)
r = r_func(theta)

# Plot the polar curve
polar_curve, = ax.plot(theta, r, label='Polar Curve')

# Initial particle position
particle, = ax.plot([], [], 'ro')

# Line from center to particle
line, = ax.plot([], [], 'r-')

# Velocity vector (quiver)
quiver = ax.quiver([], [], [], [], scale=50, color='b')

# State for the animation
is_paused = False

# Update function for the animation
def update(frame):
    global r_func
    if is_paused:
        return polar_curve, particle, line, quiver
    
    t = frame / 100 * 2 * np.pi
    r = r_func(t)
    
    x = t
    y = r

    particle.set_data([x], [y])
    line.set_data([0, x], [0, y])
    
    # Velocity vector (tangent to the curve)
    dt = 0.01
    r_next = r_func(t + dt)
    dr_dt = (r_next - r) / dt
    dx_dt = 4 * (dr_dt * np.cos(t) - r * np.sin(t))
    dy_dt = 4 * (dr_dt * np.sin(t) + r * np.cos(t))
    
    quiver.set_offsets([x, y])
    quiver.set_UVC(dx_dt, dy_dt)

    return polar_curve, particle, line, quiver

# Animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), blit=True, interval=100)

# Save the animation as a GIF
# ani.save('polar_function.gif', writer='pillow', fps=60)

# Textbox for updating the polar function
def submit(text):
    global r_func, theta
    r_func = get_polar_function(text)
    new_r = r_func(theta)
    polar_curve.set_ydata(new_r)
    
    # Update the axis limits
    max_r = np.max(new_r)
    ax.set_ylim(0, max_r)
    
    update(0)

# Create TextBox widget
text_box_ax = plt.axes([0.05, 0.85, 0.25, 0.05])
text_box = TextBox(text_box_ax, 'r(θ): ', initial=polar_function)
text_box.on_submit(submit)

# Pause/Restart button functions
def toggle_animation(event):
    global is_paused
    if is_paused:
        ani.event_source.start()
    else:
        ani.event_source.stop()
    is_paused = not is_paused

# Create Pause/Restart button
button_ax = plt.axes([0.05, 0.75, 0.15, 0.05])
button = Button(button_ax, 'Pause/Restart')
button.on_clicked(toggle_animation)

plt.show()
