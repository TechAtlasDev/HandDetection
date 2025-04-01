import mediapipe as mp

class Detectors:
  def __init__(self):
    pass

  def Hands(self, static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) -> mp.solutions.hands:
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
      static_image_mode=static_image_mode,
      max_num_hands=max_num_hands,
      min_detection_confidence=min_detection_confidence,
      min_tracking_confidence=min_tracking_confidence,
    )
    return hands