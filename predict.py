from PIL import Image
import pytesseract

def predict(image):
    # image è un file caricato da Replicate
    img = Image.open(image)
    text = pytesseract.image_to_string(img)
    return {"text": text}
