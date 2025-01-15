from PIL import Image
import pytesseract

# Step 1: Load the image using Pillow
image_path = "sample_image.png"  # Replace with your image path
image = Image.open(image_path)

# Step 2: Display the image (optional)
image.show()

# Step 3: Perform OCR using PyTesseract
text = pytesseract.image_to_string(image)
print("Extracted Text with Pillow:")
print(text)
