import cv2
import pytesseract
from PIL import Image
import pandas as pd

# Set the path to Tesseract executable (if needed)
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

# Step 1: Load and preprocess the image
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)  # Apply threshold
    return thresh

# Step 2: Perform OCR for Hebrew
def extract_text_from_image(image):
    text = pytesseract.image_to_string(image, lang="heb+eng")  # Hebrew + English
    return text

# Step 3: Extract structured table data
def extract_table_data(text):
    lines = text.split("\n")
    table_data = []
    for line in lines:
        # Extract rows that contain numeric patterns (e.g., amounts, IDs)
        columns = line.split()
        if any(char.isdigit() for char in line):  # Check if line contains numbers
            table_data.append(columns)
    return table_data

# Step 4: Save the table to CSV
def save_to_csv(table_data, output_path="output_table.csv"):
    df = pd.DataFrame(table_data)
    df.to_csv(output_path, index=False, header=False, encoding="utf-8")
    print(f"Table data saved to {output_path}")

# Main function
if __name__ == "__main__":
    image_path = "recipt1.jpg"  # Replace with your receipt image path
    processed_image = preprocess_image(image_path)
    text = extract_text_from_image(processed_image)
    print("Extracted Text:")
    print(text)  # Optionally print all text

    # Extract and save the table
    table_data = extract_table_data(text)
    save_to_csv(table_data)
