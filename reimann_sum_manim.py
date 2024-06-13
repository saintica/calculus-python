from manim import *
import numpy as np

class RiemannSum(Scene):
    def construct(self):
        # Define the function to integrate
        def func(x):
            return 2*np.exp(-x/2)*np.sin(3*x)
        
        # Axis
        axes = Axes(
            x_range=[0, PI, PI/4],
            y_range=[-1.5, 2.0, 0.5],
            axis_config={"include_tip": True}
        )
        labels = axes.get_axis_labels(x_label="X", y_label="Y")
        x_label = MathTex(r"\pi").next_to(axes.x_axis.get_end(), DOWN)
        y_label = MathTex(r"1").next_to(axes.y_axis.get_end(), LEFT)
        
        # Function graph
        func_graph = axes.plot(func, x_range=[0, PI], color=BLUE)
        
        # Title
        title = Tex("Riemann Sum Approximation of $\\int_0^\\pi 2 e^{-x/2} \\sin(3x)dx$").to_edge(UP)
        
        # Add axes, labels, and title to the scene
        self.play(Create(axes), Create(labels), Write(x_label), Write(y_label))
        self.play(Create(func_graph), Write(title))
        
        # Parameters
        a = 0
        b = PI
        
        # Number of partitions (initial value)
        n_partitions = ValueTracker(1)
        
        # Riemann sum value
        riemann_sum = always_redraw(
            lambda: MathTex(
                f"\\text{{Riemann Sum: }} {self.calculate_riemann_sum(func, a, b, n_partitions.get_value()):.5f}"
            ).to_edge(DOWN)
        )
        
        # Current number of partitions
        partitions_label = always_redraw(
            lambda: MathTex(
                f"n = {int(n_partitions.get_value())}"
            ).next_to(riemann_sum, UP)
        )
        
        # Rectangles for Riemann sum
        rectangles = always_redraw(
            lambda: axes.get_riemann_rectangles(
                graph=func_graph,
                x_range=[a, b],
                dx=(b-a)/n_partitions.get_value(),
                stroke_width=0.5,
                stroke_color=WHITE,
                fill_opacity=0.75
            )
        )
        
        # Add rectangles, sum, and partitions label to the scene
        self.play(Create(rectangles), Write(riemann_sum), Write(partitions_label))
        
        # Animate the increase of partitions from 1 to 100
        self.play(n_partitions.animate.set_value(100), run_time=10, rate_func=linear)
        
        self.wait(2)
    
    def calculate_riemann_sum(self, func, a, b, n):
        dx = (b - a) / n
        midpoints = np.linspace(a + dx/2, b - dx/2, int(n))
        return np.sum(func(midpoints) * dx)

# Save the script as riemann_sum.py and run it with the following command:
# manim -pql riemann_sum.py RiemannSum
