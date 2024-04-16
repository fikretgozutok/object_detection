import cv2
import numpy as np
import pandas as pd
import pygame

class Tools():
    def __init__(self):
        pass

    @staticmethod
    def readLabelsFromFile(filePath: str) -> list[str]:
        with open(filePath, 'r') as file:
            content = file.readlines()
            content = [line.strip() for line in content]
            return content
        
    @staticmethod
    def drawBoundingBox(
        frame,
        label: str,
        confidence,
        color,
        startX,
        startY,
        endX,
        endY
    ) -> np.ndarray:
        
        label = "{}: {:.2f}%".format(label, confidence*100)
        
        cv2.rectangle(frame, (startX, startY), (endX, endY), color, 1)
        cv2.putText(frame, label, (startX, startY-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, color, 2)

        return frame

    @staticmethod
    def getAudioFileByLabel(label: str, data: pd.DataFrame) -> str | None:
        
        filter = data[data['class_list'] == label]

        if len(filter) == 0:
            return None
        
        result = filter.iloc[0]['file_path']

        result = tuple([result.strip('()')])[0]

        return result[1 : -2]
    
    @staticmethod
    def playAudio(audioFile: str, player: pygame.mixer) -> None:
        player.music.load(audioFile)
        player.music.play()

        while player.music.get_busy():
            pygame.time.Clock().tick(10)
