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
		# Configura para celular na vertical -> mudamos de 16:9 para 9:16
		self.camera.frame_width = 9		# largura - horizontal
		self.camera.frame_height = 16	# comprimento - vertical
		
		# Funções:
		g_x = lambda x: x**(1/2)
		h_x = lambda x: (x-1)**(1/2)
		f_x = lambda x: (x-1)**(1/2) + 2
		
		# Objetos:
			# Plano cartesiano e rótulos de eixo
		plano = Axes(x_range=[-2,10,1], 
			y_range=[-2,5,1], 
			x_length=7,
			y_length=4,
			axis_config={"include_numbers": True, "tip_shape": StealthTip, "font_size":24})
		plano.shift(DOWN)
		
		x_rotulo = plano.get_x_axis_label(MathTex("x"), edge=RIGHT, direction=RIGHT)
		y_rotulo = plano.get_y_axis_label(MathTex("y"), edge=UP, direction=UP)
		
			# Gráficos
		g_plot = plano.plot(g_x, x_range=[0,10], color = YELLOW)
		g_plot_copia = g_plot.copy() # ver nota 1
		h_plot = plano.plot(h_x, x_range=[1,10], color = ORANGE)
		f_plot = plano.plot(f_x, x_range=[1,10], color = RED)
		
			# Pontos e retas no plano
		g_dot = Dot(plano.coords_to_point(0,0), color=YELLOW)
		g_dot_copia = g_dot.copy()
		h_dot = Dot(plano.coords_to_point(1,0), color=ORANGE)
		f_dot = Dot(plano.coords_to_point(1,2), color=RED)
		
		coordenadas00 = plano.get_lines_to_point(plano.coords_to_point(0,0))
		coordenadas10 = plano.get_lines_to_point(plano.coords_to_point(1,0))
		coordenadas12 = plano.get_lines_to_point(plano.coords_to_point(1,2))
		
			# Rótulos (identificam as funções)
		g_label = MathTex("g(x) = \\sqrt{x}").set_color(YELLOW)
		g_label_copia = g_label.copy()
		h_label = MathTex("h(x) = \\sqrt{x - 1}").set_color(ORANGE)
		f_label = MathTex("f(x) = \\sqrt{x - 1} + 2").set_color(RED)
		
			# Domínio (d_[funcao]) e Imagem (im_[funcao])
		d_g = MathTex("D_g = \\left\\{ x \\in \\mathbb{R} \\, : \\, x \\geq 0 \\right\\}").set_color(YELLOW)
		im_g = MathTex("Im_g = \\left\\{ y \\in \\mathbb{R} \\, : \\, y \\geq 0 \\right\\}").set_color(YELLOW)
		d_g_copia = d_g.copy()
		im_g_copia = im_g.copy()
		d_h = MathTex("D_h = \\left\\{ x \\in \\mathbb{R} \\, : \\, x \\geq 1 \\right\\}").set_color(ORANGE)
		im_h = MathTex("Im_h = \\left\\{ y \\in \\mathbb{R} \\, : \\, y \\geq 0 \\right\\}").set_color(ORANGE)
		d_f = MathTex("D_f = \\left\\{ x \\in \\mathbb{R} \\, : \\, x \\geq 1 \\right\\}").set_color(RED)
		im_f = MathTex("Im_f = \\left\\{ y \\in \\mathbb{R} \\, : \\, y \\geq 2 \\right\\}").set_color(RED)
		
			# Agrupamentos: gráficos, pontos ; rótulos, domínios e imagens das funções
		g_grafico = VGroup(g_plot, g_dot, coordenadas00)
		g_grafico_copia = g_grafico.copy()
		h_grafico = VGroup(h_plot, h_dot, coordenadas10)
		f_grafico = VGroup(f_plot, f_dot, coordenadas12)
		
		g_texto = VGroup(g_label, d_g, im_g).arrange(DOWN).to_edge(UP, buff=1).scale(0.7)
		g_texto_copia = g_texto.copy()
		h_texto = VGroup(h_label, d_h, im_h).arrange(DOWN).to_edge(UP, buff=1).scale(0.7)
		f_texto = VGroup(f_label, d_f, im_f).arrange(DOWN).to_edge(UP, buff=1).scale(0.7)

		# Animações:
			# Parte 1:
		self.play(Create(plano), Write(x_rotulo), Write(y_rotulo))
		self.play(Create(g_grafico), Write(g_texto))
		self.wait(3)
		
			# Parte 2: g -> h
		self.play(ReplacementTransform(g_texto, h_texto))
		self.play(ReplacementTransform(g_grafico, h_grafico))
		self.wait(3)
		
			# Parte 3: h -> f
		self.play(ReplacementTransform(h_texto, f_texto))
		self.play(ReplacementTransform(h_grafico, f_grafico))
		self.wait(3)
		
			# Parte 4: f -> g_copia. Confere um efeito de repetição
		self.play(ReplacementTransform(f_texto, g_texto_copia))
		self.play(ReplacementTransform(f_grafico, g_grafico_copia))
		self.wait(3)


# Notas
# 1. Copiei a variável g_plot usando o método copy(). 
# 	Quando fizemos a transformação g_plot -> h_plot, g_plot foi substituido!
#	Ainda não descobri um jeito mais simples, rápido e econômico de resolver :-P
