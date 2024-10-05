import pygame
import random

# Inicializa o Pygame
pygame.init()

# Carregar imagens
imagemFundo = pygame.image.load("img/espaço.png")
imagemAsteroide = pygame.image.load("img/asteroide.png")  # Corrigido aqui
imagemNave = pygame.image.load("img/nave.png.png")
imageRaio = pygame.image.load("img/raio.png")
imageTiro = pygame.image.load("img/raio.png")
imageAlien = pygame.image.load("img/alien.png")

musica_de_fundo = pygame.mixer.music.load("mp3/trilhasonora.mp3")
pygame.mixer.music.play(-1)

barulho_tiro = pygame.mixer.Sound("mp3/som_tiro.mp3")
barulho_explosão = pygame.mixer.Sound("mp3/explosao.mp3")
barulho_de_coleta = pygame.mixer.Sound("mp3/coleta.mp3")
# Dimensões da janela
LARGURAJANELA = 700
ALTURAJANELA = 600

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)
LARANJA = (242, 79, 0)

# Parâmetros do jogo
tempo_inicial = pygame.time.get_ticks()
VEL = 6
VEL_ASTEROIDES = 3
ITERACOES = 30
TAMANHOASTEROIDE = 70
TAMANHORAIOS = 40
RAIO_INTERVALO = 100
TAMANHO_TIRO = 20
ALINEN_INTERVALO = 110
TAMANHO_ALIEN = 40
# Escalando imagens
imagemFundo = pygame.transform.scale(imagemFundo, (LARGURAJANELA, ALTURAJANELA))
imagemAsteroide = pygame.transform.scale(imagemAsteroide, (TAMANHOASTEROIDE, TAMANHOASTEROIDE))  # Escalando asteroides
imagemNave = pygame.transform.scale(imagemNave, (50, 50))
imageRaio = pygame.transform.scale(imageRaio, (TAMANHORAIOS, TAMANHORAIOS))  # Se necessário
imageAlien = pygame.transform.scale(imageAlien, (TAMANHO_ALIEN, TAMANHO_ALIEN))
# Configurações da janela
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("DESVIE DOS ASTEROIDES 1.0")
relogio = pygame.time.Clock()

# Controle de teclas
teclas = {"esquerda": False, "direita": False, "cima": False, "baixo": False}

def moverJogador(jogador, teclas, dimensaoJanela):
    if teclas["esquerda"] and jogador["objRect"].left > 0:
        jogador["objRect"].x -= jogador["vel"]
    if teclas["direita"] and jogador["objRect"].right < dimensaoJanela[0]:  
        jogador["objRect"].x += jogador["vel"]  
    if teclas["cima"] and jogador["objRect"].top > 0:
        jogador["objRect"].y -= jogador["vel"]
    if teclas["baixo"] and jogador["objRect"].bottom < dimensaoJanela[1]:  
        jogador["objRect"].y += jogador["vel"]

nave_jogador = {"objRect": pygame.Rect(300, 100, 20, 20), "cor": VERDE, "vel": VEL}
asteorides = []
raios = []
tiros = []
aliens = []
pontos = 0
Tiros = 1
tiros.clear()
deve_continuar = True
contador = 0
contador_raio = 0
contador_alien = 0

def gerartiro(x, y):
    return {"objRect": pygame.Rect(x + 20, y, TAMANHO_TIRO, TAMANHO_TIRO), "cor": LARANJA, "vel": -10}  # Velocidade negativa para mover para cima

def gerarRaio():
    posX = random.randint(0, LARGURAJANELA - TAMANHORAIOS)
    posY = 0  
    return {"objRect": pygame.Rect(posX, posY, TAMANHORAIOS, TAMANHORAIOS), "cor": LARANJA, "vel": VEL + 2}

def gerarAlien():
    posX = random.randint(0, LARGURAJANELA - TAMANHORAIOS)
    posY = 0  
    return {"objRect": pygame.Rect(posX, posY, TAMANHORAIOS, TAMANHORAIOS), "cor": LARANJA, "vel": VEL + 2}


def moverAsteroide(asteroide):
    asteroide["objRect"].y += asteroide["vel"]
    
def moverTiro(tiro):
    tiro["objRect"].y += tiro["vel"]
    
def mostrarGameOver():
    font = pygame.font.Font(None, 74)
    texto_game_over = font.render('GAME OVER', True, BRANCO)
    texto_rect = texto_game_over.get_rect(center=(LARGURAJANELA // 2, ALTURAJANELA // 2))
    janela.blit(texto_game_over, texto_rect)
    
    font_reiniciar = pygame.font.Font(None, 36)
    texto_reiniciar = font_reiniciar.render('Pressione "R" para reiniciar ou "ESC" para fechar', True, BRANCO)
    texto_reiniciar_rect = texto_reiniciar.get_rect(center=(LARGURAJANELA // 2, texto_rect.bottom + 20))
    janela.blit(texto_reiniciar, texto_reiniciar_rect)
    
    texto_adicional = font_reiniciar.render(f'Sua pontuação foi de: {pontos}', True, BRANCO)
    texto_adicional_rect = texto_adicional.get_rect(center=(LARGURAJANELA // 2, texto_reiniciar_rect.bottom + 20))
    janela.blit(texto_adicional, texto_adicional_rect)
    
    pygame.mixer.music.stop()#Para a musica quando o jogador morre
    
def reiniciarJogo():
    global nave_jogador, asteorides, raios, pontos, deve_continuar,tempo_inicial,Tiros
    nave_jogador = {"objRect": pygame.Rect(300, 100, 50, 50), "cor": VERDE, "vel": VEL}
    asteorides.clear()
    raios.clear()
    pontos = 0
    Tiros = 1
    tempo_inicial = pygame.time.get_ticks()
    deve_continuar = True
    pygame.mixer.music.play(-1)  # Reinicia a música em loop


# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()  
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas["esquerda"] = True
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas["direita"] = True
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas["cima"] = True
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas["baixo"] = True
            if evento.key == pygame.K_r and not deve_continuar:
                reiniciarJogo()
                
           #Função de geração de tiros     
            if evento.key == pygame.K_SPACE:  # Tecla para atirar
                if Tiros >= 1: #Verifica se tem ao menos 1 tiro na variavel "Tiros"
                    tiros.append(gerartiro(nave_jogador["objRect"].x, nave_jogador["objRect"].y)) #Gera os tiros
                    Tiros -= 1 #Diminui um tiro da variavel "Tiros"
                    barulho_tiro.play()
                    
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                teclas["esquerda"] = False
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                teclas["direita"] = False
            if evento.key == pygame.K_UP or evento.key == pygame.K_w:
                teclas["cima"] = False
            if evento.key == pygame.K_DOWN or evento.key == pygame.K_s:
                teclas["baixo"] = False

    if deve_continuar:
        
        tempo_decorrido = (pygame.time.get_ticks() - tempo_inicial) // 1000  # Converte para segundos
        
        contador += 1
        if contador >= ITERACOES:
            posX = random.randint(0, LARGURAJANELA - TAMANHOASTEROIDE)
            posY = -TAMANHOASTEROIDE
            velRandom = random.uniform(1, VEL_ASTEROIDES + 3)#GERADOR DE VELOCIDADE DO ASTEROIDE
            asteorides.append({"objRect": pygame.Rect(posX, posY, TAMANHOASTEROIDE, TAMANHOASTEROIDE), "cor": BRANCO, "vel": velRandom})
            contador = 0
        
        for tiro in tiros[:]:
            moverTiro(tiro)
            if tiro["objRect"].bottom < 0:  # Remove raios que saem da tela
                tiros.remove(tiro)
        
        contador_raio += 1
        if contador_raio >= RAIO_INTERVALO:
            raios.append(gerarRaio())
            contador_raio = 0
            
        contador_alien += 1
        if contador_alien >= ALINEN_INTERVALO:
            aliens.append(gerarAlien())
            contador_alien = 0    

        janela.fill(PRETO)
        
        moverJogador(nave_jogador, teclas, (LARGURAJANELA, ALTURAJANELA))
        janela.blit(imagemNave, nave_jogador["objRect"])  # Usando a imagem da nave
        
        for asteroide in asteorides[:]:
            moverAsteroide(asteroide)
            janela.blit(imagemAsteroide, asteroide["objRect"])  # Usando a imagem do asteroide
            if nave_jogador["objRect"].colliderect(asteroide["objRect"]):
                barulho_explosão.play()
                mostrarGameOver()
                deve_continuar = False
                
                
        for raio in raios[:]:
            raio["objRect"].y += raio["vel"]
            janela.blit(imageRaio, raio["objRect"])
            if nave_jogador["objRect"].colliderect(raio["objRect"]):
                barulho_de_coleta.play()
                print("Você pegou 1 raio!")  
                pontos += 1   
                Tiros +=1
                raios.remove(raio)   
    
        for alien in aliens[:]:
            alien["objRect"].y += alien["vel"]
            janela.blit(imageAlien, alien["objRect"])
            if nave_jogador["objRect"].colliderect(alien["objRect"]):
                pontos += 3 
                barulho_explosão.play()
                mostrarGameOver()
                deve_continuar = False
                aliens.remove(alien)   
                
            for tiro in tiros[:]:
                if tiro["objRect"].colliderect(alien["objRect"]):
                    pontos += 1
                    tiros.remove(tiro)
                    aliens.remove(alien)
                    break  # Para não modificar a lista durante a iteração   
                
        for tiro in tiros:
            janela.blit(imageRaio, tiro["objRect"])
    
        font = pygame.font.Font(None, 36)
        texto_pontos = font.render(f'Pontos: {pontos}', True, BRANCO)
        janela.blit(texto_pontos, (10, 10))            
        
        font = pygame.font.Font(None, 36)
        texto_Tiros = font.render(f'Tiros: {Tiros}', True, BRANCO)
        janela.blit(texto_Tiros, (10, 40))     
        
        font_tempo = pygame.font.Font(None, 36)
        texto_tempo = font_tempo.render(f'Tempo: {tempo_decorrido} s', True, BRANCO)
        janela.blit(texto_tempo, (10, 70))       
       
        pygame.display.update()
        relogio.tick(40)
        
    else:  # Loop para exibir o Game Over
        janela.fill(PRETO)
        mostrarGameOver()  
        pygame.display.update()

pygame.quit()
