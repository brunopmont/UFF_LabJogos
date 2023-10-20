from PPlay.window import *
from PPlay.sprite import *

telanum = 0 #VARIÁVEL DE CONTROLE DE QUAL JANELA ESTÁ ABERTA
janela = Window(500, 500)
janela.set_title("Space Invaders")
janela.set_background_color((255, 255, 255))
cursor = Window.get_mouse() #ATIVAR MOUSE
teclado = Window.get_keyboard() #ATIVAR TECLADO

#SPRITES
jogar = Sprite("png/jogar.png")
dificuldade = Sprite("png/dificuldade.png")
ranking = Sprite("png/ranking.png")
sair = Sprite("png/sair.png")

facil = Sprite("png/facil.png")
medio = Sprite("png/medio.png")
dificil = Sprite("png/dificil.png")

#POSIÇÕES DOS SPRITES
jogar.set_position(janela.width/2-jogar.width/2, janela.height/6)
dificuldade.set_position(janela.width/2-jogar.width/2, 2 * janela.height/6)
ranking.set_position(janela.width/2-jogar.width/2, 3 * janela.height/6)
sair.set_position(janela.width/2-jogar.width/2, 4 * janela.height/6)

facil.set_position(janela.width/2-jogar.width/2, janela.height/6)
medio.set_position(janela.width/2-jogar.width/2, 3 * janela.height/6)
dificil.set_position(janela.width/2-jogar.width/2, 5 * janela.height/6)

while True:
    janela.update()

    if telanum == 0: #CASO ESTEJA NA TELA INICIAL, DESENHAR CADA BOTÃO COMO SPRITE
        jogar.draw()
        dificuldade.draw()
        ranking.draw()
        sair.draw()

    #TROCA DE SPRITE DO BOTÃO JOGAR DEPENDENDO DA POSIÇÃO DO CURSOR
        if cursor.is_over_area([janela.width/2-jogar.width/2, janela.height/6], [janela.width/2+jogar.width/2, janela.height/6+jogar.height]):
            jogar = Sprite("png/jogar-2.png")
            jogar.set_position(janela.width/2-jogar.width/2, janela.height/6)
            if cursor.is_button_pressed(1):
                janela.clear()
                telanum = 1
        else:
            jogar = Sprite("png/jogar.png")
            jogar.set_position(janela.width/2-jogar.width/2, janela.height/6)

        #TROCA DE SPRITE DO BOTÃO JOGAR DIFICULDADE DA POSIÇÃO DO CURSOR
        if cursor.is_over_area([janela.width/2-jogar.width/2, 2*janela.height/6], [janela.width/2+jogar.width/2, 2*janela.height/6+jogar.height]):
            dificuldade = Sprite("png/dificuldade-2.png")
            dificuldade.set_position(janela.width/2-jogar.width/2, 2*janela.height/6)
            if cursor.is_button_pressed(1):
                janela.clear()
                telanum = 2
        else:
            dificuldade = Sprite("png/dificuldade.png")
            dificuldade.set_position(janela.width/2-jogar.width/2, 2*janela.height/6) 

        #TROCA DE SPRITE DO BOTÃO RANKING DEPENDENDO DA POSIÇÃO DO CURSOR
        if cursor.is_over_area([janela.width/2-jogar.width/2, 3*janela.height/6], [janela.width/2+jogar.width/2, 3*janela.height/6+jogar.height]):
            ranking = Sprite("png/ranking-2.png")
            ranking.set_position(janela.width/2-jogar.width/2, 3*janela.height/6)
        else:
            ranking = Sprite("png/ranking.png")
            ranking.set_position(janela.width/2-jogar.width/2, 3*janela.height/6)

       #TROCA DE SPRITE DO BOTÃO SAIR DEPENDENDO DA POSIÇÃO DO CURSOR
        if cursor.is_over_area([janela.width/2-jogar.width/2, 4*janela.height/6], [janela.width/2+jogar.width/2, 4*janela.height/6+jogar.height]):
            sair = Sprite("png/sair-2.png")
            sair.set_position(janela.width/2-jogar.width/2, 4*janela.height/6)
            if cursor.is_button_pressed(1):
                exit()
        else:
            sair = Sprite("png/sair.png")
            sair.set_position(janela.width/2-jogar.width/2, 4*janela.height/6)
    
    if telanum == 1 and teclado.key_pressed("esc"): #CASO ESTEJA NA TELA DO JOGO E APERTAR ESC, VOLTAR PRO MENU
        telanum = 0


    if telanum == 2: #IR PRA TELA DE ESCOLHA DE DIFICULDADE E DESENHAR OS BOTÕES FÁCIL, MÉDIO E DIFÍCIL
        facil.draw()
        medio.draw()
        dificil.draw()

        #TROCA DE SPRITE DO BOTÃO FÁCIL DEPENDENDO DA POSIÇÃO DO CURSOR
        if cursor.is_over_area([janela.width/2-jogar.width/2, janela.height/6], [janela.width/2+jogar.width/2, janela.height/6+jogar.height]):
            facil = Sprite("png/facil-2.png")
            facil.set_position(janela.width/2-jogar.width/2, janela.height/6)
            if cursor.is_button_pressed(1):
                janela.clear()
                telanum = 1
        else:
            facil = Sprite("png/facil.png")
            facil.set_position(janela.width/2-jogar.width/2, janela.height/6)

        #TROCA DE SPRITE DO BOTÃO MÉDIO DEPENDENDO DA POSIÇÃO DO CURSOR
        if cursor.is_over_area([janela.width/2-jogar.width/2, 3*janela.height/6], [janela.width/2+jogar.width/2, 3*janela.height/6+jogar.height]):
            medio = Sprite("png/medio-2.png")
            medio.set_position(janela.width/2-jogar.width/2, 3*janela.height/6)
            if cursor.is_button_pressed(1):
                janela.clear()
                telanum = 1
        else:
            medio = Sprite("png/medio.png")
            medio.set_position(janela.width/2-jogar.width/2, 3*janela.height/6)

        #TROCA DO BOTÃO DIFÍCIL DEPENDENDO DA POSIÇÃO DO CURSOR
        if cursor.is_over_area([janela.width/2-jogar.width/2, 5*janela.height/6], [janela.width/2+jogar.width/2, 5*janela.height/6+jogar.height]):
            dificil = Sprite("png/dificil-2.png")
            dificil.set_position(janela.width/2-jogar.width/2, 5*janela.height/6)
            if cursor.is_button_pressed(1):
                janela.clear()
                telanum = 1
        else:
            dificil = Sprite("png/dificil.png")
            dificil.set_position(janela.width/2-jogar.width/2, 5*janela.height/6)