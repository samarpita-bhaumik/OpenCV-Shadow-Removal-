import cv2
import numpy as np


is_drawing = False
drawn_points = []

def draw_polygon(event, x, y, flags, param):
    global is_drawing, drawn_points

    if event == cv2.EVENT_LBUTTONDOWN:
        is_drawing = True
        drawn_points = [(x, y)]

    elif event == cv2.EVENT_LBUTTONUP:
        
        drawn_points.append((x, y))
        cv2.polylines(image, [np.array(drawn_points)], isClosed=True, color=(153, 167, 176), thickness=2)
        roi = get_roi(image, [np.array(drawn_points)])
        apply_threshold(roi)

    elif event == cv2.EVENT_MOUSEMOVE:
        if is_drawing:
            drawn_points.append((x, y))

def get_roi(image, vertices):
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, vertices, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def apply_threshold(roi):
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, binary_threshold = cv2.threshold(gray_roi, 10, 255, cv2.THRESH_BINARY)
    
    road_mask = create_road_mask(image.shape[:2], [np.array(drawn_points)])
    result_image = apply_road_mask(image, road_mask)
    
   
    cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
    cv2.imshow('Result', result_image)
    cv2.namedWindow('Result1', cv2.WINDOW_NORMAL)
    cv2.imshow('Result1', binary_threshold)

def create_road_mask(image_shape, vertices):
    mask = np.zeros(image_shape, dtype=np.uint8)
    cv2.fillPoly(mask, vertices, 255)
    return mask

def apply_road_mask(image, road_mask):
    inverted_road_mask = cv2.bitwise_not(road_mask)
    result = cv2.bitwise_and(image, image, mask=inverted_road_mask)
    
   
    result[inverted_road_mask == 0] = (167, 179, 191)  
    
    return result


image = cv2.imread('ShadowRemoval2.jpg')
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('Image', draw_polygon)

while True:
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.imshow('Image', image)

    key = cv2.waitKey(1) & 0xFF
    if key == 27: 
        break

cv2.destroyAllWindows()

