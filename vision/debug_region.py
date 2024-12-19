from data_vision_capture import DataVisionCapture
from PIL import Image

def debug_region():
    capture = DataVisionCapture()
    
    # Test different regions
    region = (100, 200, 800, 300)  # Adjust these coordinates
    
    # Capture and save the region
    image = capture.capture_screen_region(*region)
    image.save("captured_region.png")
    
    # Try OCR on the region
    text = capture.extract_text_from_image(image)
    print("Captured Text:", text)

if __name__ == "__main__":
    debug_region() 