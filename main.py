# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.

import threading

import pygame

import ball
import bar
import mainWindow
import randomball
import time
import os
from randomMusicplayer import WavPlayerRandom
from multiprocessing import Process

# Thread List
threads = []

BALLSPEED = 1
MUSIC_ON = True
SOUND_ON = True
PVP_CONTROL = True
COMPUTERONLYCONTROL = True
TIME_SINCE_GAME_START = time.time()


if __name__ == '__main__':
    pygame.init()
    soundObj = pygame.mixer.Sound('ResourcesInUse/GameStart.wav')
    soundObj.play()
    TIME_SINCE_GAME_START = time.time()


    # Init the entities

    bar1 = bar.bar([30, 30], 620, 480, 30, 120)
    bar2 = bar.bar([620 - 60, 30], 620, 480, 30, 120)

    ball = ball.ball([mainWindow.mainWindow.screenwidth / 2, mainWindow.mainWindow.screenheight / 2], 620, 480, 10, 0)
    randomball.randomBallEngine(ball)

    main = mainWindow.mainWindow(bar1, bar2, ball)
    main.createOne()

    x = threading.Thread(target=main.mainWindowLoop, args=(PVP_CONTROL,))
    threads.append(x)

    # Start only the window thread - Cython blocks concurrency
    threads[0].start()


    # End

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
