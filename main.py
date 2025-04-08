from manim import *


class Mdp(Scene):
    def construct(self):
        title = Title("Markov Decision Process (MDP)")
        self.play(Write(title))
        mdp_def = MathTex(
            r"""
            \mathcal{S} &- \text{State space} \\
            \mathcal{A} &- \text{Action space} \\
            \mathcal{P} &- \text{State transition probability function} \\
            \mathcal{R} &- \text{Reward function} \\
            """,
            substrings_to_isolate=(r"\sigma", r"\rho", r"\beta")
        ).scale(1).move_to(ORIGIN)
        self.play(Write(mdp_def))
        self.wait(5)


class ValueFunctions(Scene):
    def construct(self):
        title = Title("Value functions")
        self.play(Write(title))
        return_name = Text("Return")
        state_value = Text("State value")
        action_value = Text("Action value")

        return_eq = MathTex(r"""G_{t} = R_t + \gamma R_{t+1} + \gamma^{2} R_{t+2} + \ldots""")
        state_value_eq = MathTex(r"""v_{\pi}(s) = \mathbb{E}_{\pi}[G_{t} \mid s_{t} = s]""")
        action_value_eq = MathTex(r"""q_{\pi}(s, a) = \mathbb{E}_{\pi}[G_{t} \mid s_{t} = s, \; a_{t} = a]""")

        names = VGroup(return_name, state_value, action_value)
        names.arrange(DOWN, aligned_edge=LEFT)

        eqs = VGroup(return_eq, state_value_eq, action_value_eq)
        eqs.arrange(DOWN, aligned_edge=RIGHT).to_edge(RIGHT, buff=1)

        self.play(Write(names))
        self.play(names.animate.to_edge(LEFT, buff=1), Write(eqs))
        self.wait(5)

class ValueIteration(Scene):
    def construct(self):
        title = Title(r"Value Iteration")
        self.play(Write(title))
        
        lines = [
            MathTex(r"\Delta \gets \infty", font_size=36),
            Tex(r"While $\Delta > \theta$", font_size=36),
            Tex(r"For $s \in S$", font_size=36),
            MathTex(r"\Delta \leftarrow 0", font_size=36),
            MathTex(r"v_{\text{prev}} \leftarrow v", font_size=36),
            MathTex(r"v(s) \leftarrow \max_{a \in \mathcal{A}} \left(\mathcal{R}_s^a + \gamma \sum_{s' \in \mathcal{S}} \mathcal{P}_{ss'}^a v_{\text{prev}}(s')\right)", font_size=36),
            MathTex(r"\Delta \gets \max \{ \Delta,\; \lvert v - v_{\text{prev}} \rvert \}", font_size=36),
            Tex(r"end for", font_size=36),
            Tex(r"end while", font_size=36)
        ]
        
        # Group and arrange all lines vertically with left alignment
        algorithm_group = VGroup(*lines).arrange(DOWN, aligned_edge=LEFT).shift(0.5 * DOWN)

        tab_size = 0.7 * RIGHT
        for line in lines[2:8]:
            line.shift(tab_size)
        for line in lines[3:7]:
            line.shift(tab_size)
        
        for i, line in enumerate(lines):
            # The complex math expression (line 6) gets more time
            run_time = 1 if i == 5 else 1
            wait_time = 1.5 if i == 5 else 0.7
            
            self.play(Write(line), run_time=run_time)
            self.wait(wait_time)
        
        # highlight the key part of the algorithm (Bellman equation)
        highlight = SurroundingRectangle(lines[5], buff=0.1, color=YELLOW, stroke_width=3)
        self.play(Create(highlight))
        self.wait(2)


class QLearning(Scene):
    def construct(self):
        title = Title(r"Q-learning")
        self.play(Write(title))
        
        lines = [
            Tex(r"for $i \gets 1$, num episodes do", font_size=32),
            Tex(r"$\varepsilon \gets \varepsilon_1$", font_size=32),
            Tex(r"Observe $S_0$", font_size=32),
            Tex(r"$t \gets 0$", font_size=32),
            Tex(r"repeat", font_size=32),
            Tex(r"Choose action $A_t$ using policy derived from $Q$", font_size=32),
            Tex(r"Take action $A_t$ and observe the reward and state that follows, $R_{t+1}, S_{t+1}$", font_size=32),
            Tex(r"$Q(S_t, A_t) \gets (1 - \alpha) Q(S_t, A_t) + \alpha (R_{t+1} + \gamma \max_{a} Q(S_{t+1}, a))$", font_size=32),
            Tex(r"$t \gets t + 1$", font_size=32),
            Tex(r"until $S_t$ is terminal", font_size=32),
            Tex(r"end for", font_size=32),
            Tex(r"return $Q$", font_size=32)
        ]
        
        # Group and arrange all lines vertically with left alignment
        algorithm_group = VGroup(*lines).arrange(DOWN, aligned_edge=LEFT).shift(0.5 * DOWN)

        tab_size = 0.7 * RIGHT
        for line in lines[1:-3]:
            line.shift(tab_size)
        for line in lines[5:-2]:
            line.shift(tab_size)
        
        # Animate each line appearing
        for i, line in enumerate(lines):
            # The complex math expression (line 6) gets more time
            run_time = 1 if i == 7 else 1
            wait_time = 1.5 if i == 7 else 0.7
            
            self.play(Write(line), run_time=run_time)
            self.wait(wait_time)
        
        # highlight the key part of the algorithm (Bellman equation)
        highlight = SurroundingRectangle(lines[7], buff=0.1, color=YELLOW, stroke_width=3)
        self.play(Create(highlight))
        self.wait(2)
