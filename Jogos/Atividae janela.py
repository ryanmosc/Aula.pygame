import pygame

pygame.init()

janela = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Free fife RTX")

deve_continuar = True
while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False