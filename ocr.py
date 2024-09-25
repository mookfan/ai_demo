import streamlit as st
import easyocr
from pdf2image import convert_from_path

# Initialize the reader with Thai language support
reader = easyocr.Reader(['th'])

pdf_path = ''
images = convert_from_path(pdf_path)

# Process images as needed
for i, image in enumerate(images):
    image.save(f'ocr_images/page_{i}.jpg', 'JPEG')

    # Perform OCR on the image
    results = reader.readtext(f'ocr_images/page_{i}.jpg')

    # Extract and print the text
    for (bbox, text, prob) in results:
        print(f"Detected text: {text} with probability: {prob}")