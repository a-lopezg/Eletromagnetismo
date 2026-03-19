from manim import *
import numpy as np

class CampoFioCompleto(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0, theta=-PI/2)
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
        self.play(equacao.animate.move_to(LEFT * 5.5 + UP * 3.5)) 
        self.play(Create(linhas_campo, lag_ratio=0.4), run_time=3)
        self.play(FadeIn(vetores_direcao))
        self.wait(2)

        #Destacando um ponto para mostrar a o raio r e o vetor do campo
        ponto_foco = linhas_campo[4].point_at_angle(PI/4)
        ponto_destaque = Dot(ponto_foco, color=RED)
        
        #Cria o vetor raio
        vetor_r = Line(start=ORIGIN, end=ponto_foco, color=WHITE, stroke_width=2)
        texto_r = MathTex("r").next_to(vetor_r.get_center(), UP + LEFT, buff=0.1)

        #Cria o vetor B em um ponto no circulo
        tangente_foco = np.array([-ponto_foco[1], ponto_foco[0], 0])
        tangente_foco = (tangente_foco / np.linalg.norm(tangente_foco)) * 1.5 
        
        vetor_b = Arrow(start=ponto_foco, end=ponto_foco + tangente_foco, color=RED, buff=0)
        texto_b = MathTex(r"\vec{B}", color=RED).next_to(vetor_b.get_end(), UP + RIGHT, buff=0.1)

        #Anima a indicação do raio e direção do campo magnetico
        self.play(Create(vetor_r), Write(texto_r), FadeIn(ponto_destaque))
        self.play(GrowArrow(vetor_b), Write(texto_b))
        self.wait(3)
        
        #transiçao
        objetos_para_apagar = [mob for mob in self.mobjects if mob != equacao]
        self.play(*[FadeOut(mob) for mob in objetos_para_apagar], run_time=1.5)

        # Parte 3D
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        self.add_fixed_in_frame_mobjects(equacao)

        #Cria o texto de mudança de dimensão
        titulo_3d = Text("Visão 3D", font_size=40, color=YELLOW)
        self.add_fixed_in_frame_mobjects(titulo_3d) 
        self.play(Write(titulo_3d))
        self.wait(1)
        self.play(titulo_3d.animate.to_corner(UR), run_time=1)
        texto_canto = Text("(3D)", font_size=28, color=YELLOW).to_corner(UR)
        self.add_fixed_in_frame_mobjects(texto_canto) 
        self.play(Transform(titulo_3d, texto_canto), run_time=0.5)


        #Criando o fio longo
        fio_3d = Cylinder(radius=0.1, height=12, color=YELLOW, fill_opacity=0.8)
        fio_3d.rotate(PI/2, axis=UP) 
        self.play(Create(fio_3d), run_time=1.5)

        #Vetor indicando a direçao da corrente
        seta_corrente = Arrow(start=LEFT*2 + UP*0.6 + OUT*0.6, end=RIGHT*2 + UP*0.6 + OUT*0.6, color=YELLOW, stroke_width=6)
        texto_corrente_fixo = MathTex("I", color=YELLOW, font_size=40).to_edge(DOWN).shift(UP)
        texto_legenda_i = Text("Sentido da corrente", font_size=24, color=YELLOW).next_to(texto_corrente_fixo, DOWN)
    
        self.add_fixed_in_frame_mobjects(texto_corrente_fixo, texto_legenda_i)
        self.play(GrowArrow(seta_corrente), Write(texto_corrente_fixo), Write(texto_legenda_i))
        self.wait(1.5)
        self.play(FadeOut(seta_corrente), FadeOut(texto_corrente_fixo), FadeOut(texto_legenda_i))


        #Cria as linhas do campo magnético
        linhas_campo_3d = VGroup()
        raios_3d = raios[:4] 
        opacidades_3d = opacidades[:4]
        posicoes_x = [-4, -2, 0, 2, 4]

        for x in posicoes_x:
            plano_de_circulos = VGroup() 
            
            for raio, opacidade in zip(raios_3d, opacidades_3d):
                circulo = Circle(radius=raio, color=RED, stroke_opacity=opacidade)
                
                setas_3d = VGroup()
                for angulo in [0, PI/2, PI, 3*PI/2]:
                    ponto = circulo.point_at_angle(angulo)
                    direcao_tangente = np.array([-ponto[1], ponto[0], 0])
                    direcao_tangente = (direcao_tangente / np.linalg.norm(direcao_tangente)) * 0.4
                    
                    seta = Arrow(start=ponto - direcao_tangente/2, end=ponto + direcao_tangente/2,
                                 color=RED, buff=0, stroke_opacity=opacidade, max_tip_length_to_length_ratio=0.3)
                    setas_3d.add(seta)
        
                campo_loop = VGroup(circulo, setas_3d)
                campo_loop.rotate(PI/2, axis=UP)
                campo_loop.shift(RIGHT * x)
                plano_de_circulos.add(campo_loop)
            linhas_campo_3d.add(plano_de_circulos)

        #Faz a animaçao das linhas do campo, aparecendo de forma sincronizada.
        self.play(*[Create(plano, lag_ratio=0.1) for plano in linhas_campo_3d], run_time=4.5)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(2)