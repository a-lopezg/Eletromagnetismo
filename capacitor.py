from manim import *

class CampoCapacitor(Scene):
    def construct(self):

        #Cria um título para a apresentacao
        titulo = Text("Campo Elétrico Uniforme", font_size=30).to_edge(UP)
        self.play(Write(titulo))

        # Cria as placas paralelas como linhas verticais deslocadas 
        placa_positiva = Line(UP*3, DOWN*3, color=RED, stroke_width=8).shift(LEFT*2)
        placa_negativa = Line(UP*3, DOWN*3, color=BLUE, stroke_width=8).shift(RIGHT*2)

        # Adiciona os sinais de carga usando um loop para distribuir as cargas

        cargas_positivas = VGroup(*[Text("+", color=RED).next_to(placa_positiva, LEFT, buff=0.2).shift(UP*(i*1.2)) for i in range(-2, 3) ])      
        cargas_negativas = VGroup(*[Text("-", color=BLUE).next_to(placa_negativa, RIGHT, buff=0.2).shift(UP*(i*1.2)) for i in range(-2, 3)])

        # Linhas do campo elétrico
        linhas_campo = VGroup()
        # Cria as setas no eixo Y
        posicoes_y = [i * 0.5 for i in range(-5, 6)] 
        
        for y in posicoes_y:
            seta = Arrow(
                start=LEFT*1.9 + UP*y, 
                end=RIGHT*1.9 + UP*y, 
                color=YELLOW, 
                buff=0.1,
                max_tip_length_to_length_ratio=0.15)
            linhas_campo.add(seta)

        # Animação:
        # Faz aparecer as placas
        self.play(Create(placa_positiva), Create(placa_negativa), run_time=1.5)
        self.wait(0.5)
        
        # Faz aparecer as cargas
        self.play(FadeIn(cargas_positivas), FadeIn(cargas_negativas), run_time=1)
        self.wait(0.5)
        
        # Faz as setas aparecerem
        self.play(*[GrowArrow(seta) for seta in linhas_campo], run_time=2)

        self.wait(2)