import pygame

#Variaveis em Tupla para os codigos das cores
PRETO = (0,0,0)
BRANCO = (255,255,255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0,0,255)

PI = 3.1416

pygame.init()
janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Free fife RTX")
janela.fill(VERDE)

#Fonte utilizada e tamanho
fonte = pygame.font.Font(None,48)
#Mensagens na Tela
texto = fonte.render('Olá, Mundo', True, BRANCO, AZUL)
#Tamanho e largura do texto
janela.blit(texto, [30, 50])

#Adicinar linha na tela
pygame.draw.line(janela, PRETO, [60, 260], [420, 260], 4)
#Adicionar Poligono
pygame.draw.polygon(janela, VERMELHO, ([191, 206], [236, 277], [156, 277], ),0)
#Adicionar um circulo
pygame.draw.circle(janela, AZUL, (300, 500), 20, 1)
pygame.draw.circle(janela, AZUL, (340, 500), 20, 1)
#Elips - Oval
pygame.draw.ellipse(janela, VERMELHO,(400,250,40,80),1)
#Retangulo
pygame.draw.rect(janela, PRETO,(20,20,60,40,),0)
#Utilizando metodo Arc
pygame.draw.arc(janela, VERMELHO,(250,75,150,125),PI/2,3*PI,2)
pygame.draw.arc(janela, PRETO,(250,75,150,125),-PI/2,PI/2,  2)
pygame.display.update()







deve_continuar = True
while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False
pygame.quit()