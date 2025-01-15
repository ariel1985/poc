import cv2
import pytesseract

# Step 1: Load the image using OpenCV
image_path = "sample_image.png"  # Replace with your image path
image = cv2.imread(image_path)

# Step 2: Convert the image to grayscale (recommended for OCR)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Display the grayscale image (optional)
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 4: Perform OCR using PyTesseract
text = pytesseract.image_to_string(gray_image)
print("Extracted Text with OpenCV:")
print(text)
