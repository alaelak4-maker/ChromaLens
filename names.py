import cv2
import numpy as np

def color_name(b, g, r):
    h, s, v = cv2.cvtColor(np.uint8([[[b, g, r]]]), cv2.COLOR_BGR2HSV)[0][0]

    if v < 50:
        return "Black"
    if s < 40:
        return "White" if v > 200 else "Gray"
    if h < 10 or h >= 170:
        return "Red"
    if h < 22:
        return "Brown" if v < 150 else "Orange"
    if h < 33:
        return "Yellow"
    if h < 85:
        return "Green"
    if h < 130:
        return "Blue"
    if h < 150:
        return "Purple"
    return "Pink"

