import cv2

# 1. Initialize the default camera (0 is usually the built-in webcam)
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

print("Webcam successfully started. Press 'q' to exit.")

# 2. Loop continuously to read frames from the camera
while True:
    # Capture frame-by-frame
    # 'ret' is a boolean (True if frame read successfully)
    # 'frame' is the actual image array
    ret, frame = cap.read()

    # If the frame wasn't grabbed correctly, break the loop
    if not ret:
        print("Error: Failed to grab a frame.")
        break

    # 3. Display the resulting live video frame in a window
    cv2.imshow('Live Webcam Feed', frame)
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Live Webcam GREY Feed', grey_frame)

    # 4. Wait for 1 millisecond and check if the user pressed the 'q' key
    # 0xFF masks the integer to get the clean ASCII value
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 5. When everything is done, release the hardware capture resource and close windows
cap.release()
cv2.destroyAllWindows()
