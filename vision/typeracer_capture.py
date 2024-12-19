from data_vision_capture import DataVisionCapture
import time

def capture_typeracer():
    capture = DataVisionCapture()
    
    # These coordinates are for TypeRacer's text area
    # You'll need to adjust these for your screen resolution
    typeracer_region = (
        300,    # x1: left position
        400,    # y1: top position
        900,    # x2: right position
        500     # y2: bottom position
    )
    
    print("Position your browser window with TypeRacer")
    print("Starting capture in 3 seconds...")
    time.sleep(3)
    
    try:
        while True:
            metrics = capture.capture_typing_data(
                screen_region=typeracer_region
            )
            
            if metrics:
                print(f"\rSpeed: {metrics.typing_speed:.2f} WPM | "
                      f"Accuracy: {metrics.accuracy:.2f}%", end="")
            
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\nCapture stopped")

if __name__ == "__main__":
    capture_typeracer() 