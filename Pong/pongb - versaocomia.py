from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *

#iniciar janela
tela = Window(1000, 563)
teclado = Window.get_keyboard()
restart = 0
tela.set_title("Bruno Porto Monteiro")
ia = 1 

#imagens
bola = Sprite("png/bola50.png")
fundo = GameImage("png/onepieceredm.jpg")
pade = Sprite("png/padbp.png")
padd = Sprite("png/padbp.png")

#definir posição
pade.set_position(20, tela.height/2-padd.height/2)
padd.set_position(tela.width - 20 - pade.width, tela.height/2-pade.height/2)
bola.set_position(tela.width/2-bola.width/2,tela.height/2-bola.height/2)

#variáveis
velx = 700
vely = 700
velpady = 400
pontosesq = 0
pontosdir = 0

while True:
    if restart == 1:
        bola.move_x(velx* tela.delta_time())
        bola.move_y(vely* tela.delta_time())

    #pontuação e restart
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

    #movimento bola e colisão com parede
    if bola.y < 0 or bola.y + bola.height > tela.height:
        vely = vely * (-1)
        if bola.y < 0:
            bola.y = 0
        elif bola.y + bola.height > tela.height:
            bola.y = tela.height - bola.height - 1

    #mov pade com w e a
    if teclado.key_pressed("W"):
        if pade.y - 1 > 0:
            pade.move_y(-velpady* tela.delta_time())
    elif teclado.key_pressed("S"):
        if pade.y + pade.height + 1 < tela.height:
            pade.move_y(velpady* tela.delta_time())

    #mov padd com cima e baixo ou ia
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

    #colisão pad e bolinha
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