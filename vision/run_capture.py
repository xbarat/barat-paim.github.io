from data_vision_capture import DataVisionCapture
import time

def main():
    # Initialize the capture system
    capture = DataVisionCapture()
    
    # Define the screen region where the typing text appears
    # You'll need to adjust these coordinates based on your screen
    # You can use a tool like Screenshot to find the coordinates
    region = (100, 200, 800, 300)  # Example coordinates (x1, y1, x2, y2)
    
    print("Starting capture... Press Ctrl+C to stop")
    
    try:
        while True:
            # Capture metrics
            metrics = capture.capture_typing_data(
                screen_region=region,
                target_text="The quick brown fox jumps over the lazy dog"  # Example text
            )
            
            if metrics:
                print("\n--- Typing Metrics ---")
                print(f"Speed: {metrics.typing_speed:.2f} WPM")
                print(f"Accuracy: {metrics.accuracy:.2f}%")
                print(f"Captured Text: {metrics.text_content[:50]}...")
                
            time.sleep(1)  # Wait a second before next capture
            
    except KeyboardInterrupt:
        print("\nCapture stopped by user")

if __name__ == "__main__":
    main() 