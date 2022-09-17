import cv2
import numpy as np
import easyocr
import matplotlib.pyplot as plt

img_path = './Income.jpeg'


def recognize_text(img_path):
    '''loads an image and recognizes text.'''

    reader = easyocr.Reader(['en'])
    return reader.readtext(img_path)


result = recognize_text(img_path)
print(result)
