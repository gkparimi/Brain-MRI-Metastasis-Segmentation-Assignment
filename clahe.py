
import cv2

def apply_clahe(image):
    """Apply CLAHE to a given MRI image."""
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    return clahe.apply(image)
