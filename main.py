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
            Tex(r"\textbf{while} $\Delta > \theta$ \textbf{do}", font_size=36),
            Tex(r"\textbf{for} $s \in S$ \textbf{do}", font_size=36),
            MathTex(r"\Delta \leftarrow 0", font_size=36),
            MathTex(r"v_{\text{prev}} \leftarrow v", font_size=36),
            MathTex(r"v(s) \leftarrow \max_{a \in \mathcal{A}} \left(\mathcal{R}_s^a + \gamma \sum_{s' \in \mathcal{S}} \mathcal{P}_{ss'}^a v_{\text{prev}}(s')\right)", font_size=36),
            MathTex(r"\Delta \gets \max \{ \Delta,\; \lvert v - v_{\text{prev}} \rvert \}", font_size=36),
            Tex(r"\textbf{end} \textbf{for}", font_size=36),
            Tex(r"\textbf{end} \textbf{while}", font_size=36),
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
            Tex(r"\textbf{for} $i \gets 1$, num episodes \textbf{do}", font_size=32),
            Tex(r"$\varepsilon \gets \varepsilon_1$", font_size=32),
            Tex(r"Observe $S_0$", font_size=32),
            Tex(r"$t \gets 0$", font_size=32),
            Tex(r"\textbf{repeat}", font_size=32),
            Tex(r"Choose action $A_t$ using policy derived from $Q$", font_size=32),
            Tex(r"Take action $A_t$ and observe the reward and state that follows, $R_{t+1}, S_{t+1}$", font_size=32),
            Tex(r"$Q(S_t, A_t) \gets (1 - \alpha) Q(S_t, A_t) + \alpha (R_{t+1} + \gamma \max_{a} Q(S_{t+1}, a))$", font_size=32),
            Tex(r"$t \gets t + 1$", font_size=32),
            Tex(r"\textbf{until} $S_t$ is terminal", font_size=32),
            Tex(r"\textbf{end} \textbf{for}", font_size=32),
            Tex(r"\textbf{return} $Q$", font_size=32)
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


class VennDiagram(Scene):
    def construct(self):
        # Create circles for the Venn diagram
        circle_A = Circle(radius=2, color=BLUE).shift(LEFT)
        circle_B = Circle(radius=2, color=GREEN).shift(RIGHT)

        # Add labels for the sets
        label_A = Text("Value function", color=BLUE, font_size=32).next_to(circle_A, LEFT).shift(2 * UP + 0.5 * RIGHT)
        label_B = Text("Policy", color=GREEN, font_size=32).next_to(circle_B, RIGHT).shift(2 * UP + 0.5 * LEFT)

        # Add text for the regions
        text_A_minus_B = Text("Value based", font_size=24).move_to(circle_A.get_center() + UP * 0.5 + 0.5 * LEFT)
        text_B_minus_A = Text("Policy based", font_size=24).move_to(circle_B.get_center() + UP * 0.5 + 0.5 * RIGHT)
        text_A_and_B = Text("Actor Critic", color=YELLOW, font_size=24).move_to((circle_A.get_center() + circle_B.get_center()) / 2)

        # Adjust positions for better overlap representation
        text_A_minus_B.shift(LEFT * 0.5)
        text_B_minus_A.shift(RIGHT * 0.5)

        venn_diagram = VGroup(circle_A, circle_B, label_A, label_B, text_A_minus_B, text_B_minus_A, text_A_and_B)

        bullet_list = VGroup(*[
            Text("Value based", font_size=24),
            Text("Learnt value function", font_size=24),
            Text("Implicit policy", font_size=24),
            Text("Policy based", font_size=24),
            Text("No value function", font_size=24),
            Text("Learnt policy", font_size=24),
            Text("Actor-Critic", font_size=24),
            Text("Learnt value function", font_size=24),
            Text("Learnt policy", font_size=24),
        ]).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT, buff=1)

        for i in [0, 3, 6]:
            bullet_list[i].shift(0.5 * LEFT)

        # Add all elements to the scene
        self.play(Create(circle_A), Create(circle_B))
        self.play(Write(label_A), Write(label_B))
        self.play(Write(text_A_minus_B), Write(text_B_minus_A), Write(text_A_and_B))
        self.play(venn_diagram.animate.to_edge(RIGHT, buff=0.5), Write(bullet_list))
        self.wait(5)


class ObjectiveFunctions(Scene):
    def construct(self):
        title = Title("Objective functions")
        self.play(Write(title))
        return_name = Text("Episodic")
        state_value = Text("Continuing")
        action_value = Text("Continuing")

        return_eq = MathTex(r""" J_1(\theta)=V^{\pi_\theta}\left(s_1\right)=\mathbb{E}_{\pi_\theta}\left[v_1\right] """)
        state_value_eq = MathTex(r""" J_{a v V}(\theta)=\sum_s d^{\pi_\theta}(s) V^{\pi_\theta}(s) """)
        action_value_eq = MathTex(r""" J_{a v R}(\theta)=\sum_s d^{\pi_\theta}(s) \sum_a \pi_\theta(s, a) \mathcal{R}_s^a """)

        names = VGroup(return_name, state_value, action_value)
        names.arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        eqs = VGroup(return_eq, state_value_eq, action_value_eq)
        eqs.arrange(DOWN, aligned_edge=RIGHT, buff=0.5).to_edge(RIGHT, buff=1)

        self.play(Write(names))
        self.play(names.animate.to_edge(LEFT, buff=1), Write(eqs))
        self.wait(5)

class PolicyGradientTheorem(Scene):
    def construct(self):
        title = Title("Policy gradient theorem")
        self.play(Write(title))

        text1 = Tex(r"For any differentiable policy $\pi_{\theta}$, for any policy objective function $J$, the policy gradient is the following:", font_size=36)
        eq = MathTex(r"\nabla_{\theta}J(\theta) = \mathbb{E}_{\pi_{\theta}} [\nabla_{\theta}\log \pi_{\theta}(s, a) \cdot Q^{\pi_{\theta}}(s, a)]", font_size=36)
        text2 = Tex(r"where $Q^{\pi_{\theta}}(s, a)$ is the long-term value of a state action pair.", font_size=36)
        thm = VGroup(text1, eq, text2).arrange(DOWN, aligned_edge=LEFT, buff=1)
        eq.shift(3 * RIGHT)

        self.play(Write(thm))
        self.wait(2)
        highlight = SurroundingRectangle(eq, buff=0.1, color=YELLOW, stroke_width=3)
        self.play(Create(highlight))
        self.wait(5)


class BaselineFunction(Scene):
    def construct(self):
        title = Title("Baseline function")
        self.play(Write(title))

        text1 = Tex(r"We can reduce variance by introducing a \textbf{baseline} function $B(s)$", font_size=36)
        eq = MathTex(r"\nabla_{\theta}J(\theta) = \mathbb{E}_{\pi_{\theta}} [\nabla_{\theta}\log \pi_{\theta}(s, a) \cdot (Q^{\pi_{\theta}}(s, a) - B(s))]", font_size=36)
        text2 = Tex(r"A good choice for the baseline function is the value function $B(s) = V^{\pi_{\theta}}(s)$", font_size=36)

        texts = VGroup(text1, eq, text2).arrange(DOWN, aligned_edge=LEFT, buff=1)
        eq.shift(2 * RIGHT)
        self.play(Write(texts))
        self.wait(5)


class AdvantageFunction(Scene):
    def construct(self):
        title = Title("Advantage function")
        self.play(Write(title))

        text1 = Tex(r"We call the following the \textbf{advantage function}:", font_size=36)
        eq1 = MathTex(r"A^{\pi_{\theta}}(s, a) = Q^{\pi_{\theta}}(s, a) - V^{\pi_{\theta}}(s)", font_size=36)
        text2 = Tex(r"The policy gradient theorem with the advantage function:", font_size=36)
        eq2 = MathTex(r"\nabla_{\theta}J(\theta) = \mathbb{E}_{\pi_{\theta}} [\nabla_{\theta}\log \pi_{\theta}(s, a) \cdot A^{\pi_{\theta}}(s, a)]", font_size=36)

        texts = VGroup(text1, eq1, text2, eq2).arrange(DOWN, aligned_edge=LEFT, buff=1)
        eq1.shift(2 * RIGHT)
        eq2.shift(1.5 * RIGHT)
        self.play(Write(texts))
        self.wait(5)

class EstimatingAdvantage(Scene):
    def construct(self):
        title = Title("Estimating the advantage function")
        self.play(Write(title))

        text1 = Tex(r"By the Bellman expectation equation, we can rewrite $Q$:", font_size=36)
        eq1 = MathTex(r"Q^{\pi_{\theta}}(s, a) = \mathbb{E}[G_{t} \mid s, a] = \mathbb{E}_{\pi_{\theta}} [r + \gamma V^{\pi_{\theta}}(s') \mid s, a]", font_size=36)
        eq2 = MathTex(r"A^{\pi_{\theta}}(s, a) = \mathbb{E}_{\pi_{\theta}} [r + \gamma V^{\pi_{\theta}}(s') \mid s, a] - V^{\pi_{\theta}}(s)", font_size=36)
        text2 = Tex(r"The \textbf{TD Error} represents the error of a single step:", font_size=36)
        eq3 = MathTex(r"\delta ^{\pi_{\theta}} = r + \gamma V^{\pi_{\theta}}(s') - V^{\pi_{\theta}}(s)", font_size=36)
        eq4 = MathTex(r"\mathbb{E}_{\pi_{\theta}}[\delta ^{\pi_{\theta}} \mid s, a] = A^{\pi_{\theta}}(s, a)", font_size=36)
        text3 = Tex(r"The TD Error is an unbiased estimator of the advantage function.", font_size=36)

        texts = VGroup(text1, eq1, eq2, text2, eq3, eq4, text3).arrange(DOWN, aligned_edge=LEFT)
        eq1.shift(1.5 * RIGHT)
        eq2.shift(1.5 * RIGHT)
        eq3.shift(2 * RIGHT)
        eq4.shift(2 * RIGHT)
        self.play(Write(texts))
        self.wait(5)

class GAE(Scene):
    def construct(self):
        title = Title("Generalized Advantage Estimator (GAE)")
        self.play(Write(title))

        text1 = Tex(r"A single step TD Error may result in high bias, thus we introduce the following:", font_size=36)
        eq1 = MathTex(r"A^{(k)}_{t} = \sum_{m=0} ^{k-1} \gamma ^{m} \delta ^{\pi_{\theta}}_{t+1} = -V^{\pi_{\theta}}(s_{t}) + r_{t} + \gamma r_{t+1} + \gamma ^{2}r_{t+2} + \dots + \gamma ^{k}V^{\pi_{\theta}}(s_{t+k})", font_size=36)
        text2 = Tex(r"As $k$ increases, the bias decreases, but the variance increases.", font_size=36)
        text3 = Tex(r"\textbf{GAE} is the exponentially weightet sum of these estimates:", font_size=36)
        eq2 = MathTex(r"A^{\text{GAE}}_{t} = (1 - \lambda)\left(A^{(1)}_{t} + \lambda A^{(2)}_{t} + \lambda ^{2}A^{(3)}_{t} + \dots\right)", font_size=36)

        texts = VGroup(text1, eq1, text2, text3, eq2).arrange(DOWN, aligned_edge=LEFT)
        eq2.shift(1.5 * RIGHT)
        self.play(Write(texts))
        self.wait(5)

class ClippedSurrogate(Scene):
    def construct(self):
        title = Title("Clipped surrogate objective")
        self.play(Write(title))

        image = ImageMobject("images/clipped_loss.jpg")
        image.set(width=8)
        image.shift(DOWN)

        eq = MathTex(r"L^{\text{CLIP}}(\theta)=\hat{\mathbb{E}}_t\left[\min \left(r_t(\theta) \hat{A}_t, \operatorname{clip}\left(r_t(\theta), 1-\epsilon, 1+\epsilon\right) \hat{A}_t\right)\right]", font_size=36)

        self.play(Write(eq))
        self.wait(2)
        self.play(eq.animate.shift(2 * UP), FadeIn(image))
        self.wait(5)

class PPO(Scene):
    def construct(self):
        title = Title(r"Proximal Policy Optimization (PPO)")
        self.play(Write(title))
        
        lines = [
            Tex(r"\textbf{for} iteration $=1, 2, \ldots$ \textbf{do}", font_size=36),
            Tex(r"\textbf{for} actor $=1, 2, \ldots, N$ \textbf{do}", font_size=36),
            Tex(r"Run policy $\pi_{\theta_{\text{old}}}$ in environment for $T$ timesteps", font_size=36),
            Tex(r"Compute advantage estimates $A_1, \ldots, A_T$", font_size=36),
            Tex(r"\textbf{end} \textbf{for}", font_size=36),
            Tex(r"Optimize surrogate $L$ wrt $\theta$, with $K$ epochs and minibatch size $M \le NT$", font_size=36),
            Tex(r"$\theta_{\text{old}} \gets \theta$", font_size=36),
            Tex(r"\textbf{end} \textbf{for}", font_size=36),
        ]
        
        algorithm_group = VGroup(*lines).arrange(DOWN, aligned_edge=LEFT).shift(0.5 * DOWN)

        tab_size = 0.7 * RIGHT
        for line in lines[1:-1]:
            line.shift(tab_size)
        for line in lines[2:4]:
            line.shift(tab_size)
        
        for i, line in enumerate(lines):
            self.play(Write(line), run_time=1)
            self.wait(1)

class PPOBehemoth(Scene):
    def construct(self):
        image = ImageMobject("images/behemoth_ppo.jpg")
        image.set(width=13)
        image.shift(5 * DOWN)

        self.add(image)
        self.wait(2)
        self.play(image.animate.shift(10 * UP), run_time=20)
