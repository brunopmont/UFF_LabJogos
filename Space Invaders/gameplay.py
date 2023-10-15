from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

disparos = []

janela = Window(500, 500)
janela.set_title("Space Invaders")
fundo = GameImage("png/fundo.png")
teclado = Window.get_keyboard()

tiro = Sprite("png/tiro.png")
nave = Sprite("png/pave.png")
velnav = 700
veltiro = -500

nave.set_position(janela.width/2 - nave.width/2, 400-nave.height/4)

while True:
    
    fundo.draw()
    nave.draw()
    janela.update()

    if teclado.key_pressed("left"):
        if nave.x + 2 > 0:
            nave.move_x(-velnav* janela.delta_time())
    if teclado.key_pressed("right"):
        if nave.x < janela.width - nave.width:
            nave.move_x(velnav* janela.delta_time())
    if teclado.key_pressed("space"):
        tiro = Sprite("png/tiro.png", 5)
        tiro.set_sequence_time(0, 4, 300, True)
        tiro.set_position(nave.x+nave.width/2-2, nave.y)
        disparos.append(tiro)
    if disparos != []:
        for d in disparos:
            d.draw()
            d.y += veltiro* janela.delta_time()