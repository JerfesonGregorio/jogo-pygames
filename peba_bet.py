import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.45)
musica_fundo = pygame.mixer.music.load('musica_fundo.mp3')
pygame.mixer.music.play(-1)
som_colisao = pygame.mixer.Sound('coin.wav')
som_colisao.set_volume(0.7)

largura = 640
altura = 400
pontos = 0

velocidade = 10
x_peba, y_peba = randint(0, largura - 60), randint(50, altura - 60)
x_cobra, y_cobra = largura/2, altura/2
x_controle, y_controle = velocidade, 0


fonte = pygame.font.SysFont('arial', 40, True, False)
imagem = pygame.image.load('peba_bet.png')
imagem_redimencionada = pygame.transform.scale(imagem, (60, 60))

lista_cobra = []
comprimento_inicial = 5

relogio = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('PEBA BET!')

def crescer_cobra (arg):
    for XeY in arg:
        pygame.draw.rect(tela, (0,0,255), (XeY[0], XeY[1], 20, 20))

while True:
    relogio.tick(30) #fps
    tela.fill((200,200,200))
    mensagem= f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = x_controle - velocidade
                    y_controle = 0

            if event.key == K_RIGHT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = x_controle + velocidade
                    y_controle = 0

            if event.key == K_UP:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = y_controle - velocidade
                    x_controle = 0

            if event.key == K_DOWN:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = y_controle + velocidade
                    x_controle = 0


    cobra = pygame.draw.rect(tela, (0,0,255), (x_cobra,y_cobra,20,20))
    peba = pygame.draw.rect(tela, (200,200,200), (x_peba, y_peba,60,60))
    lista_cabeca = []
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
    
    if cobra.colliderect(peba):
        x_peba, y_peba = randint(40, 500), randint(50, 400)
        pontos+=1
        som_colisao.play()
        comprimento_inicial = comprimento_inicial + 1
    
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    crescer_cobra(lista_cobra)

    tela.blit(texto_formatado, (390, 40))
    tela.blit(imagem_redimencionada, peba)

    pygame.display.update()

