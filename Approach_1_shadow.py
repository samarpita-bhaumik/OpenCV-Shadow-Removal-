import cv2
import numpy as np

# Global variables
drawing = False  # True if mouse is pressed
points = []      # List to store points of the polygon

# Mouse callback function
def draw_polygon(event, x, y, flags, param):
    global points, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        points.append((x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            points.append((x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        points.append((x, y))
        fill_polygon(img, points)
        points = []  # Reset points for next polygon

# Function to fill the polygon with blue color
def fill_polygon(img, points):
    # Create a mask for the polygon
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    pts = np.array(points, np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.fillPoly(mask, [pts], 255)

    # Increase the brightness of the pixels inside the polygon
    for i in range(2):
        img[mask == 255] += 10
# Read the image
img = cv2.imread('ShadowRemoval2.jpg')
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('Image', draw_polygon)

while True:
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.imshow('Image', img)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Press 'Esc' to exit
        break

cv2.destroyAllWindows()