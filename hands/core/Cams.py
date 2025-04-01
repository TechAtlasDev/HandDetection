import cv2

class Camara:
  def __init__(self, camara:int=0):
    self.camara = cv2.VideoCapture(camara)
  
  def getFrame(self) -> tuple:
    ret, frame = self.camara.read()
    return ret, frame