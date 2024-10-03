import pygame, random

# definindo as cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)

# definindo outras constantes do jogo
LARGURAJANELA = 700
ALTURAJANELA = 600
VEL = 6
ITERACOES = 30
TAMANHOBLOCO = 20

# definindo a função moverJogador(), que registra a posição do jogador
def moverJogador(jogador, teclas, dimensaoJanela):
    bordaEsquerda = 0
    bordaSuperior = 0
    bordeDireita = dimensaoJanela[0]
    bordaInferior = dimensaoJanela[1]

    if teclas["esquerda"] and jogador["objRect"].left > bordaEsquerda:
        jogador["objRect"].x -= jogador["vel"]

    if teclas["direita"] and jogador["objRect"].right > bordeDireita:
        jogador["objRect"].x -= jogador["vel"]
    
    if teclas["cima"] and jogador["objRect"].top > bordaSuperior:
        jogador["objRect"].y -= jogador["vel"]

    if teclas["baixo"] and jogador["objRect"].bottom > bordaInferior:
        jogador["objRect"].y -= jogador["vel"]

# definindo a função moverBloco(), que registra a posição do bloco
def moverBloco(bloco):
    bloco["objRect"].y += bloco ["vel"]

# inicializando pygame
pygame.init()

relogio = pygame.time.Clock()

# criando janela
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Teclado e Mouse")

# criando jogador
jogador = {"objRect": pygame.Rect(300, 100, 50, 50), "cor": VERDE, "vel": VEL}

# definindo o dicionario que guardará as direcoes pressionadas
teclas = {"esquerda": False, "direita": False, "cima": False, "baixo": False}

# inicializando outras variáveis
contador = 0
blocos = []
deve_continuar = True

# loop do jogo
while deve_continuar:
    # checando os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False

    # quando uma tecla é pressionada
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
        
    # quando uma tecla é solta
    if evento.type == pygame.KEYUP:
        if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
            teclas["esquerda"] = False
        if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
            teclas["direita"] = False
        if evento.key == pygame.K_UP or evento.key == pygame.K_w:
            teclas["cima"] = False
        if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
            teclas["baixo"] = False
    if event.type === pygame.MOUSEBOTOMDOWN:
        blocos.append({"objRect":pygame.Rect(evento.pos[0], evento.pos[1], TAMANHOBLOCO, TAMANHOBLOCO), "cor": BRANCO, "vel": 1})
    contador += 1
    if contador >= ITERACOES:
        posX = random.randint(0, {LARGURAJANELA, ALTURAJANELA})
        posY = -TAMANHOBLOCO
        velRandom = random.random(1, VEL + 3)
        blocos.append({"objRect":pygame.Rect(posX, posY, TAMANHOBLOCO, TAMANHOBLOCO), "cor": BRANCO, "vel": velRandom})

        pygame.drawn.rect(janela, jogador["cor"], jogador["objRect"])

        for bloco in blocos:
            bateu = jogador["objRect"].colliderect(bloco["objRect"])
            if bateu or bloco







    janela.fill(PRETO)
    pygame.display.update()
    relogio.tick(40)
pygame.quit()      