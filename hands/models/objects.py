import mediapipe as mp
from mediapipe.framework.formats.landmark_pb2 import NormalizedLandmarkList

mp_hands = mp.solutions.hands

class Mano:
    def __init__(self, landmark: NormalizedLandmarkList):
        self.landmark = landmark
        self.partes = self.getPartes()

    def getPartes(self) -> dict:
        """
        Retorna un diccionario con los landmarks clasificados por partes de la mano.
        """
        partes = {
            "pulgar": {
                "cmc": self.landmark.landmark[mp_hands.HandLandmark.THUMB_CMC],
                "mcp": self.landmark.landmark[mp_hands.HandLandmark.THUMB_MCP],
                "ip": self.landmark.landmark[mp_hands.HandLandmark.THUMB_IP],
                "tip": self.landmark.landmark[mp_hands.HandLandmark.THUMB_TIP]
            },
            "indice": {
                "mcp": self.landmark.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP],
                "pip": self.landmark.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP],
                "dip": self.landmark.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP],
                "tip": self.landmark.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            },
            "medio": {
                "mcp": self.landmark.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP],
                "pip": self.landmark.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP],
                "dip": self.landmark.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP],
                "tip": self.landmark.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            },
            "anular": {
                "mcp": self.landmark.landmark[mp_hands.HandLandmark.RING_FINGER_MCP],
                "pip": self.landmark.landmark[mp_hands.HandLandmark.RING_FINGER_PIP],
                "dip": self.landmark.landmark[mp_hands.HandLandmark.RING_FINGER_DIP],
                "tip": self.landmark.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            },
            "menique": {
                "mcp": self.landmark.landmark[mp_hands.HandLandmark.PINKY_MCP],
                "pip": self.landmark.landmark[mp_hands.HandLandmark.PINKY_PIP],
                "dip": self.landmark.landmark[mp_hands.HandLandmark.PINKY_DIP],
                "tip": self.landmark.landmark[mp_hands.HandLandmark.PINKY_TIP]
            },
            "palma": {
                "base": self.landmark.landmark[mp_hands.HandLandmark.WRIST]
            }
        }
        return partes
