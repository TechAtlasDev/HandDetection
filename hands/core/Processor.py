from .middleware import Analytics, Experimental
import cv2
import mediapipe as mp
from mediapipe.python.solutions import hands_connections
from ..models.objects import Mano

class Window:
  def __init__(self, frame):
    self.frame = frame

  def process(self, detector):
    results = detector.process(self.frame)
    return results
  
  def draw(self, multi_landmarks, frame) -> list[Mano]:
    if multi_landmarks:
      for parts_landmarks in multi_landmarks:
        partes_mano = Mano(parts_landmarks)

#        Middleware = Analytics(parts_landmarks)
#        Middleware.println()

        Middleware = Experimental(partes_mano)
        Middleware.println()

        mp_drawing = mp.solutions.drawing_utils
        mp_drawing.draw_landmarks(frame, parts_landmarks, hands_connections.HAND_CONNECTIONS)

    
    self.frame = frame

  def show(self, title:str):
    cv2.imshow(title, self.frame)