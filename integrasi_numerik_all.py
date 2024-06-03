import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, RadioButtons, Slider

def f(x, func_str):
    return eval(func_str)

def rectangular_integration(f, a, b, n, func_str):
    dx = (b - a) / n
    midpoints = np.linspace(a + dx / 2, b - dx / 2, n)
    integral = np.sum(f(midpoints, func_str) * dx)
    return integral, midpoints, dx

def trapezoidal_integration(f, a, b, n, func_str):
    dx = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x, func_str)
    integral = (dx / 2) * np.sum(y[:-1] + y[1:])
    return integral, x, y

def simpsons_integration(f, a, b, n, func_str):
    if n % 2 != 0:
        n += 1
    dx = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x, func_str)
    integral = (dx / 3) * (y[0] + 2 * np.sum(y[2:n:2]) + 4 * np.sum(y[1:n:2]) + y[n])
    return integral, x, y

def update(val):
    try:
        n = int(n_text_box.text)
    except ValueError:
        return
    
    func_str = func_text_box.text
    method = radio.value_selected

    a = lower_slider.val
    b = upper_slider.val
    
    if a >= b:
        return

    ax.clear()

    if method == 'Rectangular':
        integral, midpoints, dx = rectangular_integration(f, a, b, n, func_str)
        x = np.linspace(a, b, 1000)
        y = f(x, func_str)
        ax.plot(x, y, label=f"$f(x) = {func_str}$")
        ax.fill_between(x, y, alpha=0.2)
        for midpoint in midpoints:
            ax.plot([midpoint - dx / 2, midpoint + dx / 2], [f(midpoint, func_str), f(midpoint, func_str)], 'g')
            ax.plot([midpoint - dx / 2, midpoint - dx / 2], [0, f(midpoint, func_str)], 'g--')
            ax.plot([midpoint + dx / 2, midpoint + dx / 2], [0, f(midpoint, func_str)], 'g--')
    elif method == 'Trapezoidal':
        integral, x_partitions, y_partitions = trapezoidal_integration(f, a, b, n, func_str)
        x = np.linspace(a, b, 1000)
        y = f(x, func_str)
        ax.plot(x, y, label=f"$f(x) = {func_str}$")
        ax.fill_between(x, y, alpha=0.2)
        for i in range(n + 1):
            ax.plot([x_partitions[i], x_partitions[i]], [0, y_partitions[i]], 'g--')
        for i in range(n):
            ax.plot([x_partitions[i], x_partitions[i + 1]], [y_partitions[i], y_partitions[i + 1]], 'g')
    elif method == 'Simpson\'s':
        integral, x_partitions, y_partitions = simpsons_integration(f, a, b, n, func_str)
        x = np.linspace(a, b, 1000)
        y = f(x, func_str)
        ax.plot(x, y, label=f"$f(x) = {func_str}$")
        ax.fill_between(x, y, alpha=0.2)
        for i in range(n + 1):
            ax.plot([x_partitions[i], x_partitions[i]], [0, y_partitions[i]], 'g--')

    ax.set_title(f"Function $f(x) = {func_str}$ and its Integral with Partitions ({method} Rule)")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$f(x)$")
    ax.legend()
    ax.text(0.5 * (a + b), 0.5*max(y), f"Integral $\\approx {integral:.6f}$", horizontalalignment='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))
    plt.draw()

a = 0
b = np.pi
n = 10
func_str = 'np.sin(x)'

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.3, bottom=0.4, top=0.9)

integral, midpoints, dx = rectangular_integration(f, a, b, n, func_str)
x = np.linspace(a, b, 1000)
y = f(x, func_str)
ax.plot(x, y, label=f"$f(x) = {func_str}$")
ax.fill_between(x, y, alpha=0.2)
for midpoint in midpoints:
    ax.plot([midpoint - dx / 2, midpoint + dx / 2], [f(midpoint, func_str), f(midpoint, func_str)], 'g')
    ax.plot([midpoint - dx / 2, midpoint - dx / 2], [0, f(midpoint, func_str)], 'g--')
    ax.plot([midpoint + dx / 2, midpoint + dx / 2], [0, f(midpoint, func_str)], 'g--')

ax.set_title(f"Function $f(x) = {func_str}$ and its Integral with Partitions (Rectangular Rule)")
ax.set_xlabel("$x$")
ax.set_ylabel("$f(x)$")
ax.legend()
ax.text(0.5 * (a + b), 0.5, f"Integral $\\approx {integral:.6f}$", horizontalalignment='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

axbox_n = plt.axes([0.1, 0.15, 0.1, 0.075])
n_text_box = TextBox(axbox_n, 'n: ', initial=str(n))
n_text_box.on_submit(update)

axbox_func = plt.axes([0.1, 0.05, 0.6, 0.075])
func_text_box = TextBox(axbox_func, 'Function: ', initial=func_str)
func_text_box.on_submit(update)

axbox_radio = plt.axes([0.05, 0.55, 0.2, 0.2])
radio = RadioButtons(axbox_radio, ('Rectangular', 'Trapezoidal', "Simpson's"))
radio.on_clicked(update)

lower_slider_ax = plt.axes([0.1, 0.30, 0.5, 0.03])
lower_slider = Slider(lower_slider_ax, 'Lower Bound', 0.0, 2.0 * np.pi, valinit=a)
lower_slider.on_changed(update)

upper_slider_ax = plt.axes([0.1, 0.25, 0.5, 0.03])
upper_slider = Slider(upper_slider_ax, 'Upper Bound', 0.0, 2.0 * np.pi, valinit=b)
upper_slider.on_changed(update)

plt.show()
