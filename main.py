from manim import *

class SimpleScene(Scene):
    def construct(self):
        logo = SVGMobject("vscode.svg").scale(2)

        text = Text("This is a city", font="0xProto Nerd Font")
        text.next_to(logo, DOWN)

        # Show logo
        self.play(Create(logo), run_time=2)

        # Write text under the logo
        self.play(Write(text), run_time=1.5)
        self.wait(1)

        # Remove both cleanly
        self.play(Unwrite(text), Uncreate(logo), run_time=2)
        self.wait()
