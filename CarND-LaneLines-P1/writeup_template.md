# **Finding Lane Lines on the Road**

---

The aim of this project are the following:

* Make a pipeline that finds lane lines on the road
* Use this pipeline to detect lane lines on a continuous video stream

[image0]: ./test_images/solidWhiteCurve.jpg "Colour Image"
[image1]: ./test_images_output/Gray-solidWhiteCurve.jpg "Grayscale"
[image2]: ./test_images_output/solidWhiteCurve.jpg "Lane Lines"
[image3]: ./test_images_output/Canny-solidWhiteCurve.jpg "Canny Edges"

---
Dependencies:

* Python 3
* OpenCV & numpy - Image/Video processing toolkit
* Matplotlib - Display the Images/Videos
* PIL - Reading images
* moviepy - Creating animated videos and GIF's

---

### **1. Reading Images**

The images are read in colour format of 3 channels [BGR] and each pixel is of 8-bit i.e 0-255.

![Original colour image][image0]

Images are converted to grayscale reducing them to single channel images.

A gaussian filter of kernel size 5 is convoluted on the image to reduce unwanted noice and blur out the image.

![pre-processed grayscale image][image1]

### **2. Extracting features**

Lane line signify coloured (mostly white) strip on black roads, To detect these the best method is to find sharp edges in the image.

The Grayscale image is passed through a canny edge detector, which return all the edges above a certain tunable threshold.

![Cann edge Output][image3]

Since only a certain region of the image can contain these strips, An polygonal ROI is created which holds only lanes.

This ROI is used to calculate Hough Lines which are essentially an approximate line drawn through the points on the lane.

In order to calculate a resultant and consistant line, all the found lines are averaged to replace multiple lines with a single representative accurate line.

These lines are then plotted on the image highlighting the lane lines in the image.

![Final Output][image2]

---

## Potential shortcomings with current pipeline

Not robust for diffferent lighting conditions

Camera positioning can alter result

Dependent on hand tuned parameters which cannot be generalized

---

## Suggest possible improvements to your pipeline

Train a CNN to detect lane lines

Using night vison cameras may solve lighting problems
