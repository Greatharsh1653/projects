import cv2

def detect_flashlight():
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    
    flashlight_detected = False
    
    while not flashlight_detected:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # Convert the captured frame to grayscale for better analysis
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Thresholding to segment flashlight area (adjust threshold value as needed)
        _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        
        # Count non-zero pixels in the binary image
        nonzero_pixels = cv2.countNonZero(binary)
        
        # If the number of non-zero pixels exceeds a certain threshold, consider flashlight as ON
        flashlight_on = nonzero_pixels > 1000
        
        # Display result
        if flashlight_on:
            print("Flashlight is ON")
        else:
            print("Flashlight is OFF")
        
        # Break the loop if flashlight status detected
        flashlight_detected = True
        
    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Run the detection function
detect_flashlight()
