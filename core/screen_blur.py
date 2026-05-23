import pyautogui
import numpy as np
import cv2

def get_blurred_screen():
    """Takes a screenshot and returns a blurred numpy image"""
    screenshot = pyautogui.screenshot()
    img = np.array(screenshot)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    blurred = cv2.GaussianBlur(img, (51, 51), 0)
    return blurred