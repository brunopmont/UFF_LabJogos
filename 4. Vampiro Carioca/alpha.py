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
player.set_position(janela.width/2-player.width/2, janela.height/2-player.height/2)
esqueleto.set_position(janela.width/2-player.width/2, janela.height/2-player.height/2)
policial.set_position(janela.width/2-player.width/2, janela.height/2-player.height/2)
zumbi.set_position(janela.width/2-player.width/2, janela.height/2-player.height/2)

velplayer = 300

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

    janela.update()
    fundo.draw()
    player.draw()