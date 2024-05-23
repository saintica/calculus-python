import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Define the function and its partial derivatives
def f(x, y):
    return np.sin(x) * np.cos(y)

def df_dx(x, y):
    return np.cos(x) * np.cos(y)

def df_dy(x, y):
    return -np.sin(x) * np.sin(y)

# Set up the figure and 3D axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0, bottom=0.25, right=0.5, top=0.9)

# Create a meshgrid for the surface plot
x = np.linspace(-np.pi, np.pi, 100)
y = np.linspace(-np.pi, np.pi, 100)
x, y = np.meshgrid(x, y)
z = f(x, y)

# Plot the surface
surf = ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.6, cmap='viridis')

# Set labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Initialize a point and tangent lines
point, = ax.plot([0], [0], [f(0, 0)], 'ro')
tangent_line_x, = ax.plot([], [], [], 'b', linewidth=2)
tangent_line_y, = ax.plot([], [], [], 'g', linewidth=2)

# Slider axes
axcolor = 'lightgoldenrodyellow'
ax_x = plt.axes([0.6, 0.4, 0.2, 0.03], facecolor=axcolor)
ax_y = plt.axes([0.6, 0.5, 0.2, 0.03], facecolor=axcolor)

# Sliders
s_x = Slider(ax_x, 'X', -np.pi, np.pi, valinit=0)
s_y = Slider(ax_y, 'Y', -np.pi, np.pi, valinit=0)

# Update function
def update(val):
    point_x = s_x.val
    point_y = s_y.val
    point_z = f(point_x, point_y)
    
    slope_x = df_dx(point_x, point_y)
    slope_y = df_dy(point_x, point_y)
    
    tangent_x_x = np.linspace(point_x - 0.5, point_x + 0.5, 100)
    tangent_x_y = np.full_like(tangent_x_x, point_y)
    tangent_x_z = slope_x * (tangent_x_x - point_x) + point_z
    
    tangent_y_y = np.linspace(point_y - 0.5, point_y + 0.5, 100)
    tangent_y_x = np.full_like(tangent_y_y, point_x)
    tangent_y_z = slope_y * (tangent_y_y - point_y) + point_z
    
    point.set_data([point_x], [point_y])
    point.set_3d_properties([point_z])
    
    tangent_line_x.set_data(tangent_x_x, tangent_x_y)
    tangent_line_x.set_3d_properties(tangent_x_z)
    
    tangent_line_y.set_data(tangent_y_x, tangent_y_y)
    tangent_line_y.set_3d_properties(tangent_y_z)
    
    fig.canvas.draw_idle()

# Connect the update function to sliders
s_x.on_changed(update)
s_y.on_changed(update)

# Initial call to update to set up plot
update(None)

plt.show()
