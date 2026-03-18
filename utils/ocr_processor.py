import cv2
import pytesseract
# 👇 Add this line right here, after importing pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from PIL import Image
import numpy as np

def preprocess_image(image):
    """
    Convert image to grayscale, increase contrast, remove noise, apply threshold.
    """
    # Convert PIL Image to OpenCV format
    img = np.array(image)
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    else:
        gray = img

    # Increase contrast
    gray = cv2.convertScaleAbs(gray, alpha=1.5, beta=0)

    # Noise removal
    gray = cv2.medianBlur(gray, 3)

    # Thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresh

def extract_text_from_image(image):
    """
    Preprocess image and run OCR.
    """
    processed = preprocess_image(image)
    # Convert back to PIL for Tesseract
    pil_img = Image.fromarray(processed)
    text = pytesseract.image_to_string(pil_img)
    return text.strip()
