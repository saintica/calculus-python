import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify, limit
from matplotlib.widgets import TextBox, Slider

# Function to plot the curve and update the y-value and limits
def plot_function():
    try:
        func_expr = function_text.text
        x_val = float(x_value_text.text)
        left_lim = left_slider.val
        right_lim = right_slider.val

        x = symbols('x')
        func_sympy = sympify(func_expr)
        func = lambdify(x, func_sympy, modules=['numpy'])
        
        x_vals = np.linspace(x_val - 10, x_val + 10, 400)
        y_vals = func(x_vals)
        y_vals = np.nan_to_num(y_vals, nan=np.nan, posinf=np.nan, neginf=np.nan)  # Handle singularities
        
        ax.clear()
        ax.plot(x_vals, y_vals, label=f'f(x) = {func_expr}')
        ax.scatter([x_val], [func(x_val)], color='red')
        ax.axvline(left_lim, color='blue', linestyle='--', label=f'Left Limit ({left_lim})')
        ax.axvline(right_lim, color='green', linestyle='--', label=f'Right Limit ({right_lim})')
        ax.set_title('Function Plot')
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.legend()
        ax.grid(True)
        
        y_val = func(x_val)
        y_label.set_text(f"f({x_val}) = {y_val}")
        
        left_limit_value = limit(func_sympy, x, left_lim)
        right_limit_value = limit(func_sympy, x, right_lim)
        left_limit_label.set_text(f"Left limit as x -> {left_lim}: {left_limit_value}")
        right_limit_label.set_text(f"Right limit as x -> {right_lim}: {right_limit_value}")
        
        # Update slider limits
        left_slider.valmin = x_val - 5
        left_slider.valmax = x_val
        right_slider.valmin = x_val
        right_slider.valmax = x_val + 5

        # Redraw the sliders with new boundaries
        left_slider.ax.set_xlim(left_slider.valmin, left_slider.valmax)
        right_slider.ax.set_xlim(right_slider.valmin, right_slider.valmax)

        fig.canvas.draw_idle()
    except Exception as e:
        y_label.set_text(f"Error: {e}")

def on_release(event):
    if event.inaxes == ax_slider_left or event.inaxes == ax_slider_right:
        plot_function()

# Initial function and x value
initial_func = 'x**2'
initial_x_val = 0

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.4)

# Add text boxes for function and x value input
axbox_func = plt.axes([0.1, 0.32, 0.3, 0.05])
function_text = TextBox(axbox_func, 'Function:', initial=initial_func)
function_text.on_submit(lambda text: plot_function())

axbox_x = plt.axes([0.6, 0.32, 0.1, 0.05])
x_value_text = TextBox(axbox_x, 'x value:', initial=str(initial_x_val))
x_value_text.on_submit(lambda text: plot_function())

# Add labels to display y value and limits
axlabel_y = plt.axes([0.1, 0.25, 0.8, 0.05], facecolor='lightgoldenrodyellow')
y_label = axlabel_y.text(0.1, 0.5, '', transform=axlabel_y.transAxes, fontsize=10)

axlabel_left = plt.axes([0.1, 0.2, 0.8, 0.05], facecolor='lightgoldenrodyellow')
left_limit_label = axlabel_left.text(0.1, 0.5, '', transform=axlabel_left.transAxes, fontsize=10)

axlabel_right = plt.axes([0.1, 0.15, 0.8, 0.05], facecolor='lightgoldenrodyellow')
right_limit_label = axlabel_right.text(0.1, 0.5, '', transform=axlabel_right.transAxes, fontsize=10)

# Add sliders for left and right limits
ax_slider_left = plt.axes([0.1, 0.08, 0.35, 0.03], facecolor='lightgoldenrodyellow')
left_slider = Slider(ax_slider_left, 'Left Limit', initial_x_val - 5, initial_x_val, valinit=initial_x_val - 1)
ax_slider_right = plt.axes([0.55, 0.08, 0.35, 0.03], facecolor='lightgoldenrodyellow')
right_slider = Slider(ax_slider_right, 'Right Limit', initial_x_val, initial_x_val + 5, valinit=initial_x_val + 1)

# Connect release event to the on_release function
fig.canvas.mpl_connect('button_release_event', on_release)

# Initial plot
plot_function()

plt.show()
