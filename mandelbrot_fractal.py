import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    """
    Compute the Mandelbrot set for a complex number c
    """
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    """
    Generate a Mandelbrot set image
    """
    # Create a 2D array of complex numbers representing the grid
    real = np.linspace(x_min, x_max, width)
    imag = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(real, imag)
    C = X + 1j * Y

    # Initialize the output image
    mandelbrot_set = np.zeros(C.shape, dtype=int)

    # Compute the Mandelbrot set
    for i in range(width):
        for j in range(height):
            mandelbrot_set[j, i] = mandelbrot(C[j, i], max_iter)

    return mandelbrot_set

def plot_mandelbrot(mandelbrot_set, cmap='hot'):
    """
    Plot the Mandelbrot set with a given colormap
    """
    plt.figure(figsize=(10, 10))
    plt.imshow(mandelbrot_set, cmap=cmap, extent=(x_min, x_max, y_min, y_max))
    plt.colorbar()
    plt.title('Mandelbrot Fractal')
    plt.xlabel('Re(c)')
    plt.ylabel('Im(c)')
    plt.show()

# Parameters for the Mandelbrot set
width, height = 800, 800
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = 256

# Generate the Mandelbrot set
mandelbrot_set = generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter)

# Plot the Mandelbrot set
plot_mandelbrot(mandelbrot_set, cmap='twilight')
