import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import TextBox
from sympy import symbols, diff, lambdify, sympify, sin, cos, tan, exp, log

x_sym = symbols('x')  # Define x_sym globally

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

        plt.draw()
    except ValueError:
        print("Please enter valid numeric values for x limits.")

def submit_function(expression):
    global f, df, x, y
    try:
        # Update the function and its derivative
        f_expr = sympify(expression, locals={'sin': sin, 'cos': cos,'tan':tan, 'exp': exp, 'log': log, 'x': x_sym})
        f = lambdify(x_sym, f_expr, 'numpy')
        df_expr = diff(f_expr, x_sym)
        df = lambdify(x_sym, df_expr, 'numpy')

        # Update y values
        y = f(x)

        # Update title
        ax.set_title(fr'$\text{{f(x): }} {expression} \quad \text{{df(x): }} {str(df_expr)}$', pad=20)

        update_plot(ax.get_xlim()[0], ax.get_xlim()[1])
    except Exception as e:
        print(f"Error in expression: {e}")

def submit_x_limits(text):
    update_plot(text_box_xmin.text, text_box_xmax.text)

def init():
    point.set_data([], [])
    tangent_line.set_data([], [])
    return point, tangent_line


def animate(i):
    # Update x values based on current x limits
    x_new = np.linspace(ax.get_xlim()[0], ax.get_xlim()[1], 400)
    y_new = f(x_new)

    # Update function line
    line.set_data(x_new, y_new)

    # Get the current x value and the corresponding y value
    x0 = x_new[i]
    y0 = y_new[i]

    # Set the point location
    point.set_data([x0], [y0])

    # Calculate the slope (derivative) at x0
    slope = df(x0)

    # Create the tangent line
    tangent_x = np.linspace(x0 - 1, x0 + 1, 10)
    tangent_y = y0 + slope * (tangent_x - x0)

    # Set the tangent line data
    tangent_line.set_data(tangent_x, tangent_y)

    return line, point, tangent_line


def main():
    global x, f, df, ax, line, point, tangent_line, text_box_xmin, text_box_xmax, text_box_function

    # Symbol for sympy
    x_sym = symbols('x')

    # Initial function and its derivative using sympy
    function_str = 'sin(x)'
    f_expr = sympify(function_str, locals={'sin': sin, 'cos': cos,'tan':tan, 'exp': exp, 'log': log})
    f = lambdify(x_sym, f_expr, 'numpy')
    df = lambdify(x_sym, diff(f_expr, x_sym), 'numpy')

    # Generate x values
    x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
    y = f(x)

    # Set up the figure, axis, and plot elements
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.5)  # Adjust to make space for text boxes
    line, = ax.plot(x, y, lw=2)
    point, = ax.plot([], [], 'ro')
    tangent_line, = ax.plot([], [], 'r--', lw=2)

    # Set up the text box for function input
    axbox_function = plt.axes([0.15, 0.25, 0.75, 0.05])
    text_box_function = TextBox(axbox_function, 'f(x): ', initial=function_str)
    text_box_function.on_submit(submit_function)

    # Text boxes for adjusting x min and max limits
    axbox_xmin = plt.axes([0.15, 0.15, 0.3, 0.05])
    axbox_xmax = plt.axes([0.6, 0.15, 0.3, 0.05])
    text_box_xmin = TextBox(axbox_xmin, 'X Min', initial=str(x[0]))
    text_box_xmax = TextBox(axbox_xmax, 'X Max', initial=str(x[-1]))

    text_box_xmin.on_submit(submit_x_limits)
    text_box_xmax.on_submit(submit_x_limits)

    # Initialization function: plot the background of each frame
    init()

    # Create animation
    ani = FuncAnimation(fig, animate, init_func=init, frames=len(x), interval=25, blit=True)

    # Show plot
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title(fr'$\text{{f(x): }} {function_str} \quad \text{{df(x): }} {str(diff(f_expr, x_sym))}$', pad=20)
    plt.show()

if __name__ == "__main__":
    main()
