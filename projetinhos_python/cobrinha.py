import pygame
from pygame.locals import *

WINDOWS_WIDTH = 800
WINDOWS_HEIGHT = 800
POS_INICIAL_X = WINDOWS_WIDTH/2
POS_INICIAL_Y = WINDOWS_HEIGHT/2
BLOCK = 10

pygame.init()
window = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))

cobra_pos = [(POS_INICIAL_X, POS_INICIAL_Y)]
cobra_surface = pygame.Surface((BLOCK,BLOCK))
cobra_surface.fill((53,59,72))
direcao = K_LEFT

while True:
    pygame.time.Clock().tick(10)
    window.fill((68,189,50))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            quit()

        elif evento.type == KEYDOWN:
            if evento.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                direcao = evento.key

    for post in cobra_pos:
        window.blit(cobra_surface, post)

    if direcao == K_RIGHT:
        cobra_pos[0] = cobra_pos[0][0] + BLOCK, cobra_pos[0][1] #Movimenta a direita
    elif direcao == K_LEFT:
        cobra_pos[0] = cobra_pos[0][0] - BLOCK, cobra_pos[0][1] #Movimenta a esquerda
    elif direcao == K_UP:
        cobra_pos[0] = cobra_pos[0][0], cobra_pos[0][1] - BLOCK #Movimenta a cima
    elif direcao == K_DOWN:
        cobra_pos[0] = cobra_pos[0][0], cobra_pos[0][1] + BLOCK #Movimenta a baixo

    pygame.display.update()
