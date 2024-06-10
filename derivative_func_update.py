import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import TextBox
from sympy import symbols, diff, lambdify, sympify, sin, cos, exp, log

# Symbol for sympy
x_sym = symbols('x')

# Initial function and its derivative using sympy
function_str = 'sin(x)'
f_expr = sympify(function_str, locals={'sin': sin, 'cos': cos, 'exp': exp, 'log': log})
f = lambdify(x_sym, f_expr, 'numpy')
df = lambdify(x_sym, diff(f_expr, x_sym), 'numpy')

# Generate x values
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y = f(x)

# Set up the figure, axis, and plot elements
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)  # Adjust to make space for text boxes
ax.set_xlim((x[0], x[-1]))
ax.set_ylim((np.min(y) - 0.5, np.max(y) + 0.5))
line, = ax.plot(x, y, lw=2)
point, = ax.plot([], [], 'ro')
tangent_line, = ax.plot([], [], 'r--', lw=2)

# Function to update plot based on textbox input
def submit_function(expression):
    global f, df, x, y, line, ax
    try:
        # Update the function and its derivative
        f_expr = sympify(expression, locals={'sin': sin, 'cos': cos, 'exp': exp, 'log': log, 'x': x_sym})
        f = lambdify(x_sym, f_expr, 'numpy')
        df_expr = diff(f_expr, x_sym)
        df = lambdify(x_sym, df_expr, 'numpy')
        
        # Update y values
        y = f(x)
        line.set_ydata(y)
        
        # Update plot limits based on new y values
        y_min, y_max = np.min(y), np.max(y)
        ax.set_ylim((y_min - 0.5, y_max + 0.5))
        
        # Update title
        ax.set_title(f'Function: {expression}    Derivative: {str(df_expr)}', pad=20)
        
        fig.canvas.draw_idle()
    except Exception as e:
        print(f"Error in expression: {e}")

# Set up the text box for function input
axbox = plt.axes([0.15, 0.15, 0.75, 0.05])
text_box = TextBox(axbox, 'Function f(x)', initial=function_str)
text_box.on_submit(submit_function)

# Initialization function: plot the background of each frame
def init():
    point.set_data([], [])
    tangent_line.set_data([], [])
    return point, tangent_line

# Animation function: this is called sequentially
def animate(i):
    # Get the current x value and the corresponding y value
    x0 = x[i]
    y0 = f(x0)
    
    # Set the point location
    point.set_data([x0], [y0])
    
    # Calculate the slope (derivative) at x0
    slope = df(x0)
    
    # Create the tangent line
    tangent_x = np.linspace(x0 - 1, x0 + 1, 10)
    tangent_y = y0 + slope * (tangent_x - x0)
    
    # Set the tangent line data
    tangent_line.set_data(tangent_x, tangent_y)
    
    return point, tangent_line

# Create animation
ani = FuncAnimation(fig, animate, init_func=init, frames=len(x), interval=25, blit=True)

# Show plot
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Function: {function_str}    Derivative: {str(diff(f_expr, x_sym))}', pad=20)
plt.show()
