import os
import cv2
import pyautogui
from mediapipe.framework.formats.landmark_pb2 import NormalizedLandmarkList

class Analytics:
  def __init__(self, landmark:NormalizedLandmarkList):
    self.landmark = landmark

    self.x = landmark.landmark[0].x if landmark else 0
    self.y = landmark.landmark[0].y if landmark else 0
    self.z = landmark.landmark[0].z if landmark else 0

  def println(self):
    print (f"\r[ X: {self.x} | Y: {self.y} | Z: {self.z} ]", end="")

class Forloop:
  def __init__(self, frame):
    self.frame = frame
  
  def start(self):
    # Pausar todo
    if cv2.waitKey(1) & 0xFF == ord('q'):
      return True
    
class Experimental:
  def __init__(self, partes_mano):
    self.partes_mano = partes_mano
    self.screen_width, self.screen_height = pyautogui.size()

  def println(self):

    pulgar = self.partes_mano.partes['pulgar']
    punta_pulgar = pulgar['tip']
    indice = self.partes_mano.partes['indice']
    punta_indice = indice['tip']

    '''pulgarData = f"""[ PULGAR ]
  [PUNTA]
{punta_pulgar}

[ INDICE ]
  [PUNTA]
{punta_indice}

[ DIFERENCIAS ]
x: {punta_pulgar.x - punta_indice.x}
y: {punta_pulgar.y - punta_indice.y}
z: {punta_pulgar.z - punta_indice.z}

[ ¿ESTÁN JUNTOS? ]
{(punta_pulgar.x - punta_indice.x) < 0.05 and (punta_pulgar.y - punta_indice.y) < 0.05 and (punta_pulgar.z - punta_indice.z) < 0.05}
"""'''
    
    #moviendo mouse
    pyautogui.moveTo((punta_indice.x * self.screen_width), (punta_indice.y * self.screen_height))

    #mantener click si están juntos

    if (punta_pulgar.x - punta_indice.x) < 0.05 and (punta_pulgar.y - punta_indice.y) < 0.05 and (punta_pulgar.z - punta_indice.z) < 0.05:
      pyautogui.mouseDown()
    else:
      pyautogui.mouseUp()

    #os.system("clear")
    #print (f"{pulgarData}",)
