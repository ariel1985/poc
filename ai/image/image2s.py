import cv2
import numpy as np

def color_space_conversion(image):
    # Convert the image from BGR to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return rgb_image

def image_thresholding(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Otsu's thresholding
    _, thresholded_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresholded_image

def smoothing_image(image):
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    return blurred_image

def find_and_draw_contours(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Find contours in the image
    contours, _ = cv2.findContours(gray_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Draw the contours on the image
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
    return image

def apply_filter(image):
    # Apply a simple linear filter (here we use a 5x5 averaging filter)
    kernel = np.ones((5, 5), np.float32) / 25
    filtered_image = cv2.filter2D(image, -1, kernel)
    return filtered_image

file = '0.jpeg'

# Load the image
image = cv2.imread(file)
   
image = color_space_conversion(image) #for the thresholding to work properly

cv2.namedWindow('image thresholding original', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image thresholding', 400, 400)
cv2.imshow('image thresholding original', image_thresholding(image))

cv2.namedWindow('image smoothing', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image smoothing', 400, 400)
cv2.imshow('image smoothing', smoothing_image(image))

cv2.namedWindow('image thresholding smoothed', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image thresholding smoothed', 400, 400)
cv2.imshow('image thresholding smoothed', image_thresholding(smoothing_image(image)))

# cv2.namedWindow('image contours', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image contours', 400, 400)
# cv2.imshow('image contours', find_and_draw_contours(image))

# cv2.namedWindow('image filter', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image filter', 400, 400)
# cv2.imshow('image filter', apply_filter(image))


# cv2.namedWindow('image morphological transformations', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image morphological transformations', 400, 400)
# cv2.imshow('image morphological transformations', morphological_transformations(image))
# cv2.namedWindow('image gradients', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image gradients', 400, 400)
# cv2.imshow('image gradients', image_gradients(image))
# cv2.namedWindow('image pyramids', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image pyramids', 400, 400)
# cv2.imshow('image pyramids', image_pyramids(image))
# cv2.namedWindow('image histogram', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image histogram', 400, 400)
# cv2.imshow('image histogram', calculate_histogram(image))
# cv2.namedWindow('image transformations', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image transformations', 400, 400)
# cv2.imshow('image transformations', apply_transformations(image))

cv2.waitKey(0)
cv2.destroyAllWindows()

