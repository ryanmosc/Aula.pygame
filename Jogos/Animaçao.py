import pygame

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

LARGURAJANELA = 800
ALTURAJANELA = 700

def mover(figura, dimensao_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dimensao_janela[0]
    borda_inferior = dimensao_janela[1]
    
    if figura['objRect'].top < borda_superior or figura['objRect'].bottom > borda_inferior:
        figura['vel'][1] = -figura['vel'][1]
    if figura['objRect'].left < borda_esquerda or figura['objRect'].right > borda_direita:
        figura['vel'][0] = -figura['vel'][0]
    
    figura['objRect'].x += figura['vel'][0]
    figura['objRect'].y += figura['vel'][1]

pygame.init()
relogio = pygame.time.Clock()

janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Colisão")

b1 = {"objRect": pygame.Rect(300, 80, 40, 80), "cor": VERMELHO, "vel": [0, -5], "forma": "ELIPSE"}
b2 = {"objRect": pygame.Rect(200, 200, 20, 20), "cor": VERDE, "vel": [5, 5], "forma": "ELIPSE"}
b3 = {"objRect": pygame.Rect(100, 150, 60, 60), "cor": AZUL, "vel": [-5, 5], "forma": "RETANGULO"}
b4 = {"objRect": pygame.Rect(200, 150, 80, 40), "cor": AMARELO, "vel": [5, 0], "forma": "RETANGULO"}
blocos = [b1, b2, b3, b4]

bola = {"objRect": pygame.Rect(300, 330, 30, 30), "cor": BRANCO, "vel": [3, 3], "forma": "BOLA"}

deve_continuar = True
while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False
    
    janela.fill(PRETO)

    for bloco in blocos:
        mover(bloco, (LARGURAJANELA, ALTURAJANELA))
        pygame.draw.rect(janela, bloco["cor"], bloco["objRect"])
        
        if bola["objRect"].colliderect(bloco["objRect"]):
            bola["cor"] = bloco["cor"]  

    mover(bola, (LARGURAJANELA, ALTURAJANELA))
    pygame.draw.ellipse(janela, bola["cor"], bola["objRect"])
    
    relogio.tick(60)
    pygame.display.update()

pygame.quit()
