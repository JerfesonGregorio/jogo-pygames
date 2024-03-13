import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 400

x, y = 30, 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('LENDOSA')

while True:
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.draw.rect(tela, (255,0,0), (x,y,100,50))

    if y >= altura:
        y = 0
    y = y+20

    pygame.display.update()

