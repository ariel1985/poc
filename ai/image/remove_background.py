import cv2
import numpy as np

# Load the image
image = cv2.imread('0.jpeg')

# Create a mask of the same size as the image
mask = np.zeros(image.shape[:2], np.uint8)

# Define a rectangle that includes the foreground object
# (start_x, start_y, width, height)
rect = (50,50,450,290)

# Create two arrays used by the GrabCut algorithm internally
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

# Run the GrabCut algorithm
cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Modify the mask
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

# Multiply the image with the new mask to get the result
image = image*mask2[:,:,np.newaxis]

# Display the image
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()