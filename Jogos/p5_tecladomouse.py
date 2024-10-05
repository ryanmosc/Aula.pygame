import pygame
import random

# Definindo as cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)

# Definindo outras constantes do jogo
LARGURA_JANELA = 700
ALTURA_JANELA = 600
VEL = 6
ITERACOES = 30
TAMANHO_BLOCO = 20

# Função para mover o jogador
def moverJogador(jogador, teclas, dimensaoJanela):
    bordaEsquerda = 0
    bordaSuperior = 0
    bordeDireita = dimensaoJanela[0]
    bordaInferior = dimensaoJanela[1]

    if teclas["esquerda"] and jogador["objRect"].left > bordaEsquerda:
        jogador["objRect"].x -= jogador["vel"]
    if teclas["direita"] and jogador["objRect"].right < bordeDireita:
        jogador["objRect"].x += jogador["vel"]
    if teclas["cima"] and jogador["objRect"].top > bordaSuperior:
        jogador["objRect"].y -= jogador["vel"]
    if teclas["baixo"] and jogador["objRect"].bottom < bordaInferior:
        jogador["objRect"].y += jogador["vel"]

# Função para mover os blocos
def moverBloco(bloco):
    bloco["objRect"].y += bloco["vel"]

# Inicializando pygame
pygame.init()
relogio = pygame.time.Clock()

# Criando a janela
janela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
pygame.display.set_caption("Teclado e Mouse")

# Criando o jogadorddddd
jogador = {"objRect": pygame.Rect(300, 100, 50, 50), "cor": VERDE, "vel": VEL}

# Dicionário para as teclas pressionadas
teclas = {"esquerda": False, "direita": False, "cima": False, "baixo": False}

# Inicializando outras variáveis
contador = 0
blocos = []
deve_continuar = True

# Loop do jogo
while deve_continuar:
    # Checando os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False

        # Quando uma tecla é pressionada
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                deve_continuar = False  
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas["esquerda"] = True
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas["direita"] = True
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas["cima"] = True
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas["baixo"] = True
        
        # Quando uma tecla é solta
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas["esquerda"] = False
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas["direita"] = False
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas["cima"] = False
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas["baixo"] = False

        # Quando o mouse é clicado
        if evento.type == pygame.MOUSEBUTTONDOWN:
            blocos.append({"objRect": pygame.Rect(evento.pos[0], evento.pos[1], TAMANHO_BLOCO, TAMANHO_BLOCO), "cor": BRANCO, "vel": 1})

    contador += 1
    if contador >= ITERACOES:
        posX = random.randint(0, LARGURA_JANELA - TAMANHO_BLOCO)
        posY = -TAMANHO_BLOCO
        velRandom = random.uniform(1, VEL + 3)
        blocos.append({"objRect": pygame.Rect(posX, posY, TAMANHO_BLOCO, TAMANHO_BLOCO), "cor": BRANCO, "vel": velRandom})
        contador = 0

    # Atualizando a posição dos blocos
    for bloco in blocos:
        moverBloco(bloco)
        if bloco["objRect"].top > ALTURA_JANELA:
            blocos.remove(bloco)

    # Atualizando a posição do jogador
    moverJogador(jogador, teclas, (LARGURA_JANELA, ALTURA_JANELA))

    # Desenhando tudo na tela
    janela.fill(PRETO)
    pygame.draw.rect(janela, jogador["cor"], jogador["objRect"])
    for bloco in blocos:
        pygame.draw.rect(janela, bloco["cor"], bloco["objRect"])

    pygame.display.update()
    relogio.tick(40)

pygame.quit()
