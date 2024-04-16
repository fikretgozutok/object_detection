import cv2
import numpy as np

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
    def getAudioFileByLabel():
        pass