import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# ---------------------------------------
# Select Image
# ---------------------------------------
Tk().withdraw()

image_path = askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)

if not image_path:
    print("No image selected")
    exit()

# ---------------------------------------
# IMGCODECS MODULE
# ---------------------------------------
img = cv2.imread(image_path)

if img is None:
    print("Unable to load image")
    exit()

# ---------------------------------------
# CORE MODULE
# ---------------------------------------
print("\n--- CORE MODULE ---")
print("Image Shape :", img.shape)
print("Image Size  :", img.size)
print("Image Type  :", img.dtype)

# Create a copy using core operations
core_img = cv2.add(img, np.zeros(img.shape, dtype=np.uint8))

# ---------------------------------------
# IMGPROC MODULE
# ---------------------------------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blur, 100, 200)

# ---------------------------------------
# FEATURES2D MODULE
# ---------------------------------------
orb = cv2.ORB_create()

keypoints, descriptors = orb.detectAndCompute(gray, None)

feature_img = cv2.drawKeypoints(
    img,
    keypoints,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

print("Number of ORB Features:", len(keypoints))

# ---------------------------------------
# OBJDETECT MODULE
# ---------------------------------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)

face_img = img.copy()

for (x, y, w, h) in faces:
    cv2.rectangle(
        face_img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

print("Faces Detected:", len(faces))

# ---------------------------------------
# DNN MODULE
# MobileNet SSD Object Detection
# ---------------------------------------
try:

    model = "MobileNetSSD_deploy.caffemodel"
    proto = "MobileNetSSD_deploy.prototxt"

    net = cv2.dnn.readNetFromCaffe(proto, model)

    dnn_img = img.copy()

    blob = cv2.dnn.blobFromImage(
        cv2.resize(img, (300, 300)),
        0.007843,
        (300, 300),
        127.5
    )

    net.setInput(blob)

    detections = net.forward()

    h, w = img.shape[:2]

    classes = [
        "background", "aeroplane", "bicycle", "bird",
        "boat", "bottle", "bus", "car", "cat",
        "chair", "cow", "diningtable", "dog",
        "horse", "motorbike", "person",
        "pottedplant", "sheep", "sofa",
        "train", "tvmonitor"
    ]

    for i in range(detections.shape[2]):

        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:

            idx = int(detections[0, 0, i, 1])

            box = detections[0, 0, i, 3:7] * \
                  np.array([w, h, w, h])

            (x1, y1, x2, y2) = box.astype("int")

            label = classes[idx]

            cv2.rectangle(
                dnn_img,
                (x1, y1),
                (x2, y2),
                (0, 0, 255),
                2
            )

            cv2.putText(
                dnn_img,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2
            )

except:
    print("\nDNN model files not found.")
    dnn_img = img.copy()

# ---------------------------------------
# HIGHGUI MODULE
# ---------------------------------------
cv2.imshow("Original Image", img)
cv2.imshow("Edges - Imgproc", edges)
cv2.imshow("ORB Features - Features2D", feature_img)
cv2.imshow("Face Detection - Objdetect", face_img)
cv2.imshow("DNN Object Detection", dnn_img)

# ---------------------------------------
# VIDEOIO MODULE
# ---------------------------------------
cap = cv2.VideoCapture(0)

print("\nPress 'q' to quit webcam.")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("VideoIO Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ---------------------------------------
# Save Output (IMGCODECS)
# ---------------------------------------
cv2.imwrite("edges_output.jpg", edges)
cv2.imwrite("features_output.jpg", feature_img)
cv2.imwrite("faces_output.jpg", face_img)

cap.release()
cv2.destroyAllWindows()

print("\nOutputs Saved Successfully")
