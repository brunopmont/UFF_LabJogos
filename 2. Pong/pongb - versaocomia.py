from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *

#INCIAR JANELA
tela = Window(1000, 563)
teclado = Window.get_keyboard()
restart = 0
tela.set_title("Bruno Porto Monteiro")
ia = 1 

#SPRITES
bola = Sprite("2. Pong/png/bola50.png")
fundo = GameImage("2. Pong/png/onepieceredm.jpg")
pade = Sprite("2. Pong/png/padbp.png")
padd = Sprite("2. Pong/png/padbp.png")

#DEFINIR POSIÇÃO
pade.set_position(20, tela.height/2-padd.height/2)
padd.set_position(tela.width - 20 - pade.width, tela.height/2-pade.height/2)
bola.set_position(tela.width/2-bola.width/2,tela.height/2-bola.height/2)

#VARIÁVEIS DE VELOCIDADE E PONTUAÇÃO
velx = 700
vely = 700
velpady = 400
pontosesq = 0
pontosdir = 0

while True:
    if restart == 1:
        bola.move_x(velx* tela.delta_time())
        bola.move_y(vely* tela.delta_time())

    #PONTUAÇÃO E CONTROLADOR DE INÍCIO DO JOGO
    if bola.x > tela.width:
        pontosesq += 1
        bola.set_position(tela.width/2-bola.width/2,tela.height/2-bola.height/2)
        restart = 0
    elif bola.x < 0:
        pontosdir += 1
        bola.set_position(tela.width/2-bola.width/2,tela.height/2-bola.height/2)
        restart = 0
    if teclado.key_pressed("space"):   
        restart = 1

    #MOVIMENTO DA BOLA E COLISÃO COM O "TETO" E "CHÃO"
    if bola.y < 0 or bola.y + bola.height > tela.height:
        vely = vely * (-1)
        if bola.y < 0:
            bola.y = 0
        elif bola.y + bola.height > tela.height:
            bola.y = tela.height - bola.height - 1

    #MOVIMENTO DO PAD ESQUERDO COM TECLAS "W" E "A"
    if teclado.key_pressed("W"):
        if pade.y - 1 > 0:
            pade.move_y(-velpady* tela.delta_time())
    elif teclado.key_pressed("S"):
        if pade.y + pade.height + 1 < tela.height:
            pade.move_y(velpady* tela.delta_time())

    #MOVIMENTO DO PAD DIREITO COM SETAS PRA CIMA E PRA BAIXO OU COM IA
    if ia == 0:
        if teclado.key_pressed("up"):
            if padd.y - 1 > 0:
                padd.move_y(-velpady* tela.delta_time())
        elif teclado.key_pressed("down"):
            if padd.y + padd.height + 1 < tela.height:
                padd.move_y(velpady* tela.delta_time())
    else:
        if bola.y >= padd.y:
            if padd.y + padd.height + 1 < tela.height:
                padd.move_y(400* tela.delta_time())
        else:
            if padd.y - 1 > 0:
                padd.move_y(-400* tela.delta_time())

    #COLISÃO DO PAD COM A BOLINHA
    if Collision.perfect_collision(bola, padd):
        velx = -700
    if Collision.perfect_collision(bola, pade):
        velx = 700
        
    fundo.draw()
    bola.draw()
    pade.draw()
    padd.draw()
    tela.draw_text(str(pontosesq), tela.width/6, tela.height/8, size=100, color=(0,0,0))
    tela.draw_text(str(pontosdir), tela.width - tela.width/6-100, tela.height/8, size=100, color=(0,0,0))
    tela.update()