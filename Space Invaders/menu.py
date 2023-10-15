from PPlay.window import *
from PPlay.sprite import *

telanum = 0
janela = Window(500, 500)
janela.set_title("Space Invaders")
janela.set_background_color((255, 255, 255))
cursor = Window.get_mouse()
teclado = Window.get_keyboard()

jogar = Sprite("png/jogar.png")
dificuldade = Sprite("png/dificuldade.png")
ranking = Sprite("png/ranking.png")
sair = Sprite("png/sair.png")

facil = Sprite("png/facil.png")
medio = Sprite("png/medio.png")
dificil = Sprite("png/dificil.png")

jogar.set_position(janela.width/2-jogar.width/2, janela.height/6)
dificuldade.set_position(janela.width/2-jogar.width/2, 2 * janela.height/6)
ranking.set_position(janela.width/2-jogar.width/2, 3 * janela.height/6)
sair.set_position(janela.width/2-jogar.width/2, 4 * janela.height/6)

facil.set_position(janela.width/2-jogar.width/2, janela.height/6)
medio.set_position(janela.width/2-jogar.width/2, 3 * janela.height/6)
dificil.set_position(janela.width/2-jogar.width/2, 5 * janela.height/6)

while True:
    janela.update()

    if telanum == 0:
    #jogar
        if cursor.is_over_area([janela.width/2-jogar.width/2, janela.height/6], [janela.width/2+jogar.width/2, janela.height/6+jogar.height]):
            jogar = Sprite("png/jogar-2.png")
            jogar.set_position(janela.width/2-jogar.width/2, janela.height/6)
            if cursor.is_button_pressed(1):
                janela.clear()
                telanum = 1

        else:
            jogar = Sprite("png/jogar.png")
            jogar.set_position(janela.width/2-jogar.width/2, janela.height/6)

        #dificuldade
        if cursor.is_over_area([janela.width/2-jogar.width/2, 2*janela.height/6], [janela.width/2+jogar.width/2, 2*janela.height/6+jogar.height]):
            dificuldade = Sprite("png/dificuldade-2.png")
            dificuldade.set_position(janela.width/2-jogar.width/2, 2*janela.height/6)
            if cursor.is_button_pressed(1):
                janela.clear()
                telanum = 2
        else:
            dificuldade = Sprite("png/dificuldade.png")
            dificuldade.set_position(janela.width/2-jogar.width/2, 2*janela.height/6) 

        #ranking
        if cursor.is_over_area([janela.width/2-jogar.width/2, 3*janela.height/6], [janela.width/2+jogar.width/2, 3*janela.height/6+jogar.height]):
            ranking = Sprite("png/ranking-2.png")
            ranking.set_position(janela.width/2-jogar.width/2, 3*janela.height/6)
        else:
            ranking = Sprite("png/ranking.png")
            ranking.set_position(janela.width/2-jogar.width/2, 3*janela.height/6)

        #sair
        if cursor.is_over_area([janela.width/2-jogar.width/2, 4*janela.height/6], [janela.width/2+jogar.width/2, 4*janela.height/6+jogar.height]):
            sair = Sprite("png/sair-2.png")
            sair.set_position(janela.width/2-jogar.width/2, 4*janela.height/6)
            if cursor.is_button_pressed(1):
                exit()
        else:
            sair = Sprite("png/sair.png")
            sair.set_position(janela.width/2-jogar.width/2, 4*janela.height/6) 
    
    if telanum == 1 and teclado.key_pressed("esc"):
        telanum = 0

    if telanum == 0 :
        jogar.draw()
        dificuldade.draw()
        ranking.draw()
        sair.draw()

    if telanum == 2:

        facil.draw()
        medio.draw()
        dificil.draw()

        if cursor.is_over_area([janela.width/2-jogar.width/2, janela.height/6], [janela.width/2+jogar.width/2, janela.height/6+jogar.height]):
            facil = Sprite("png/facil-2.png")
            facil.set_position(janela.width/2-jogar.width/2, janela.height/6)
            if cursor.is_button_pressed(1):
                janela.clear()
                telanum = 1
        else:
            facil = Sprite("png/facil.png")
            facil.set_position(janela.width/2-jogar.width/2, janela.height/6)

        if cursor.is_over_area([janela.width/2-jogar.width/2, 3*janela.height/6], [janela.width/2+jogar.width/2, 3*janela.height/6+jogar.height]):
            medio = Sprite("png/medio-2.png")
            medio.set_position(janela.width/2-jogar.width/2, 3*janela.height/6)
            if cursor.is_button_pressed(1):
                janela.clear()
                telanum = 1
        else:
            medio = Sprite("png/medio.png")
            medio.set_position(janela.width/2-jogar.width/2, 3*janela.height/6)

        if cursor.is_over_area([janela.width/2-jogar.width/2, 5*janela.height/6], [janela.width/2+jogar.width/2, 5*janela.height/6+jogar.height]):
            dificil = Sprite("png/dificil-2.png")
            dificil.set_position(janela.width/2-jogar.width/2, 5*janela.height/6)
            if cursor.is_button_pressed(1):
                janela.clear()
                telanum = 1
        else:
            dificil = Sprite("png/dificil.png")
            dificil.set_position(janela.width/2-jogar.width/2, 5*janela.height/6)