import pygame
import time

PRETO = (0,0,0)
BRANCO = (255,255,255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0,0,255)
AMARELO = (255, 255,0)

LARGURAJANELA = 800
ALTURAJANELA = 700

def mover(figura,dimensaoJanela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]
    if figura[objRect].top<borda_superior or figura[objRect].bottom>borda_inferior:
        fiura["ver"][1]= -figura["ver"][1]