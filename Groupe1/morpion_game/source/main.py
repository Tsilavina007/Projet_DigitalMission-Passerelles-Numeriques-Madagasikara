from music import music_class
import pygame
import random
from function import Morpion

# the actual game doesn't support player vs computer
# it was pretty hard for the 6x6 version, but i'm just a nood so i continue learning
# there may be some bug around, but just ignore it, the main function works ¯\_(ツ)_/¯
pygame.mixer.init()
music_obj = music_class()

# pick a number randomly and choose a music using the number, there's only 4 music
# all the audio are OST from the game "Nameless cat"(it's a really good pixel game, have a try!)

"""My github: https://github.com/ClermontJudicael/jeux_morpion.git"""


class audio:
    def __init__(self):

        self.i = random.randint(0, 3)

    def music(self):
        if self.i == 0:
            music_obj.play_music1()
        if self.i == 1:
            music_obj.play_music2()
        if self.i == 2:
            music_obj.play_music3()
        if self.i == 3:
            music_obj.play_music4()


# here we played the music picked randomly
sound = audio()
sound.music()

if __name__ == '__main__':

    morpion_game = Morpion()
    morpion_game.run()
