from .core.Cams import Camara
from .core.Filters import Filtros
from .core.Processor import Window

from .core.detectors import Detectors
from .core.middleware import Forloop

import cv2

def normal():
  camara = Camara()
  convertidor = Filtros()

  while True:
    ret, frame = camara.getFrame()
    matriz = convertidor.normal(frame).getFrame()
    processor = Window(matriz)
    processor.show("Normal")

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

def grises():
  camara = Camara()
  convertidor = Filtros()

  while True:
    ret, frame = camara.getFrame()
    matriz = convertidor.grises(frame).getFrame()
    processor = Window(matriz)
    processor.show("Grises")

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

def detectHands():
  camara = Camara(1)
  convertidor = Filtros()
  detector = Detectors().Hands(max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.4)
  
  while True:
    ret, frame = camara.getFrame()
    matriz = convertidor.optimize(frame).getFrame()
    # matriz = convertidor.normal(frame).getFrame() -> Este es el normal
    processor = Window(matriz)
    resultado_detector = processor.process(detector)
    processor.draw(resultado_detector.multi_hand_landmarks, matriz)

    frame = processor.frame
    processor.show("Manos")

    breaker = Forloop(frame=frame).start()
    if breaker:
      break
