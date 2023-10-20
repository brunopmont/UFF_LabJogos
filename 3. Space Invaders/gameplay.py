from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

def atira():
    tiro = Sprite("png/tiro.png")
    tiro.set_position(nave.x+nave.width/2-2, nave.y)
    return tiro

janela = Window(500, 500)
janela.set_title("Space Invaders")
fundo = GameImage("png/fundo.png")
teclado = Window.get_keyboard()

tiro = Sprite("png/tiro.png")
nave = Sprite("png/pave.png")
velnav = 700
veltiro = -500

timer = 0
tiros = []

nave.set_position(janela.width/2 - nave.width/2, 400-nave.height/4)

while True:
    fundo.draw()
    nave.draw()
    timer += janela.delta_time()
    if teclado.key_pressed("left"):
        if nave.x + 2 > 0:
            nave.move_x(-velnav* janela.delta_time())
    if teclado.key_pressed("right"):
        if nave.x < janela.width - nave.width:
            nave.move_x(velnav* janela.delta_time())
    if teclado.key_pressed("space") and timer > 0.1:
        tiros.append(atira())
        timer = 0     
    if tiros != []:
        for t in tiros:
            t.draw()
            t.y += veltiro* janela.delta_time()
            if t.y < 0:
                tiros.remove(t)
    tiro.y += veltiro* janela.delta_time()
    janela.update()