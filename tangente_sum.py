from manim import *

class Tangente(Scene):
    def construct(self):
        title = Text('Demonstração Tangente da Soma', font_size = 50, font = 'Arial', color = YELLOW) #MathTex é para LaTeX e Text para texto
        instagram = Text('@motaax._', font_size = 30, fill_opacity = 0.5)
        instagram.shift(6 * UP)
        self.play(Write(title), Write(instagram))
        self.wait()

        self.play(FadeOut(title))

        def equations_sequence(initial, equations):
            self.play(Write(initial))
            self.wait()
            for step in equations:
                if step == equations[0]:
                    current_step = equations[0]
                    self.play(ReplacementTransform(initial, equations[0]))
                    self.wait(3)
                else:
                    self.play(ReplacementTransform(current_step, step))
                    self.wait(3)
                    current_step = step
            self.play(Circumscribe(equations[-1]), buff = 1.5) #Desenha um retângulo amarelo na última equação

        equation = MathTex(r'\tan(\alpha + \beta) = \frac{\tan(\alpha + \beta)}{1 - \tan \alpha \cdot \tan \beta}')
        step1 = MathTex(r'\frac{\sin(\alpha + \beta)}{\cos(\alpha + \beta)')
        step2 = MathTex(r'\frac{\sin \alpha \cdot \cos \beta + \sin \beta \cdot \cos \alpha}{\cos \alpha \cdot \cos \beta - \sin \alpha \cdot \sin \beta}}')
        step3 = MathTex(r'\frac{\sin \alpha \cos \beta + \sin \beta \cdot \cos \alpha}{\cos \alpha \cdot \cos \beta} \div \frac{\cos \alpha \cdot \cos \beta - \sin \alpha \cdot \sin \beta}{\cos \alpha \cdot \cos \beta}')
        step4 = MathTex(r'\tan(\alpha + \beta) = \frac{\tan \alpha + \tan \beta}{1 - \tan \alpha \cdot \tan \beta}')

        equations = [step1, step2, step3, step4]

        equations_sequence(equation, equations)

        self.wait()
        self.play(FadeOut(step4))
        self.play(FadeOut(instagram))