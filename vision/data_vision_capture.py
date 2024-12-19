from PIL import Image
import numpy as np
import cv2
from typing import Dict, Any, Optional
import time
from dataclasses import dataclass

@dataclass
class CaptureMetrics:
    timestamp: float
    text_content: str
    typing_speed: float
    accuracy: float
    screen_region: tuple

class DataVisionCapture:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
        self.last_capture_time = 0
        self.capture_interval = 0.1  # 100ms default interval
        
    def capture_screen_region(self, x1: int, y1: int, x2: int, y2: int) -> Image.Image:
        """Capture a specific region of the screen"""
        screenshot = cv2.cvtColor(
            np.array(Image.grab((x1, y1, x2, y2))), 
            cv2.COLOR_BGR2RGB
        )
        return Image.fromarray(screenshot)
    
    def extract_text_from_image(self, image: Image.Image) -> str:
        """Extract text from image using OCR"""
        try:
            import pytesseract
            return pytesseract.image_to_string(image)
        except ImportError:
            raise ImportError("Please install pytesseract: pip install pytesseract")
    
    def calculate_typing_metrics(self, 
                               current_text: str, 
                               target_text: str, 
                               elapsed_time: float) -> Dict[str, float]:
        """Calculate typing speed and accuracy metrics"""
        if not elapsed_time:
            return {"wpm": 0, "accuracy": 0}
            
        # Calculate Words Per Minute (WPM)
        char_count = len(current_text)
        wpm = (char_count / 5) / (elapsed_time / 60)
        
        # Calculate accuracy
        correct_chars = sum(1 for a, b in zip(current_text, target_text) if a == b)
        accuracy = (correct_chars / len(target_text)) * 100 if target_text else 0
        
        return {
            "wpm": round(wpm, 2),
            "accuracy": round(accuracy, 2)
        }
    
    def capture_typing_data(self, 
                           screen_region: tuple,
                           target_text: str = None) -> CaptureMetrics:
        """Capture and analyze typing data from screen region"""
        current_time = time.time()
        
        # Throttle capture rate
        if current_time - self.last_capture_time < self.capture_interval:
            return None
            
        # Capture screen region
        image = self.capture_screen_region(*screen_region)
        
        # Extract text
        captured_text = self.extract_text_from_image(image)
        
        # Calculate metrics
        elapsed_time = current_time - self.last_capture_time
        metrics = self.calculate_typing_metrics(
            captured_text, 
            target_text or captured_text,
            elapsed_time
        )
        
        self.last_capture_time = current_time
        
        return CaptureMetrics(
            timestamp=current_time,
            text_content=captured_text,
            typing_speed=metrics["wpm"],
            accuracy=metrics["accuracy"],
            screen_region=screen_region
        ) 