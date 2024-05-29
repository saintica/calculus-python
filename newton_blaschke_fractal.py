import numpy as np
import matplotlib.pyplot as plt

def blaschke_product(z, zeros):
    result = np.ones_like(z, dtype=complex)
    for zero in zeros:
        result *= (z - zero) / (1 - np.conj(zero) * z)
    return result

def blaschke_derivative(z, zeros):
    derivative = np.zeros_like(z, dtype=complex)
    product = np.ones_like(z, dtype=complex)
    for zero in zeros:
        product *= (z - zero) / (1 - np.conj(zero) * z)
    for zero in zeros:
        partial = (1 - np.conj(zero) * z + zero - z) / ((1 - np.conj(zero) * z)**2)
        derivative += product / ((z - zero) / (1 - np.conj(zero) * z)) * partial
    return derivative

def newton_fractal(width, height, x_min, x_max, y_min, y_max, zeros, max_iter=100, tol=1e-6):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    fractal = np.zeros(Z.shape, dtype=int)
    for i in range(max_iter):
        B = blaschke_product(Z, zeros)
        dB = blaschke_derivative(Z, zeros)
        Z_next = Z - B / dB
        mask = np.abs(Z_next - Z) < tol
        fractal[mask] = i
        Z = Z_next
        if np.all(mask):
            break

    return fractal

# Parameters
width, height = 800, 800
x_min, x_max = -2, 2
y_min, y_max = -2, 2
zeros = [0.5 + 0.5j, -0.5 - 0.5j, 0.5 - 0.5j, -0.5 + 0.5j]  # Example zeros of the Blaschke product

# Generate the fractal
fractal = newton_fractal(width, height, x_min, x_max, y_min, y_max, zeros)

# Plot the fractal
plt.figure(figsize=(10, 10))
plt.imshow(fractal, extent=(x_min, x_max, y_min, y_max), cmap='viridis')
plt.colorbar()
plt.title('Newton Fractal for Blaschke Product')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.show()
