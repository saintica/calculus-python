import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Slider
from sympy import symbols, lambdify, sympify, sin, cos, tan, exp, log

# Define x_sym globally
x_sym = symbols('x')

def update_plot(x_min, x_max):
    try:
        x_min = float(x_min)
        x_max = float(x_max)
        ax.set_xlim((x_min, x_max))

        # Update x and y values for the function
        x_new = np.linspace(x_min, x_max, 400)
        y_new = f(x_new)
        line.set_data(x_new, y_new)

        # Update y limits based on the new function data
        ax.set_ylim((np.min(y_new) - 0.5, np.max(y_new) + 0.5))

        update_riemann_sum(x_min, x_max, slider.val)
        plt.draw()
    except ValueError:
        print("Please enter valid numeric values for x limits.")

def submit_function(expression):
    global f, x, y
    try:
        # Update the function
        f_expr = sympify(expression, locals={'sin': sin, 'cos': cos, 'tan': tan, 'exp': exp, 'log': log, 'x': x_sym})
        f = lambdify(x_sym, f_expr, 'numpy')

        # Update y values
        y = f(x)

        # Update title
        ax.set_title(fr'$\text{{f(x): }} {expression}$')

        update_plot(ax.get_xlim()[0], ax.get_xlim()[1])
    except Exception as e:
        print(f"Error in expression: {e}")

def submit_x_limits(text):
    update_plot(text_box_xmin.text, text_box_xmax.text)

def update_riemann_sum(x_min, x_max, n):
    x_vals = np.linspace(x_min, x_max, int(n) + 1)
    y_vals = f((x_vals[:-1] + x_vals[1:]) / 2)
    heights = y_vals
    widths = (x_max - x_min) / n

    # Clear existing rectangles
    for patch in reversed(ax.patches):
        patch.remove()

    # Add new rectangles
    for x_val, height in zip(x_vals[:-1], heights):
        rect = plt.Rectangle((x_val, 0), widths, height, edgecolor='blue', facecolor='lightblue', alpha=0.5)
        ax.add_patch(rect)
    
    riemann_sum = np.sum(heights * widths)
    sum_label.set_text(f'Riemann Sum: {riemann_sum:.4f}')
    plt.draw()

def update_partitions(val):
    update_riemann_sum(ax.get_xlim()[0], ax.get_xlim()[1], val)
    plt.draw()

def main():
    global x, f, ax, line, text_box_xmin, text_box_xmax, text_box_function, slider, sum_label

    # Symbol for sympy
    x_sym = symbols('x')

    # Initial function using sympy
    function_str = 'exp(-x)*sin(3*x)'
    f_expr = sympify(function_str, locals={'sin': sin, 'cos': cos, 'tan': tan, 'exp': exp, 'log': log})
    f = lambdify(x_sym, f_expr, 'numpy')

    # Generate x values
    x = np.linspace(0, 2 * np.pi, 400)
    y = f(x)

    # Set up the figure, axis, and plot elements
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.4)  # Adjust to make space for text boxes and slider
    line, = ax.plot(x, y, lw=2)

    # Set up the text box for function input
    axbox_function = plt.axes([0.15, 0.3, 0.75, 0.05])
    text_box_function = TextBox(axbox_function, 'f(x): ', initial=function_str)
    text_box_function.on_submit(submit_function)

    # Text boxes for adjusting x min and max limits
    axbox_xmin = plt.axes([0.15, 0.2, 0.3, 0.05])
    axbox_xmax = plt.axes([0.6, 0.2, 0.3, 0.05])
    text_box_xmin = TextBox(axbox_xmin, 'X Min', initial=str(x[0]))
    text_box_xmax = TextBox(axbox_xmax, 'X Max', initial=str(x[-1]))

    text_box_xmin.on_submit(submit_x_limits)
    text_box_xmax.on_submit(submit_x_limits)

    # Slider for adjusting the number of partitions
    ax_slider = plt.axes([0.15, 0.1, 0.75, 0.03])
    slider = Slider(ax_slider, 'Partitions', 1, 100, valinit=50, valstep=1)
    slider.on_changed(update_partitions)

    # Label to display the Riemann sum
    sum_label = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=14, verticalalignment='top')

    # Show plot
    ax.grid(True)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(fr'$\text{{f(x): }} {function_str}$')
    update_riemann_sum(x[0], x[-1], slider.val)
    plt.show()

if __name__ == "__main__":
    main()
