import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def hexagonal_tessellation(ax, rows, cols, size):
    """Create a hexagonal (honeycomb) tessellation."""
    for row in range(rows):
        for col in range(cols):
            offset_x = size * 1.5 * col
            offset_y = size * np.sqrt(3) * (row + 0.5 * (col % 2))
            hexagon = np.array([
                [np.cos(np.pi / 3 * i) * size + offset_x, np.sin(np.pi / 3 * i) * size + offset_y]
                for i in range(6)
            ])
            polygon = Polygon(hexagon, closed=True, edgecolor='k', facecolor=np.random.rand(3,))
            ax.add_patch(polygon)
    ax.set_xlim(0, cols * size * 1.5)
    ax.set_ylim(0, rows * size * np.sqrt(3))
    ax.set_aspect('equal')
    ax.axis('off')

def triangular_tessellation(ax, rows, cols, size):
    """Create a triangular tessellation."""
    for row in range(rows):
        for col in range(cols):
            offset_x = col * size
            offset_y = row * size * np.sqrt(3) / 2
            triangle_up = np.array([
                [offset_x, offset_y],
                [offset_x + size / 2, offset_y + size * np.sqrt(3) / 2],
                [offset_x - size / 2, offset_y + size * np.sqrt(3) / 2]
            ])
            triangle_down = triangle_up + np.array([0, size * np.sqrt(3) / 2])
            polygon_up = Polygon(triangle_up, closed=True, edgecolor='k', facecolor=np.random.rand(3,))
            polygon_down = Polygon(triangle_down, closed=True, edgecolor='k', facecolor=np.random.rand(3,))
            ax.add_patch(polygon_up)
            ax.add_patch(polygon_down)
    ax.set_xlim(0, cols * size)
    ax.set_ylim(0, rows * size * np.sqrt(3) / 2 + size * np.sqrt(3) / 2)
    ax.set_aspect('equal')
    ax.axis('off')

def square_tessellation(ax, rows, cols, size):
    """Create a square tessellation."""
    for row in range(rows):
        for col in range(cols):
            offset_x = col * size
            offset_y = row * size
            square = np.array([
                [offset_x, offset_y],
                [offset_x + size, offset_y],
                [offset_x + size, offset_y + size],
                [offset_x, offset_y + size]
            ])
            polygon = Polygon(square, closed=True, edgecolor='k', facecolor=np.random.rand(3,))
            ax.add_patch(polygon)
    ax.set_xlim(0, cols * size)
    ax.set_ylim(0, rows * size)
    ax.set_aspect('equal')
    ax.axis('off')

# Plotting the tessellations
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Hexagonal Tessellation
hexagonal_tessellation(axs[0], 10, 10, 1)
axs[0].set_title("Hexagonal Tessellation")

# Triangular Tessellation
triangular_tessellation(axs[1], 10, 10, 1)
axs[1].set_title("Triangular Tessellation")

# Square Tessellation
square_tessellation(axs[2], 10, 10, 1)
axs[2].set_title("Square Tessellation")

plt.tight_layout()
plt.show()
