import cv2
import os
import argparse
import pytesseract
from PIL import Image, ImageGrab

screenshot = ImageGrab.grabclipboard()
imagefile = screenshot.save("temp.png")
images=cv2.imread("temp.png")
gray=cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)

filename = "{}.jpg".format(os.getpid())
cv2.imwrite(filename, gray)
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

cv2.imshow("Image Input", images)
cv2.imshow("Output In Grayscale", gray)
cv2.waitKey(0)