from fer import FER
import cv2

def get_emotion(img_path):
    img = cv2.imread(img_path) 
    detector = FER()
    emotion, score = detector.top_emotion(img)
    
    return emotion