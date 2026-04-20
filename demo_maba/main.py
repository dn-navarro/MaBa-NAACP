# Demonstração 1: Esboce o gráfico da função f(x) = 2 + sqrt(x - 1) seguindo os passos:
# a) Trace o grafico de g(x) = sqrt(x)
# b) Trace o gráfico de h(x) = sqrt(x-1), explicando como obter o gráfico de h(x) a partir de g(x)
# c) Trace o gráfico de w(x) = 2 + sqrt(x), explicando como obter o gráfico a partir de h(x)
# d) Dê o domínio e imagem da função f(x)

# Roteiro: https://docs.google.com/document/d/1U77Qt5SwEeWQzFfX9puwi3L_G2R3v2gXV3xFKCiyMK8/edit?usp=sharing
# (Acesso somente com credencial USP)

# Criado com <3 em 19 de abril de 2026, por David Navarro - david.navarro@usp.br
# Núcleo Autopoiético de Acolhimento Científico-pedagógico (NAACP), EACH-USP.

from manim import *

# Demonstração comentada (ainda estou fazendo, pessoal)
class demonstracao(Scene):
    def construct(self):
        plano = Axes(x_range=[-5, 5, 1], y_range=[-5, 5, 1])
        labels = plano.get_axis_labels(x_label="x", y_label="y")
        
        grafico_g = plano.plot(lambda x: (x)**(1/2), x_range=[1,5], color = WHITE)
        grafico_w = plano.plot(lambda x: (x)**(1/2) + 2, x_range=[1,5], color = WHITE)
        
        self.add(plano)
        self.play(Create(grafico_g))
        self.wait(2)

# Demonstração para quem tem pressa
class shorts(Scene):
	def construct(self):
		# Funções:
		g_x = lambda x: x**(1/2)
		h_x = lambda x: (x-1)**(1/2)
		f_x = lambda x: (x-1)**(1/2) + 2
		
		# Objetos:
			# Plano cartesiano e rótulos de eixo
		plano = Axes(x_range=[-2,10,1], y_range=[-2,5,1], axis_config={"include_numbers": True, "tip_shape": StealthTip})
		x_rotulo = plano.get_x_axis_label(MathTex("x"), edge=RIGHT, direction=RIGHT)
		y_rotulo = plano.get_y_axis_label(MathTex("y"), edge=UP, direction=UP)
		
			# Gráficos
		g_plot = plano.plot(g_x, x_range=[0,10], color = YELLOW)
		g_plot_copia = g_plot.copy() # ver nota 1
		h_plot = plano.plot(h_x, x_range=[1,10], color = ORANGE)
		f_plot = plano.plot(f_x, x_range=[1,10], color = RED)
		
			# Rótulos (identificam as funções)
		g_label = MathTex("g(x) = \\sqrt{x}").to_corner(DR, buff=1).set_color(YELLOW)
		g_label_copia = g_label.copy()
		h_label = MathTex("h(x) = \\sqrt{x - 1}").to_corner(DR, buff=1).set_color(ORANGE)
		f_label = MathTex("f(x) = \\sqrt{x - 1} + 2").to_corner(DR, buff=1).set_color(RED)
		
		# Animações:
			# Parte 1:
		self.play(Create(plano), Write(x_rotulo), Write(y_rotulo))
		self.play(Create(g_plot), Write(g_label))
		self.wait(3)
		
			# Parte 2: g -> h
		self.play(ReplacementTransform(g_label, h_label))
		self.play(ReplacementTransform(g_plot, h_plot))
		self.wait(3)
		
			# Parte 3: h -> f
		self.play(ReplacementTransform(h_label, f_label))
		self.play(ReplacementTransform(h_plot, f_plot))
		self.wait(3)
		
			# Parte 4: f -> g_copia. Confere um efeito de repetição
		self.play(ReplacementTransform(f_label, g_label_copia))
		self.play(ReplacementTransform(f_plot, g_plot_copia))
		self.wait(3)

# Notas
# 1. Copiei a variável g_plot usando o método copy(). 
# 	Quando fizemos a transformação g_plot -> h_plot, g_plot foi substituido!
