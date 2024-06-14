from manim import *

class DifferentialWithTangentLine(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3, 1], 
            y_range=[-1, 9, 1], 
            axis_config={"color": BLUE},
        )

        # Labels for the axes
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Function definition
        graph = axes.plot(lambda x: x**2, color=WHITE)

        # Function label
        graph_label = axes.get_graph_label(graph, label="f(x) = x^2")

        # Initial point
        x0 = 1
        dot = Dot().move_to(axes.c2p(x0, x0**2))

        # Tangent line calculation
        def get_tangent_line(x):
            slope = 2 * x  # Derivative of x^2 is 2x
            y = x**2
            tangent_line = Line(
                axes.c2p(x - 1, y - slope),
                axes.c2p(x + 1, y + slope),
                color=YELLOW
            )
            return tangent_line

        tangent_line = get_tangent_line(x0)
        tangent_label = MathTex(r"f'(x) = 2x").next_to(tangent_line, UP)

        # Animation steps
        self.play(Create(axes), Write(labels))
        self.play(Create(graph), Write(graph_label))
        self.play(FadeIn(dot, scale=0.5))
        self.play(Create(tangent_line), Write(tangent_label))

        # Update tangent line as the dot moves
        def update_tangent(mob, alpha):
            x = interpolate(-2, 2, alpha)
            y = x**2
            dot.move_to(axes.c2p(x, y))
            new_tangent_line = get_tangent_line(x)
            mob.become(new_tangent_line)
            tangent_label.next_to(new_tangent_line, UP)
        
        self.play(UpdateFromAlphaFunc(tangent_line, update_tangent), run_time=6, rate_func=linear)
        self.wait()

if __name__ == "__main__":
    scene = DifferentialWithTangentLine()
    scene.render()
