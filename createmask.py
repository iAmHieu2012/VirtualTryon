import numpy as np
import cv2
from matplotlib import pyplot as plt
import time

PATH_IMG =r"5.jpg"
image = cv2.imread(PATH_IMG)
cv2.threshold(image, 250, 255, cv2.THRESH_BINARY_INV)
mask = np.zeros(image.shape[:2], dtype="uint8")
rect = (1, 1, mask.shape[1], mask.shape[0])
fgModel = np.zeros((1, 65), dtype="float")
bgModel = np.zeros((1, 65), dtype="float")
start = time.time()
(mask, bgModel, fgModel) = cv2.grabCut(image, mask, rect, bgModel,
                                       fgModel, iterCount=10, mode=cv2.GC_INIT_WITH_RECT)
outputMask = np.where((mask == cv2.GC_BGD) | (mask == cv2.GC_PR_BGD),0, 1)
outputMask = (outputMask * 255).astype("uint8")

cv2.imwrite("result.png", outputMask)

plt.imshow(outputMask, cmap="gray")
plt.title('my picture')
plt.show()


# import cv2
# import numpy as np

# # load image with alpha channel
# img = cv2.imread(r"5.jpg")

# # convert to HSV
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# # create mask for shirt in hsv
# # specify lower and upper ranges for h,s,v colors of shirt
# lower = (0,0,0)
# upper = (200,255,245)
# mask = cv2.inRange(hsv, lower, upper)
# mask = cv2.merge([mask,mask,mask])

# # apply morphology to clean mask
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
# mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17,17))
# mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# # save mask
# cv2.imwrite("shirt_masked.png", mask)

# # display mask
# cv2.imshow('mask',mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()