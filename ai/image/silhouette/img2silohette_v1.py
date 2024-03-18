import cv2
import numpy as np

# Load the image
image = cv2.imread('rmbg_0.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply thresholding to create a binary image
_, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

# Invert the binary image
silhouette = cv2.bitwise_not(binary)

# Save the silhouette image
cv2.imwrite('img2silhouette_v1_0.png', silhouette)