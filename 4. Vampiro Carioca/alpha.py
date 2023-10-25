from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

janela = Window(600, 600)
teclado = Window.get_keyboard()
fundo = GameImage("4. Vampiro Carioca/png/fundo_jogo.png")

player = Sprite("4. Vampiro Carioca/png/player.png")
esqueleto = Sprite("4. Vampiro Carioca/png/esqueleto.png")
policial = Sprite("4. Vampiro Carioca/png/policial.png")
zumbi = Sprite("4. Vampiro Carioca/png/zumbi.png")
player.set_position(460, 460)
esqueleto.set_position(460, 10)
policial.set_position(10, 460)
zumbi.set_position(10, 10)

velplayer = 300
velmob = 150

while True:
    if teclado.key_pressed("w"):
        if player.y - 1 > 0: 
            player.move_y(janela.delta_time() * -velplayer)
    if teclado.key_pressed("s"):
        if player.y + 1 < janela.height - player.height: 
            player.move_y(janela.delta_time() * velplayer)
    if teclado.key_pressed("a"):
        if player.x - 1 > 0: 
            player.move_x(janela.delta_time() * -velplayer)
    if teclado.key_pressed("d"):
        if player.x + 1 < janela.width - player.width: 
            player.move_x(janela.delta_time() * velplayer)

    if zumbi.x > player.x:
        zumbi.move_x(janela.delta_time() * -velmob)
    else:
        zumbi.move_x(janela.delta_time() * velmob)
    if zumbi.y > player.y:
        zumbi.move_y(janela.delta_time() * -velmob)
    else:
        zumbi.move_y(janela.delta_time() * velmob)
    janela.update()
    fundo.draw()
    player.draw()
    zumbi.draw()
