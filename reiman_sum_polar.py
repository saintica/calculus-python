import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Slider
from sympy import symbols, lambdify, sympify, sin, cos, tan, exp, log

# Define theta_sym globally
theta_sym = symbols('theta')

def update_plot(theta_min, theta_max):
    try:
        theta_min = float(theta_min)
        theta_max = float(theta_max)
        ax.set_xlim((theta_min, theta_max))

        # Update theta and r values for the function
        theta_new = np.linspace(theta_min, theta_max, 400)
        r_new = f(theta_new)
        line.set_data(theta_new, r_new)

        # Update y limits based on the new function data
        ax.set_ylim((0, np.max(r_new) + 0.5))

        update_riemann_sum(theta_min, theta_max, slider.val)
        plt.draw()
    except ValueError:
        print("Please enter valid numeric values for theta limits.")

def submit_function(expression):
    global f, theta, r
    try:
        # Update the function
        f_expr = sympify(expression, locals={'sin': sin, 'cos': cos, 'tan': tan, 'exp': exp, 'log': log, 'theta': theta_sym})
        f = lambdify(theta_sym, f_expr, 'numpy')

        # Update r values
        r = f(theta)

        # Update title
        ax.set_title(fr'$\text{{r(\theta): }} {expression}$')

        update_plot(ax.get_xlim()[0], ax.get_xlim()[1])
    except Exception as e:
        print(f"Error in expression: {e}")

def submit_theta_limits(text):
    update_plot(text_box_thetamin.text, text_box_thetamax.text)

def update_riemann_sum(theta_min, theta_max, n):
    theta_vals = np.linspace(theta_min, theta_max, int(n) + 1)
    r_vals = f(theta_vals)
    areas = 0.5 * (theta_vals[1:] - theta_vals[:-1]) * (r_vals[:-1]**2 + r_vals[1:]**2)
    
    # Clear existing patches
    for patch in reversed(ax.patches):
        patch.remove()

    # Add new patches
    for i in range(len(theta_vals) - 1):
        theta0 = theta_vals[i]
        theta1 = theta_vals[i+1]
        r0 = r_vals[i]
        r1 = r_vals[i+1]
        wedge = plt.Polygon([
            (0, 0),
            (r0 * np.cos(theta0), r0 * np.sin(theta0)),
            (r1 * np.cos(theta1), r1 * np.sin(theta1)),
        ], edgecolor='blue', facecolor='lightblue', alpha=0.5)
        ax.add_patch(wedge)
    
    riemann_sum = np.sum(areas)
    sum_label.set_text(f'Riemann Sum: {riemann_sum:.5f}')
    plt.draw()

def update_partitions(val):
    update_riemann_sum(ax.get_xlim()[0], ax.get_xlim()[1], val)
    plt.draw()

def main():
    global theta, f, ax, line, text_box_thetamin, text_box_thetamax, text_box_function, slider, sum_label

    # Symbol for sympy
    theta_sym = symbols('theta')

    # Initial function using sympy
    function_str = '1 + sin(theta)'
    f_expr = sympify(function_str, locals={'sin': sin, 'cos': cos, 'tan': tan, 'exp': exp, 'log': log})
    f = lambdify(theta_sym, f_expr, 'numpy')

    # Generate theta values
    theta = np.linspace(0, 2 * np.pi, 400)
    r = f(theta)

    # Set up the figure, axis, and plot elements
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    plt.subplots_adjust(bottom=0.4)  # Adjust to make space for text boxes and slider
    line, = ax.plot(theta, r, lw=2)

    # Set up the text box for function input
    axbox_function = plt.axes([0.15, 0.3, 0.75, 0.05])
    text_box_function = TextBox(axbox_function, 'r(θ): ', initial=function_str)
    text_box_function.on_submit(submit_function)

    # Text boxes for adjusting theta min and max limits
    axbox_thetamin = plt.axes([0.15, 0.2, 0.3, 0.05])
    axbox_thetamax = plt.axes([0.6, 0.2, 0.3, 0.05])
    text_box_thetamin = TextBox(axbox_thetamin, 'θ Min', initial=str(theta[0]))
    text_box_thetamax = TextBox(axbox_thetamax, 'θ Max', initial=str(theta[-1]))

    text_box_thetamin.on_submit(submit_theta_limits)
    text_box_thetamax.on_submit(submit_theta_limits)

    # Slider for adjusting the number of partitions
    ax_slider = plt.axes([0.15, 0.1, 0.75, 0.03])
    slider = Slider(ax_slider, 'Partitions', 1, 100, valinit=50, valstep=1)
    slider.on_changed(update_partitions)

    # Label to display the Riemann sum
    sum_label = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=14, verticalalignment='top')

    # Show plot
    ax.grid(True)
    ax.set_title(fr'$\text{{r(\theta): }} {function_str}$')
    update_riemann_sum(theta[0], theta[-1], slider.val)
    plt.show()

if __name__ == "__main__":
    main()
