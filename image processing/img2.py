import cv2 as cv
import matplotlib.pyplot as plt

img = cv2.imread('img2.jpg')
cv2.imshow(img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow(img_gray)