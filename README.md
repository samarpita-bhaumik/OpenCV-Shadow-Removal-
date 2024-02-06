# Shadow_Removal
Approach 1:
Mouse Callback Function:
•	Handles mouse events such as button down, mouse movement, and button up.
•	When the left mouse button is pressed down, it starts drawing by adding the current point to the list.
•	During mouse movement, if drawing is in progress, it continues to append points to the list.
•	When the left mouse button is released, drawing is stopped, and the last point is added to the list.
•	Calls fill_polygon function after drawing.
fill_polygon Function:
•	Creates a binary mask for the polygon using the list of points.
•	Increases the brightness of the pixels inside the polygon in the original image.
Image Reading and Window Setup:
•	Reads an image.
•	Sets up a window named 'Image' and associates the mouse callback function.

Picture 1:
 

Picture 2:

 









Approach 2:
•	The code allow the user to draw a polygon on an input image by clicking and dragging the mouse.
•	The drawn polygon is then used to create a region of interest (ROI) on the image.
•	A grayscale version of the ROI is thresholded to create a binary mask, highlighting certain areas of interest.
•	A road mask is created based on the drawn polygon, and this mask is applied to the original image.
•	The result is displayed in a window ,showing the original image with the specified region masked in a different color.



Picture 1:
Masked shadow region:
 






Final image masked with different color:
 

Picture 2:
Masked shadow region:
 








Final image masked with different color:
 
This is the final improvement I have done
