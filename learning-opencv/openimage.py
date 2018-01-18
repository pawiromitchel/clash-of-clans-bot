import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('gold_mine.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
