import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# ---------------------------------
# Select an Image
# ---------------------------------
Tk().withdraw()  # Hide the Tkinter root window

file_path = askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp *.tif *.tiff"),
        ("All Files", "*.*")
    ]
)

if not file_path:
    print("No image selected.")
    exit()

# Read the image
original = cv2.imread(file_path)

if original is None:
    print("Unable to read the image.")
    exit()

display = original.copy()

print("\n========== OpenCV Image Flip ==========")
print("H : Flip Horizontally")
print("V : Flip Vertically")
print("B : Flip Both Horizontally and Vertically")
print("R : Restore Original Image")
print("ESC : Exit")
print("=======================================\n")

while True:

    cv2.imshow("Image Flip Application", display)

    key = cv2.waitKey(0) & 0xFF

    if key == ord('h') or key == ord('H'):
        display = cv2.flip(original, 1)
        print("Horizontal Flip")

    elif key == ord('v') or key == ord('V'):
        display = cv2.flip(original, 0)
        print("Vertical Flip")

    elif key == ord('b') or key == ord('B'):
        display = cv2.flip(original, -1)
        print("Horizontal + Vertical Flip")

    elif key == ord('r') or key == ord('R'):
        display = original.copy()
        print("Original Image Restored")

    elif key == 27:   # ESC key
        break

cv2.destroyAllWindows()

