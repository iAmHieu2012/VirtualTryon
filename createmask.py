import cv2
import numpy as np

# load image with alpha channel
img = cv2.imread(r"5.jpg")

# convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# create mask for shirt in hsv
# specify lower and upper ranges for h,s,v colors of shirt
lower = (0,0,0)
upper = (200,255,245)
mask = cv2.inRange(hsv, lower, upper)
mask = cv2.merge([mask,mask,mask])

# apply morphology to clean mask
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17,17))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# save mask
cv2.imwrite("shirt_masked.png", mask)

# display mask
cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()