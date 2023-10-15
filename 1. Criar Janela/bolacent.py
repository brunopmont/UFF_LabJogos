from PPlay.window import *
from PPlay.sprite import *

janela = Window(400, 400)
janela.set_title('Bruno Porto Monteiro')

bola = Sprite('./assets/bola-3.png')
bola.set_position(janela.width/2 - bola.width/2, janela.height/2 - bola.height/2)
bola.draw()

while True:
    janela.update()