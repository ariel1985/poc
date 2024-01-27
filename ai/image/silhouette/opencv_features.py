import cv2
import numpy as np
import matplotlib.pyplot as plt

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

def morphological_transformations(image):
    # Perform dilation
    dilated_image = cv2.dilate(image, None, iterations=2)
    return dilated_image

def image_gradients(image):
    # Compute the Sobel gradient magnitude representation
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    gradient_magnitude = np.sqrt(sobelx ** 2.0 + sobely ** 2.0)
    return gradient_magnitude

def image_pyramids(image):
    # Construct the Gaussian pyramid
    gaussian_pyramid = cv2.pyrDown(image)
    return gaussian_pyramid

def find_and_draw_contours(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Find contours in the image
    contours, _ = cv2.findContours(gray_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Draw the contours on the image
    cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
    return image

def calculate_histogram(image):
    # Calculate the histogram of the image
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    return histogram

def apply_transformations(image):
    # Apply a simple geometric transformation (here we use rotation)
    rows, cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
    transformed_image = cv2.warpAffine(image, M, (cols, rows))
    return transformed_image

def apply_filter(image):
    # Apply a simple linear filter (here we use a 5x5 averaging filter)
    kernel = np.ones((5, 5), np.float32) / 25
    filtered_image = cv2.filter2D(image, -1, kernel)
    return filtered_image

def normalize_image(image):
    if image.dtype == np.uint8:
        return image.astype(float) / 255
    else:
        return image / image.max()
    
file = '0.jpeg'

# Load the image
image = cv2.imread(file)


# cv2.namedWindow('image filter', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image filter', 400, 400)
# cv2.imshow('image filter', apply_filter(image))
# 


# Apply all the functions to the image
images = [color_space_conversion(image), image_thresholding(image), smoothing_image(image),
          morphological_transformations(image), image_gradients(image), image_pyramids(image),
          find_and_draw_contours(image), calculate_histogram(image), apply_transformations(image),
          apply_filter(image)]

images = [normalize_image(func(image)) for func in [color_space_conversion, image_thresholding, smoothing_image, morphological_transformations, image_gradients, image_pyramids, find_and_draw_contours, calculate_histogram, apply_transformations, apply_filter]]
titles = ['Color Space Conversion', 'Image Thresholding', 'Image Smoothing',
          'Morphological Transformations', 'Image Gradients', 'Image Pyramids',
          'Find and Draw Contours', 'Calculate Histogram', 'Apply Transformations',
          'Apply Filter']

# Create a figure for the images
fig = plt.figure(figsize=(10, 10))

# Loop over the images and titles
for i in range(len(images)):
    # Add a subplot for this image
    plt.subplot(4, 3, i+1)
    # Display the image
    plt.imshow(images[i], cmap='gray')
    # Set the title for this subplot
    plt.title(titles[i])
    # Remove the x- and y-axis
    plt.xticks([])
    plt.yticks([])

# Show the figure with the images
# plt.show()
plt.savefig('output123456.png')

cv2.waitKey(0)
cv2.destroyAllWindows()

