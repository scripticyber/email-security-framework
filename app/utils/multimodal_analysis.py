import pytesseract
from PIL import Image
from io import BytesIO
from deepface import DeepFace

def analyze_attachment(attachment: bytes, filename: str) -> dict:
    if filename.endswith(('.jpg', '.png')):
        img = Image.open(BytesIO(attachment))
        text = pytesseract.image_to_string(img)  # OCR
        deepfake = DeepFace.verify(img, model_name="VGG-Face")  # Stub for deepfake
        return {"ocr_text": text, "deepfake": deepfake['verified']}
    return {}