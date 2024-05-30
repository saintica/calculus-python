import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Wave equation parameters
c = 1  # Wave speed
L = 10  # Length of the domain
N = 100  # Number of points in each dimension
dx = L / N  # Spatial step size
dt = dx / (2 * c)  # Time step size for stability

# Initialize the wave field and velocity field
u = np.zeros((N, N))
u_new = np.zeros((N, N))
u_old = np.zeros((N, N))

# Initial condition: Gaussian in the center
x = np.linspace(0, L, N)
y = np.linspace(0, L, N)
X, Y = np.meshgrid(x, y)
u = np.exp(-((X - L/2)**2 + (Y - L/2)**2))*np.sin(-((X - L/2) * (Y - L/2)))

# Boundary conditions (fixed edges)
def apply_boundary_conditions(u):
    u[0, :] = 0
    u[-1, :] = 0
    u[:, 0] = 0
    u[:, -1] = 0
    return u

# Apply initial boundary conditions
u = apply_boundary_conditions(u)

# Initialize the figure for plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_zlim(-1, 1)

# Runge-Kutta method for the wave equation
def runge_kutta_step(u, u_old, dt, dx, c):
    laplacian_u = (np.roll(u, 1, axis=0) + np.roll(u, -1, axis=0) + 
                   np.roll(u, 1, axis=1) + np.roll(u, -1, axis=1) - 4 * u) / dx**2
    u_new = 2 * u - u_old + (c * dt)**2 * laplacian_u
    u_new = apply_boundary_conditions(u_new)
    return u_new

# Update function for animation
def update(frame):
    global u, u_old
    u_new = runge_kutta_step(u, u_old, dt, dx, c)
    u_old = u.copy()
    u = u_new.copy()
    ax.clear()
    ax.set_zlim(-1, 1)
    surf = ax.plot_surface(X, Y, u, cmap='viridis')
    return surf,

# Create the animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=False)
# Save the animation as a GIF
ani.save('2d_wave_function.gif', writer='pillow', fps=60)

# Display the animation
plt.show()
