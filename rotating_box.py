import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button

# Function to create a cube
def create_cube():
    r = [-1, 1]
    vertices = np.array([[x, y, z] for x in r for y in r for z in r])
    edges = [[vertices[j] for j in range(8) if (i & (1 << j))] for i in range(1, 256)]
    return vertices, edges

# Function to update the rotation of the cube
def update_cube(i, lines, vertices, ax):
    ax.cla()
    angle = i * np.pi / 45
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])
    rotated_vertices = vertices @ rotation_matrix.T
    for edge in lines:
        ax.plot(*zip(*rotated_vertices[edge]), color='b')
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_axis_off()

# Initialize the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
vertices, edges = create_cube()
lines = [[0, 1], [0, 2], [0, 4], [1, 3], [1, 5], [2, 3], [2, 6], [3, 7], [4, 5], [4, 6], [5, 7], [6, 7]]

# Button callback functions
class ButtonCallback:
    def __init__(self):
        self.anim_running = True

    def start(self, event):
        if not self.anim_running:
            self.anim.event_source.start()
            self.anim_running = True

    def stop(self, event):
        if self.anim_running:
            self.anim.event_source.stop()
            self.anim_running = False

callback = ButtonCallback()

# Create the buttons
axstart = plt.axes([0.7, 0.05, 0.1, 0.075])
axstop = plt.axes([0.81, 0.05, 0.1, 0.075])
btn_start = Button(axstart, 'Start')
btn_stop = Button(axstop, 'Stop')
btn_start.on_clicked(callback.start)
btn_stop.on_clicked(callback.stop)

# Create the animation
callback.anim = FuncAnimation(fig, update_cube, frames=np.arange(0, 90), fargs=(lines, vertices, ax), interval=50, repeat=True)

# Display the plot
plt.show()
