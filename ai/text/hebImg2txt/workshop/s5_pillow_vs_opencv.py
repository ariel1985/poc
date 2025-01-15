from PIL import Image
import cv2
import pytesseract

# Image path
image_path = "sample_image.png"  # Replace with your image path

# Load image using Pillow
pillow_image = Image.open(image_path)
pillow_text = pytesseract.image_to_string(pillow_image)

# Load image using OpenCV
opencv_image = cv2.imread(image_path)
gray_opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
opencv_text = pytesseract.image_to_string(gray_opencv_image)

# Display results
print("Extracted Text with Pillow:")
print(pillow_text)

print("\nExtracted Text with OpenCV:")
print(opencv_text)

# close window on key press
cv2.waitKey(0)
cv2.destroyAllWindows()
# Output:
# Extracted Text with Pillow:
# 314156
