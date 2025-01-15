
from PIL import Image
import pytesseract
import cv2
import re

# # environment variables from .env
# import dotenv
# import os

# # load images from .env file
# dotenv.load_dotenv()
# image_path = os.getenv('IMAGE_PATH')

image_path = 'cropped_images_simple.jpg'

# Specify Hebrew as the language
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # Adjust path if needed

# Preprocessing the image
def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply thresholding to binarize the image
    _, thresh_image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
    
    # Save the processed image temporarily
    processed_path = "processed_image_simple.jpg"
    cv2.imwrite(processed_path, thresh_image)
    return processed_path

# Path to the cropped image
image_path = "cropped_image.jpg"

# Preprocess the image
processed_image_path = preprocess_image(image_path)

# Load the preprocessed image using PIL
processed_image = Image.open(processed_image_path)

# Perform OCR on the preprocessed image
extracted_text = pytesseract.image_to_string(processed_image, lang="heb")

# Extract numbers using regex
numbers = re.findall(r'\d+', extracted_text)

# Output the results
print("Extracted Numbers:", numbers)
