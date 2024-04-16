import cv2
import pygame
import threading
import pandas as pd
from detector import Detector
from tools import Tools


detector = Detector(
    'model\yolov3.cfg',
    'model/yolov3.weights'
)

player = pygame.mixer
player.init()

data = pd.read_csv('outputs\data.csv')

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    detector.readFrame(frame)

    (label, 
     confidence, 
     boxColor, 
     startX, 
     startY, 
     endX, 
     endY) = detector.predict()
    
    frame = Tools.drawBoundingBox(
        frame,
        label,
        confidence,
        boxColor,
        startX,
        startY,
        endX,
        endY
    )

    if not player.music.get_busy():
        audioFile = Tools.getAudioFileByLabel(label, data)

        if not audioFile == None:
            threadPlayer = threading.Thread(target = Tools.playAudio, args = (audioFile, player))
            threadPlayer.start()

    # threadPreview = threading.Thread(target = cv2.imshow, args = ('Live', frame))
    # threadPreview.start()

    cv2.imshow('Live', frame)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
