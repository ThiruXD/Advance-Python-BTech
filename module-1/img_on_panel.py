import cv2
import numpy as np

# 1. Configuration Constants
SIDE_PANEL_WIDTH = 250
BOTTOM_PANEL_HEIGHT = 100
WINDOW_NAME = "OpenCV Multi-Panel GUI"

# 2. Load the Main Image
img = cv2.imread('asset/iwmages.jpg')
if img is None:
    print("Error: Image not found!")
    exit()

img_h, img_w, img_c = img.shape

# 3. Calculate Canvas Dimensions
canvas_w = img_w + SIDE_PANEL_WIDTH
canvas_h = img_h + BOTTOM_PANEL_HEIGHT

# 4. Create a Blank Black Canvas
canvas = np.zeros((canvas_h, canvas_w, 3), dtype=np.uint8)

# 5. Place the Main Image into the top-left area
canvas[0:img_h, 0:img_w] = img

# 6. Customize the Side Panel (Solid dark grey fill)
canvas[0:canvas_h, img_w:canvas_w] = [45, 45, 45]  # BGR Color

# 7. Customize the Bottom Panel (Solid mid grey fill)
canvas[img_h:canvas_h, 0:img_w] = [70, 70, 70]     # BGR Color

# 8. Render UI Text Annotations
# Add a thin white dividing line
cv2.line(canvas, (img_w, 0), (img_w, canvas_h), (255, 255, 255), 1)
cv2.line(canvas, (0, img_h), (img_w, img_h), (255, 255, 255), 1)

# Add text labels (Text, coordinates, font, scale, color, thickness)
cv2.putText(canvas, "SIDE PANEL", (img_w + 20, 40), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

cv2.putText(canvas, f"Res: {img_w}x{img_h}", (img_w + 20, 80), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

cv2.putText(canvas, "BOTTOM PANEL - Status: Active", (20, img_h + 55), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

# 9. Create Window and Display the Canvas
cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_AUTOSIZE)
cv2.imshow(WINDOW_NAME, canvas)

# Keep window open until 'q' or ESC is pressed
print("Press 'q' or 'ESC' to close the GUI window.")
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        break

cv2.destroyAllWindows()
