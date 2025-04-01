import cv2

class Filtros:
  def grises(self, frame):
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    self.frame = gris
    return self
  
  def normal(self, frame):
    self.frame = frame
    return self

  def optimize(self, frame, max_width=320, max_height=240):
      """
      Optimiza el tamaño del frame manteniendo la relación de aspecto.
      - max_width: Ancho máximo permitido.
      - max_height: Altura máxima permitida.
      """
      # Obtener dimensiones actuales
      height, width = frame.shape[:2]
      
      # Calcular la relación de aspecto
      aspect_ratio = width / height

      # Determinar nuevas dimensiones manteniendo la relación de aspecto
      if width > height:
          new_width = max_width
          new_height = int(new_width / aspect_ratio)
      else:
          new_height = max_height
          new_width = int(new_height * aspect_ratio)
      
      # Redimensionar la imagen
      self.frame = cv2.resize(frame, (new_width, new_height))
      return self

  def getFrame(self):
    self.frame = cv2.flip(self.frame, 1)
    return self.frame
  
  def showFrame(self, title:str):
    self.frame = cv2.flip(self.frame, 1)
    cv2.imshow(title, self.frame)