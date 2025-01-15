from PIL import Image
import pytesseract
import subprocess

def validate_tesseract():
    """
    Validate that Tesseract is installed and accessible.
    """
    try:
        # Check Tesseract version
        version = subprocess.run(["tesseract", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if version.returncode == 0:
            print("Tesseract is installed.")
            print("Tesseract Version:")
            print(version.stdout.splitlines()[0])
        else:
            print("Tesseract is not installed or not accessible. Please install it.")
            exit(1)
    except FileNotFoundError:
        print("Tesseract executable not found. Ensure it is installed and added to your PATH.")
        exit(1)

def run_ocr(image_path):
    """
    Run OCR on the specified image and print the results.
    """
    try:
        # Load the image
        image = Image.open(image_path)

        # Perform OCR
        text = pytesseract.image_to_string(image)

        # Print the extracted text
        print("\nExtracted Text:")
        print(text)

    except FileNotFoundError:
        print(f"Image file '{image_path}' not found.")
        exit(1)

if __name__ == "__main__":
    # Validate Tesseract installation
    validate_tesseract()

    # Run OCR on a sample image
    image_path = "sample_image.png"  # Replace with your image file
    print(f"Running OCR on '{image_path}'...")
    run_ocr(image_path)
