import cv2
import numpy as np
import urllib.request
import os
import tkinter as tk
from tkinter import filedialog

def download_models():
    prototxt_url = "https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/deploy.prototxt"
    # Note: If this URL fails due to file size, you may need to manually download a valid caffemodel or use another model.
    caffemodel_url = "https://raw.githubusercontent.com/hwalsuklee/tensorflow-yolo-v3/master/yolov3.weights"
    caffemodel_url = "https://raw.githubusercontent.com/chuanqi305/MobileNet-SSD/master/mobilenet_iter_73000.caffemodel"
    
    prototxt_path = "deploy.prototxt"
    caffemodel_path = "mobilenet_iter_73000.caffemodel"
    
    if not os.path.exists(prototxt_path):
        print(f"Downloading {prototxt_path}...")
        try:
            urllib.request.urlretrieve(prototxt_url, prototxt_path)
        except Exception as e:
            print(f"Warning: Failed to download {prototxt_path}: {e}")

    if not os.path.exists(caffemodel_path):
        print(f"Downloading {caffemodel_path}...")
        try:
            # Note: Sometimes GitHub raw content for large files might be an LFS pointer.
            urllib.request.urlretrieve(caffemodel_url, caffemodel_path)
        except Exception as e:
            print(f"Warning: Failed to download {caffemodel_path}: {e}")
            print("You may need to download a pre-trained MobileNet SSD model manually.")

def select_image():
    root = tk.Tk()
    root.withdraw() # Hide the main window
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    return file_path

def main():
    print("--- OpenCV Modules Demonstration ---")
    
    # 1. Provide an option to upload an image
    image_path = select_image()
    if not image_path:
        print("No image selected. Exiting...")
        return
        
    print(f"Selected Image: {image_path}")

    # 2. Read and display the selected image (imgcodecs, highgui)
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not read the image.")
        return
    
    cv2.imshow("Original Image", img)

    # 3. Display image properties (core module)
    print("\n--- Image Properties (core) ---")
    print(f"Shape (Height, Width, Channels): {img.shape}")
    print(f"Size (Total number of pixels/elements): {img.size}")
    print(f"Data Type: {img.dtype}")

    # 4. Convert to grayscale, apply Gaussian blur, edge detection (imgproc)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    cv2.imshow("Grayscale Image", gray)
    cv2.imshow("Blurred Image", blurred)
    cv2.imshow("Edge Detection", edges)

    # 5. Detect and display ORB keypoints/features (features2d)
    orb = cv2.ORB_create()
    keypoints, descriptors = orb.detectAndCompute(gray, None)
    img_orb = cv2.drawKeypoints(img, keypoints, None, color=(0, 255, 0), flags=0)
    cv2.imshow("ORB Keypoints", img_orb)

    # 6. Detect human faces using a Haar Cascade classifier (objdetect)
    # Using the pre-installed Haar cascades in cv2.data
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    img_faces = img.copy()
    for (x, y, w, h) in faces:
        cv2.rectangle(img_faces, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("Face Detection", img_faces)

    # 7. Perform object detection using a pre-trained DNN model (dnn)
    # Ensure models are downloaded
    download_models()
    
    img_dnn = img.copy()
    if os.path.exists("deploy.prototxt") and os.path.exists("mobilenet_iter_73000.caffemodel"):
        try:
            net = cv2.dnn.readNetFromCaffe("deploy.prototxt", "mobilenet_iter_73000.caffemodel")
            # Prepare image for DNN (blob)
            blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 0.007843, (300, 300), 127.5)
            net.setInput(blob)
            detections = net.forward()

            h, w = img.shape[:2]
            for i in range(detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > 0.5: # 50% confidence threshold
                    idx = int(detections[0, 0, i, 1])
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    # Draw bounding box
                    cv2.rectangle(img_dnn, (startX, startY), (endX, endY), (0, 255, 255), 2)
                    label = f"Obj {idx}: {confidence:.2f}"
                    cv2.putText(img_dnn, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
            cv2.imshow("DNN Object Detection", img_dnn)
        except Exception as e:
            print("Error loading or running DNN model:", e)
    else:
        print("DNN models not found. Skipping DNN object detection.")

    # 10. Save the processed output images to disk (imgcodecs)
    cv2.imwrite("output_grayscale.jpg", gray)
    cv2.imwrite("output_edges.jpg", edges)
    cv2.imwrite("output_orb.jpg", img_orb)
    cv2.imwrite("output_faces.jpg", img_faces)
    cv2.imwrite("output_dnn.jpg", img_dnn)
    print("\nProcessed images saved to disk (e.g., output_grayscale.jpg, etc.).")

    print("\nPress any key in any image window to close them and proceed to webcam capture.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 9. Capture and display live video from the webcam (videoio)
    print("\n--- Starting Webcam (Press 'q' to quit) ---")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
    else:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame.")
                break
                
            # Apply some basic processing to webcam feed for demonstration
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Detect faces in webcam
            faces_webcam = face_cascade.detectMultiScale(gray_frame, 1.1, 4)
            for (x, y, w, h) in faces_webcam:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
            cv2.imshow("Live Webcam Face Detection", frame)
            
            # Press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # 11. Properly release all resources and close all windows
    if cap.isOpened():
        cap.release()
    cv2.destroyAllWindows()
    print("Resources released and windows closed. Program terminated.")

if __name__ == "__main__":
    main()
