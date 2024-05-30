import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Wave equation parameters
c = 20  # Wave speed
L = 40  # Length of the domain
N = 200  # Number of points in the domain
dx = L / N  # Spatial step size
dt = dx / (2 * c)  # Time step size for stability
damping = 0.002  # Damping factor

# Initialize the wave field and velocity field
u = np.zeros(N)
u_new = np.zeros(N)
u_old = np.zeros(N)

# Initial condition: Given wave function
x = np.linspace(-L/2, L/2, N)
u = 10 * np.exp(-x**2 / 20)

# Boundary conditions (tied edges)
def apply_boundary_conditions_tied(u):
    u[0] = 0
    u[-1] = 0
    return u

# Boundary conditions (loose edges)
def apply_boundary_conditions_loose(u):
    u[0] = u[1]
    u[-1] = u[-2]
    return u

# Apply initial boundary conditions (choose one)
apply_boundary_conditions = apply_boundary_conditions_loose
u = apply_boundary_conditions(u)
u_old = u.copy()

# Initialize the figure for plotting
fig, ax = plt.subplots()
line, = ax.plot(x, u, color='b')
ax.set_ylim(-11, 11)
ax.set_title('1D Wave Function Animation')
ax.set_xlabel('x')
ax.set_ylabel('Wave function value')

# Runge-Kutta method for the wave equation
def runge_kutta_step(u, u_old, dt, dx, c, damping):
    laplacian_u = (np.roll(u, 1) + np.roll(u, -1) - 2 * u) / dx**2
    u_new = (2 * u - u_old + (c * dt)**2 * laplacian_u) * (1 - damping)
    u_new = apply_boundary_conditions(u_new)
    return u_new

# Update function for animation
def update(frame):
    global u, u_old
    u_new = runge_kutta_step(u, u_old, dt, dx, c, damping)
    u_old = u.copy()
    u = u_new.copy()
    line.set_ydata(u)
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Display the animation
plt.show()
