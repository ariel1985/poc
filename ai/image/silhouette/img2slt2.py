import cv2
import numpy as np

def create_silhouette(filename, output_size=(500, 500)):
    # Load the image
    try:
        image = cv2.imread(filename)
        if image is None:
            print(f"Failed to load image: {filename}")
            return
    except Exception as e:
        print(f"Error: {e}")
        return

    # Resize the image
    image = cv2.resize(image, output_size)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Normalize the image
    gray = cv2.normalize(gray, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    # Convert back to 8-bit
    gray = np.uint8(gray * 255)

    # Apply adaptive thresholding
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Invert the binary image
    binary = cv2.bitwise_not(binary)

    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create an empty image for the silhouette
    silhouette = np.zeros_like(image)

    # Draw filled contour on the empty image
    cv2.drawContours(silhouette, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

    # Display the result
    cv2.imshow('image', silhouette)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function
create_silhouette('rmbg_0.jpeg')