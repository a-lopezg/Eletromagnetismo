from manim import *
import numpy as np

class CampoFioRetilineo(Scene):
    def construct(self):
        #Titulo e formula
        titulo = Text("Fio Retilíneo", font_size=40).shift(UP * 3.5)
        equacao = MathTex(r"B = \frac{\mu_0 i}{2\pi r}", font_size=48).next_to(titulo, DOWN)
        #Animando o texto
        self.play(Write(titulo))
        self.play(FadeIn(equacao))
        self.wait(1)

        #Criando o fio
        #Criando na forma 2D
        fio_borda = Circle(radius=0.4, color=WHITE, stroke_width=4)
        fio_centro = Dot(radius=0.1, color=YELLOW)
        fio = VGroup(fio_borda, fio_centro)

        #Indicaçao de direçao da corrente
        texto_fio = Text("Corrente (I)\nsaindo da tela", font_size=24, color=YELLOW).next_to(fio, DOWN, buff=0.5)
        self.play(Create(fio_borda), FadeIn(fio_centro), Write(texto_fio))
        self.wait(2)
        self.play(FadeOut(texto_fio))

        #Linhas de campo
        linhas_campo = VGroup()
        vetores_direcao = VGroup()
        raios = [0.8, 1.5, 1.9, 2.5, 3.5, 4.5]
        #Faz diminuir a opacidade na medida que o raio aumenta mostrando que o campo enfraquece
        opacidades = [1.0, 0.9, 0.8, 0.6, 0.3, 0.1] 

        #Juntando cada raio com a opacidade correta
        for raio, opacidade in zip(raios, opacidades):
            circulo = Circle(radius=raio, color=BLUE, stroke_opacity=opacidade)
            linhas_campo.add(circulo)

            #Adicionando setas para mostrar a direçao do campo
            for angulo in [0, PI/2, PI, 3*PI/2]:
                #Encontra a coordenada do circulo
                ponto = circulo.point_at_angle(angulo)
                direcao_tangente = np.array([-ponto[1], ponto[0], 0])
                direcao_tangente = (direcao_tangente / np.linalg.norm(direcao_tangente)) * 0.4
                
                seta = Arrow(start=ponto - direcao_tangente/2, end=ponto + direcao_tangente/2,color=BLUE, buff=0, 
                             stroke_opacity=opacidade,max_tip_length_to_length_ratio=0.3)
                vetores_direcao.add(seta)

        self.play(FadeOut(titulo))
        self.play(equacao.animate.move_to(LEFT * 6 + UP * 3.5))
        self.play(Create(linhas_campo, lag_ratio=0.4), run_time=3)
        self.play(FadeIn(vetores_direcao))
        self.wait(2)

        #Destacando um ponto para mostrar a Distância (r) e o Vetor Tangente (B)
        #Vamos pegar um ponto no segundo círculo (índice 1), no ângulo de 45 graus (PI/4)
        ponto_foco = linhas_campo[4].point_at_angle(PI/4)
        ponto_destaque = Dot(ponto_foco, color=RED)
        
        # Desenhando o raio (r)
        vetor_r = Line(start=ORIGIN, end=ponto_foco, color=WHITE, stroke_width=2)
        texto_r = MathTex("r").next_to(vetor_r.get_center(), UP + LEFT, buff=0.1)

        # Desenhando o vetor B exato neste ponto
        tangente_foco = np.array([-ponto_foco[1], ponto_foco[0], 0])
        tangente_foco = (tangente_foco / np.linalg.norm(tangente_foco)) * 1.5 # Tamanho 1.5 para dar destaque
        
        vetor_b = Arrow(start=ponto_foco, end=ponto_foco + tangente_foco, color=RED, buff=0)
        texto_b = MathTex(r"\vec{B}", color=RED).next_to(vetor_b.get_end(), UP + RIGHT, buff=0.1)

        # Apagamos o texto da mão direita para focar na matemática
        self.play(Create(vetor_r), Write(texto_r), FadeIn(ponto_destaque))
        self.play(GrowArrow(vetor_b), Write(texto_b))

        self.wait(4)