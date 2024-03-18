import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 400
pontos = 0

x_red, y_red = largura/2, altura/2
x_blue, y_blue = largura/3, altura/3
fonte = pygame.font.SysFont('arial', 40, True, False)

relogio = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('LENDOSA')

while True:
    relogio.tick(30) #fps
    tela.fill((0,0,0))
    mensagem= f'pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[K_a]:
        x_red = x_red - 20

    if pygame.key.get_pressed()[K_d]:
        x_red = x_red + 20

    if pygame.key.get_pressed()[K_w]:
        y_red = y_red - 20

    if pygame.key.get_pressed()[K_s]:
        y_red = y_red + 20

    if pygame.key.get_pressed()[K_LEFT]:
        x_blue = x_blue - 20

    if pygame.key.get_pressed()[K_RIGHT]:
        x_blue = x_blue + 20

    if pygame.key.get_pressed()[K_UP]:
        y_blue = y_blue - 20

    if pygame.key.get_pressed()[K_DOWN]:
        y_blue = y_blue + 20
    

    ret_red = pygame.draw.rect(tela, (255,0,0), (x_red,y_red,40,40))
    ret_blue = pygame.draw.rect(tela, (0,0,255), (x_blue,y_blue,50,30))
    
    if ret_blue.colliderect(ret_red):
        x_red = randint(40, 600)
        y_red = randint(50, 430)
        pontos+=1
    
    tela.blit(texto_formatado, (450, 40))


    pygame.display.update()

