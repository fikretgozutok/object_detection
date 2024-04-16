import cv2
from detector import Detector
from tools import Tools

detector = Detector(
    'model\yolov3.cfg',
    'model/yolov3.weights'
)

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

    cv2.imshow('Live', frame)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
