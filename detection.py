class Detection:
    def __init__(self,
                 label,
                 confidence,
                 boxColor,
                 startX,
                 startY,
                 endX,
                 endY):
        
        self.label = label
        self.confidence = confidence
        self.boxColor = boxColor
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY