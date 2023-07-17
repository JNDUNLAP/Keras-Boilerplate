import pytesseract
from pdf2image import convert_from_path
import tempfile
import cv2
import numpy as np
import os
import json

pdf_path = "Data/2256_001.pdf"

def process_document(pdf_path):
    page_path = 'Data/Pages'
    images = convert_from_path(pdf_path, output_folder=page_path)
    document = []
    for i, image in enumerate(images):
        image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        recognized_text = pytesseract.image_to_string(image_cv)
        page = {f"page_{i+1}": recognized_text}
        document.append(page)

    for file in os.listdir(page_path):
        os.remove(os.path.join(page_path, file))
    return document


processed_document = process_document(pdf_path)
json_document = json.dumps(processed_document)

api_response = {
    "status": "success",
    "message": "Document processed successfully",
    "data": json_document
}

json_response = json.dumps(api_response, indent=4)

print(json_response)
