import cv2

# Initialize the default webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

print("Webcam started. Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab a frame.")
        break

    # ----------------------------------------------------
    # DRAWING GEOMETRIC SHAPES (Coordinates are: x, y)
    # Note: OpenCV uses BGR color format (Blue, Green, Red)
    # ----------------------------------------------------

    # 1. Draw a Blue Line
    # Syntax: cv2.line(img, start_point, end_point, color_bgr, thickness)
    cv2.line(frame, (50, 50), (250, 50), (255, 0, 0), 5)

    # 2. Draw a Green Rectangle
    # Syntax: cv2.rectangle(img, top_left, bottom_right, color_bgr, thickness)
    # Note: Pass thickness = -1 if you want to fill the shape with solid color
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 3)

    # 3. Draw a Red Circle
    # Syntax: cv2.circle(img, center_coordinates, radius, color_bgr, thickness)
    cv2.circle(frame, (400, 200), (50), (0, 0, 255), 3)

    # 4. Draw a Solid Yellow Circle (Filled)
    cv2.circle(frame, (550, 200), (40), (0, 255, 255), -1)

    # 5. Add text overlay next to the shapes
    # Syntax: cv2.putText(img, text, origin, font, scale, color_bgr, thickness)
    cv2.putText(frame, "Thiruselvan", (50, 400), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # ----------------------------------------------------

    # Display the final frame with shapes drawn over it
    cv2.imshow('Live Camera with Shapes', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
