from manim import *
import numpy as np

class CampoCargaPontual(Scene):
    def construct(self):
        # Título
        titulo = Text("Campo elétrico de uma carga pontual", font_size=30).shift(UP * 3.5)
        
        # Equação do campo eletrico
        equacao = MathTex(r"\vec{E} = \frac{1}{4 \pi \epsilon_0}\frac{q}{r^2} \hat{r}", font_size=48).next_to(titulo, DOWN, buff=0.5)
        
        self.play(Write(titulo))
        self.play(FadeIn(equacao))
        self.wait(2)
        
        # Move a equação
        self.play(equacao.animate.move_to(RIGHT * 4 + UP * 2))

        # 2. Criando a Carga Positiva
        carga_pos = Circle(radius=0.4, color=RED, fill_opacity=1)
        sinal_pos = Text("+", color=WHITE, font_size=36).move_to(carga_pos.get_center())
        # Agrupa a carga e o sinal
        grupo_pos = VGroup(carga_pos, sinal_pos) 
        
        texto_pos = Text("Carga positiva", font_size=28).to_edge(DOWN)

        self.play(FadeIn(grupo_pos), Write(texto_pos))

        # Cria as setas para carga positiva
        setas_saindo = VGroup()
        
        #  Loop de 0 a 360 graus para cobrir a carga de setas
        for ang in range(0, 360, 30):
            rad = ang * DEGREES # converte para radianos
            inicio = np.array([0.6 * np.cos(rad), 0.6 * np.sin(rad), 0])
            fim = np.array([3.0 * np.cos(rad), 3.0 * np.sin(rad), 0])
            seta = Arrow(start=inicio, end=fim, color=YELLOW, buff=0)
            setas_saindo.add(seta)

        # Animação das setas aparecendo em conjunto a partir da carga
        self.play(*[GrowArrow(s) for s in setas_saindo], run_time=2)
        self.wait(2)

        #Construção da carga negativa para a segunda parte da animação
        carga_neg = Circle(radius=0.4, color=BLUE, fill_opacity=1)
        sinal_neg = Text("-", color=WHITE, font_size=48).move_to(carga_neg.get_center())
        grupo_neg = VGroup(carga_neg, sinal_neg)
        
        texto_neg = Text("Carga negativa", font_size=28).to_edge(DOWN)

        #Cria as setas da carga negativa
        setas_entrando = VGroup()
        for angulo in range(0, 360, 30):
            rad = angulo * DEGREES
            #Para o caso da carga negativa vamos fazer a seta crescer de um raio maior em direção a carga
            inicio = np.array([3.0 * np.cos(rad), 3.0 * np.sin(rad), 0])
            fim = np.array([0.6 * np.cos(rad), 0.6 * np.sin(rad), 0])          
            seta = Arrow(start=inicio, end=fim, color=YELLOW, buff=0)
            setas_entrando.add(seta)

        #Transição:
        self.play(FadeOut(setas_saindo), FadeOut(texto_pos))
        
        #Fade entre a carga positiva com a negativa
        self.play(Transform(grupo_pos, grupo_neg), Write(texto_neg))
        
        #Animaçao das setas da carga negativa
        self.play(*[GrowArrow(s) for s in setas_entrando], run_time=2)
        self.wait(3)
