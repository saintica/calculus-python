import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
from scipy.integrate import quad

# Initial function and bounds
initial_function = "1 + 3 * np.cos(2 * theta)"
theta_min, theta_max = 0, 2 * np.pi
int_min, int_max = 0, 2 * np.pi

def polar_function(theta):
    return eval(current_function)

def plot_polar_function(ax, function, theta_min, theta_max, int_min, int_max):
    theta = np.linspace(theta_min, theta_max, 1000)
    r = eval(function)
    
    ax.clear()
    ax.plot(theta, r)
    
    # Shade the area under the curve for the integration bounds
    theta_fill = np.linspace(int_min, int_max, 1000)
    r_fill = eval(function.replace("theta", "theta_fill"))
    ax.fill_between(theta_fill, r_fill, alpha=0.3)
    
    ax.set_ylim(0, max(r) + 1)
    integral_result = integrate_function(function, int_min, int_max)
    ax.set_title(rf"Polar Plot of $r(\theta) = {function}$")
    ax.set_xlabel(r'$\theta$')
    ax.set_ylabel('')
    
    ax_result.clear()
    ax_result.set_xticks([])
    ax_result.set_yticks([])
    ax_result.text(0.1, 0.4, rf"Integral Result: $\int_{{{int_min:.2f}}}^{{{int_max:.2f}}} r(\theta) \, d\theta = {integral_result:.2f}$")

    plt.draw()

def integrate_function(function, int_min, int_max):
    integrand = lambda theta: eval(function)
    result, _ = quad(integrand, int_min, int_max)
    return result

def submit_function(text):
    global current_function
    current_function = text
    plot_polar_function(ax, current_function, theta_min, theta_max, int_min, int_max)

def submit_theta_min(text):
    global theta_min
    theta_min = float(text)
    plot_polar_function(ax, current_function, theta_min, theta_max, int_min, int_max)

def submit_theta_max(text):
    global theta_max
    theta_max = float(text)
    plot_polar_function(ax, current_function, theta_min, theta_max, int_min, int_max)

def submit_int_min(text):
    global int_min
    int_min = float(text)
    plot_polar_function(ax, current_function, theta_min, theta_max, int_min, int_max)

def submit_int_max(text):
    global int_max
    int_max = float(text)
    plot_polar_function(ax, current_function, theta_min, theta_max, int_min, int_max)

# Create the initial plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
plt.subplots_adjust(bottom=0.4)
current_function = initial_function

# Create textboxes for inputs
axbox_func = plt.axes([0.1, 0.25, 0.8, 0.05])
text_box_func = TextBox(axbox_func, r'$r(\theta)$', initial=current_function)
text_box_func.on_submit(submit_function)

ax_result = plt.axes([0.1, 0.14, 0.8, 0.1])
ax_result.set_xticks([])
ax_result.set_yticks([])

axbox_theta_min = plt.axes([0.1, 0.08, 0.3, 0.05])
text_box_theta_min = TextBox(axbox_theta_min, r'$\theta_{\text{min}}$', initial=str(theta_min))
text_box_theta_min.on_submit(submit_theta_min)

axbox_theta_max = plt.axes([0.6, 0.08, 0.3, 0.05])
text_box_theta_max = TextBox(axbox_theta_max, r'$\theta_{\text{max}}$', initial=str(theta_max))
text_box_theta_max.on_submit(submit_theta_max)

axbox_int_min = plt.axes([0.1, 0.02, 0.3, 0.05])
text_box_int_min = TextBox(axbox_int_min, r'$\theta_{\text{0}}$', initial=str(int_min))
text_box_int_min.on_submit(submit_int_min)

axbox_int_max = plt.axes([0.6, 0.02, 0.3, 0.05])
text_box_int_max = TextBox(axbox_int_max, r'$\theta_{\text{1}}$', initial=str(int_max))
text_box_int_max.on_submit(submit_int_max)

plot_polar_function(ax, current_function, theta_min, theta_max, int_min, int_max)

plt.show()
