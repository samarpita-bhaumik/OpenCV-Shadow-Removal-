# OpenCV Shadow Removal 
<ins><b>Approach 1:</b></ins><br>
<ins><b>Mouse Callback Function:</b></ins>
<ul>
 <li>Handles mouse events such as button down, mouse movement, and button up.</li>
 <li>When the left mouse button is pressed down, it starts drawing by adding the current point to the list.</li>
 <li>During mouse movement, if drawing is in progress, it continues to append points to the list.</li>
 <li>When the left mouse button is released, drawing is stopped, and the last point is added to the list.</li>
 <li>Calls fill_polygon function after drawing.</li>
</ul>
<ins><b>fill_polygon Function:</b></ins>
<ul>
 <li>Creates a binary mask for the polygon using the list of points.</li>
 <li>Increases the brightness of the pixels inside the polygon in the original image.</li>
</ul>

<ins><b>Image Reading and Window Setup:</b></ins>
<ul>
 <li>Reads an image.</li>
 <li>Sets up a window named 'Image' and associates the mouse callback function.</li>
</ul>

<ins><b>Picture 1:</b><br></ins>
<img src="approach1_pic.png" height="300px" width="500px"/>

<ins><b>Picture 2:</b></ins><br>
<img src="approach1_pic2.png" height="300px" width="500px"/>
 <br>

<b><ins>Approach 2:</ins></b>
<ul>
 <li>The code allow the user to draw a polygon on an input image by clicking and dragging the mouse.</li>
 <li>The drawn polygon is then used to create a region of interest (ROI) on the image.</li>
 <li>A grayscale version of the ROI is thresholded to create a binary mask, highlighting certain areas of interest.</li>
 <li>A road mask is created based on the drawn polygon, and this mask is applied to the original image.</li>
 <li>The result is displayed in a window ,showing the original image with the specified region masked in a different color.</li>
</ul>
	
<ins><b>Picture 1:</b></ins>
<ins><b>Masked shadow region:</b></ins><br>
<img src="masked_image1.png" height="300px" width="500px"/><br>
<ins><b>Final image masked with different color:</b></ins><br>
 <img src="shadow_removed1.png" height="300px" width="500px"/><br>

<ins><b>Picture 2:</b></ins>
<ins><b>Masked shadow region:</b></ins><br>
<img src="masked_image2.png" height="300px" width="500px"/><br> 
<ins><b>Final image masked with different color:</b></ins><br>
<img src="shadow_removed2.png" height="300px" width="500px"/><br>
<b>This is the final improvement I have done<b>
