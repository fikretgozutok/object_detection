from tools import Tools
import pandas as pd
import pygame
import threading

path = 'outputs\data.csv'

data = pd.read_csv(path)

label = 'person'

audioFile = Tools.getAudioFileByLabel(label, data)

player = pygame.mixer

player.init()

def xy():
    print('fjdkslşajk')

thread1 = threading.Thread(target = Tools.playAudio, args = (audioFile, player))
thread2 = threading.Thread(target = xy)

thread1.start()
thread2.start()
