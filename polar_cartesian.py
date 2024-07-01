import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Slider
import numpy as np

# Initialize the figure and axis
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)

# Plot settings for Cartesian coordinates
ax[0].set_xlim(-10, 10)
ax[0].set_ylim(-10, 10)
ax[0].set_title('Cartesian Coordinates')
ax[0].grid(True)
cartesian_point, = ax[0].plot([], [], 'bo')
cartesian_line, = ax[0].plot([], [], 'b--')
cartesian_label = ax[0].text(0, 0, '', fontsize=12)

# Plot settings for Polar coordinates
ax[1] = plt.subplot(122, projection='polar')
ax[1].set_ylim(0, 10)
ax[1].set_title('Polar Coordinates')
polar_point, = ax[1].plot([], [], 'bo')
polar_line, = ax[1].plot([], [], 'b--')
polar_label = ax[1].text(0, 0, 'A', fontsize=12)

# Initial coordinates
x_init, y_init = 5, 5
r_init, theta_init = np.sqrt(x_init**2 + y_init**2), np.arctan2(y_init, x_init)
cartesian_point.set_data([x_init], [y_init])
cartesian_line.set_data([0, x_init], [0, y_init])
cartesian_label.set_position((x_init, y_init))
cartesian_label.set_text(f'A ({x_init:.2f}, {y_init:.2f})')
polar_point.set_data([theta_init], [r_init])
polar_line.set_data([0, theta_init], [0, r_init])
polar_label.set_position((theta_init, r_init))

# Flag to prevent recursive updates
updating = False

# Function to update the coordinates
def update_cartesian(val):
    global updating
    if updating:
        return

    try:
        x = float(text_box_x.text)
        y = float(text_box_y.text)
    except ValueError:
        return

    updating = True

    # Update Cartesian coordinates
    cartesian_point.set_data([x], [y])
    cartesian_line.set_data([0, x], [0, y])
    cartesian_label.set_position((x, y))
    cartesian_label.set_text(f'A ({x:.2f}, {y:.2f})')

    # Adjust Cartesian limits if necessary
    current_xlim = ax[0].get_xlim()
    current_ylim = ax[0].get_ylim()
    if x < current_xlim[0] or x > current_xlim[1] or y < current_ylim[0] or y > current_ylim[1]:
        ax[0].set_xlim(min(current_xlim[0], x-1), max(current_xlim[1], x+1))
        ax[0].set_ylim(min(current_ylim[0], y-1), max(current_ylim[1], y+1))
    ax[0].figure.canvas.draw_idle()

    # Convert to polar and update
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    polar_point.set_data([theta], [r])
    polar_line.set_data([0, theta], [0, r])
    polar_label.set_position((theta, r))
    text_box_r.set_val(f'{r:.2f}')
    theta_slider.set_val(theta)
    ax[1].set_ylim(0, r + 1)
    ax[1].figure.canvas.draw_idle()

    updating = False

def update_polar(val):
    global updating
    if updating:
        return

    try:
        r = float(text_box_r.text)
    except ValueError:
        return

    theta = theta_slider.val

    updating = True

    # Update polar coordinates
    polar_point.set_data([theta], [r])
    polar_line.set_data([0, theta], [0, r])
    polar_label.set_position((theta, r))

    # Convert to Cartesian and update
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    cartesian_point.set_data([x], [y])
    cartesian_line.set_data([0, x], [0, y])
    cartesian_label.set_position((x, y))
    cartesian_label.set_text(f'A ({x:.2f}, {y:.2f})')
    text_box_x.set_val(f'{x:.2f}')
    text_box_y.set_val(f'{y:.2f}')

    # Adjust Cartesian limits if necessary
    current_xlim = ax[0].get_xlim()
    current_ylim = ax[0].get_ylim()
    if x < current_xlim[0] or x > current_xlim[1] or y < current_ylim[0] or y > current_ylim[1]:
        ax[0].set_xlim(min(current_xlim[0], x-1), max(current_xlim[1], x+1))
        ax[0].set_ylim(min(current_ylim[0], y-1), max(current_ylim[1], y+1))
    ax[0].figure.canvas.draw_idle()
    ax[1].set_ylim(0, r + 1)
    ax[1].figure.canvas.draw_idle()

    updating = False

def update_theta(val):
    global updating
    if updating:
        return

    try:
        r = float(text_box_r.text)
    except ValueError:
        return

    theta = val

    updating = True

    # Update polar coordinates
    polar_point.set_data([theta], [r])
    polar_line.set_data([0, theta], [0, r])
    polar_label.set_position((theta, r))

    # Convert to Cartesian and update
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    cartesian_point.set_data([x], [y])
    cartesian_line.set_data([0, x], [0, y])
    cartesian_label.set_position((x, y))
    cartesian_label.set_text(f'A ({x:.2f}, {y:.2f})')
    text_box_x.set_val(f'{x:.2f}')
    text_box_y.set_val(f'{y:.2f}')

    # Adjust Cartesian limits if necessary
    current_xlim = ax[0].get_xlim()
    current_ylim = ax[0].get_ylim()
    if x < current_xlim[0] or x > current_xlim[1] or y < current_ylim[0] or y > current_ylim[1]:
        ax[0].set_xlim(min(current_xlim[0], x-1), max(current_xlim[1], x+1))
        ax[0].set_ylim(min(current_ylim[0], y-1), max(current_ylim[1], y+1))
    ax[0].figure.canvas.draw_idle()
    ax[1].set_ylim(0, r + 1)
    ax[1].figure.canvas.draw_idle()

    updating = False

# Text boxes for Cartesian coordinates input
ax_box_x = plt.axes([0.1, 0.05, 0.15, 0.075])
text_box_x = TextBox(ax_box_x, 'X:', initial=str(x_init))
text_box_x.on_submit(update_cartesian)

ax_box_y = plt.axes([0.3, 0.05, 0.15, 0.075])
text_box_y = TextBox(ax_box_y, 'Y:', initial=str(y_init))
text_box_y.on_submit(update_cartesian)

# Text boxes for Polar coordinates input
ax_box_r = plt.axes([0.55, 0.05, 0.15, 0.075])
text_box_r = TextBox(ax_box_r, 'r:', initial=f'{r_init:.2f}')
text_box_r.on_submit(update_polar)

# Slider for theta
ax_slider_theta = plt.axes([0.75, 0.05, 0.15, 0.03], facecolor='lightgoldenrodyellow')
theta_slider = Slider(ax_slider_theta, 'θ', 0, 2*np.pi, valinit=theta_init)
theta_slider.on_changed(update_theta)

plt.show()
