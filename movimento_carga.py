from manim import *
import numpy as np

class CampoMagnetico(Scene):
    def construct(self):
        # Cria o titulo do video
        titulo = Text("Carga em um campo magnético uniforme", font_size=30).shift(UP * 3.5)
        self.play(Write(titulo))

        #Adicionando os Eixos Cartesianos
        eixos = Axes(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            x_length=12,
            y_length=6,
            axis_config={"color": DARK_GREY, "stroke_width": 1}).shift(DOWN * 0.3)
        
        # Pegamos o final do eixo Y (a seta de cima) e colocamos o texto à esquerda (LEFT)
        label_x = MathTex("x").next_to(eixos.x_axis.get_end(), DOWN)
        label_y = MathTex("y").next_to(eixos.y_axis.get_end(), LEFT)
        labels = VGroup(label_x, label_y)



        #Texto direção do campo
        info_campo = VGroup(
            Text("Campo Magnético ", font_size=24, color=BLUE),
            MathTex(r"\vec{B} = B \hat{z}", color=BLUE, font_size=30)).arrange(DOWN).shift(RIGHT * 5).shift(UP * 1.5)
        
        self.play(Write(info_campo))
        self.play(Create(eixos), Write(labels), run_time=2)

        #Cria o campo magnético
        campo_b = VGroup()
        for x in np.arange(0.5, 6.5, 1):
            for y in np.arange(-3, 4, 1):
                if x >= 4 and y >= 2:
                    continue
                marca_b = MathTex(r"\otimes", color=BLUE, font_size=36).move_to(eixos.c2p(x, y))
                campo_b.add(marca_b)
        
        self.play(FadeIn(campo_b, lag_ratio=0.1), run_time=2)

        #Texto carga do campo
        info_carga = Text("Carga positiva (+)", color=YELLOW, font_size=28).to_corner(UL).shift(DOWN * 0.5)

        #Cria a partícula e o rastro da trajetoria
        carga = Dot(color=RED, radius=0.15)
        sinal = Text("+", color=WHITE, font_size=20).move_to(carga.get_center())
        particula = VGroup(carga, sinal).move_to(eixos.c2p(-5, 0))
        rastro = TracedPath(particula.get_center, stroke_width=6, stroke_color=YELLOW, dissipating_time=0.6)

        self.play(Write(info_carga), FadeIn(particula))
        self.wait(2)
        self.add(rastro)

        #Movimento da particula:
        #Movimento retilineo uniforme antes do campo magnetico
        self.play(particula.animate.move_to(eixos.c2p(1, 0)), run_time=2, rate_func=linear)

        #Movimento circular uniforme dentro do campo
        centro_curva = eixos.c2p(1, 1.5)
        self.play(Rotate(particula,angle=PI, about_point=centro_curva,rate_func=linear),run_time=2.5)

        #A particula sai do campo
        self.play(particula.animate.move_to(eixos.c2p(-5, 3)), run_time=2, rate_func=linear)

        self.play(FadeOut(particula), FadeOut(info_carga))

        #Criando a carga negativa e o texto
        texto_neg = Text("Carga negativa (-)", color=YELLOW, font_size=28).to_corner(UL).shift(DOWN * 0.5)
        
        carga_neg = Dot(color=YELLOW, radius=0.15)
        sinal_neg = Text("-", color=BLACK, font_size=28).move_to(carga_neg.get_center())
        
        particula_neg = VGroup(carga_neg, sinal_neg).move_to(eixos.c2p(-5, 0))
        rastro_neg = TracedPath(particula_neg.get_center, stroke_width=6, stroke_color=YELLOW, dissipating_time=0.6)
        
        self.play(Write(texto_neg), FadeIn(particula_neg))
        self.wait(2)
        self.add(rastro_neg)

        #Movimento da particula:
        #Movimento retilineo uniforme antes do campo magnetico
        self.play(particula_neg.animate.move_to(eixos.c2p(1, 0)), run_time=2, rate_func=linear)

        #Movimento circular uniforme dentro do campo
        centro_curva_neg = eixos.c2p(1, -1.5)
        #rotação no sentido horário
        self.play(Rotate(particula_neg, angle=-PI, about_point=centro_curva_neg, rate_func=linear), run_time=2.5)

        ##A particula sai do campo
        self.play(particula_neg.animate.move_to(eixos.c2p(-5, -3)), run_time=2, rate_func=linear)

        self.wait(1)