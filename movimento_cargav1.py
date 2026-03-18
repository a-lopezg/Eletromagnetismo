from manim import *
import numpy as np

class ParticulaCampoMagnetico(Scene):
    def construct(self):
        # Cria o titulo do video
        titulo = Text("Movimento de uma garga em um campo magnético uniforme", font_size=30).to_edge(UP)
        self.play(Write(titulo))

        # Cria o vetor do campo magnetico:
        # Preenche o lado direito da tela com vetores entrando na tela
        campo_b = VGroup()
        for x in np.arange(0.5, 6.5, 1):
            for y in np.arange(-3, 3, 1):
                x_mark = Text("x", color=BLUE, font_size=24).move_to(RIGHT * x + UP * y)
                campo_b.add(x_mark)
        
        # Animação da grade
        self.play(FadeIn(campo_b, lag_ratio=0.1), run_time=2)

        # Carga possitiva e trajetória:

        carga = Dot(color=RED, radius=0.15)
        sinal = Text("+", color = WHITE, font_size=20).move_to(carga.get_center())
        particula = VGroup(carga, sinal).move_to(LEFT * 4 + DOWN * 1.5)

        # usando o comando TracedPath faz um rastro da trajetória feita pela carga positiva
        rastro = TracedPath(particula.get_center, stroke_width=4, stroke_color=WHITE)
        self.add(rastro)

        self.play(FadeIn(particula))

        #Movimento da particula:
        #Movimento retilineo uniforme antes do campo magnetico
        self.play(
            particula.animate.move_to(RIGHT * 0.5 + DOWN * 1.5), run_time=2, rate_func=linear)

        #Movimento Circular Uniforme dentro do campo
        centro_curva = RIGHT * 0.5 + UP * 0     
        self.play(
            Rotate(particula, angle=PI, # faz girar exatos 180 graus
                about_point=centro_curva,
                rate_func=linear), run_time=2)

        #A particula sai do campo
        self.play(particula.animate.move_to(LEFT * 4 + UP * 1.5), run_time=2,  rate_func=linear)

        # Pausa dramática para o aluno apreciar a trajetória
        self.wait(3)