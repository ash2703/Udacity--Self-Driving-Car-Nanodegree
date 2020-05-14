
## Advanced Lane Finding Project

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: # (Image References)
[image1]: ./camera_cal/calibration2.jpg "Distorted"
[image4]: ./examples/warped_straight_lines.jpg "Warp Example"
[image7]: ./examples/window_hist.png "Histogram"
[image8]: ./examples/find_peaks.png "Histogram peaks"
[image9]: ./examples/slide_histogram.png "Slide Histogram"
[image10]: ./examples/differential-eqn.png "differential equation"
[image11]: ./examples/formula.png "Simplified Formula"
[image2]: ./examples/Trackbar-GUI.png "Trackbar GUI"

[image12]: ./examples/second-derivative.png "Second order derivative"
[video1]: ./project_video.mp4 "Video"
[outimage0]: ./output_images/Corrected-image.png "Distortion Corrected image"
[outimage1]: ./output_images/lane-detected-radius.png "Calculate Radius"
[outimage2]: ./output_images/lane-detected.png "Lane Lines detected"
[outimage3]: ./output_images/line-fitted.png "Polynomial fitting using histogram sliding"
[outimage4]: ./output_images/warped-image.png "Bird-eye-view"
[outimage5]: ./output_images/stacked-threshold-gif.gif "Stacked threshold GIF"
[outimage6]: ./output_images/distortion-corrected.png "Corrected Image"
[outimage7]: ./output_images/line-fitted.png "polynomial fit lines"
[outvideo0]: ./output_images/project_video-out.mp4 "Final video output"
---

### End-to-End Lane Detection

### 1. Camera Calibration

The code for this step is contained in the function `get_cal_matrix` of the IPython notebook located in `Advanced_Lane_Detection.ipynb`  

Create "object points", which will be the (x, y, z) coordinates of the chessboard corners in the world, assuming the chessboard is fixed on the (x, y) plane at z=0, such that the object points are the same for each calibration image.  Thus, `objp` is just a replicated array of coordinates, and `objpoints` will be appended with a copy of it for every calibration image. `imgpoints` will be appended with the (x, y) pixel position of each of the corners in the image plane with each successful chessboard detection.  

The output `objpoints` and `imgpoints` are used to compute the camera calibration and distortion coefficients using the `cv2.calibrateCamera()` function. This distortion correction is applied to the test image using the `cv2.undistort()` function and obtained this result:

Distorted Image         |  Undistorted Image
:-------------------------:|:-------------------------:
![alt-text-1][image1] |  ![alt-text-2][outimage0]

### Pipeline (single images)

### Example of a distortion-corrected image

![alt text][outimage6]

#### 2. Thresholding

A combination of color and gradient thresholds is used to generate a binary image (thresholding is performed in function `pipeline`).  This involves 5 different thresholding methods

* Edge detection in x-axis
* Edge detection in y-axis
* Magnitude of edge in both direction
* Direction of edges in image
* Saturation value in HLS color space

![alt text][outimage5]

I created a trackbar GUI in order to calculate the thresholds for all these different features, the code can be found as `lane-threshold-gui.py`

![alt text][image2]

#### 3. Image Perspective Transform

Perspective transform means mapping each pixel in input image to some another coordinate in order to get a different view of the image. In this case the pixels are mapped to get a birds-eye-view image in order to effeciently calculate the lane lines. The perspective matrix is calculayed using the function `getPerspectiveMatrix`. The function requires source and destination points for calculating the transforms.

This resulted in the following source and destination points:

                | Source        | Destination   |
                |:-------------:|:-------------:|
                | 200, 720      | 310, 720      |
                | 590, 450      | 310, 0        |
                | 690,450       | 900,0         |
                | 1120, 720     | 900, 720      |

![alt text][image4]

#### 4. Lane Identification Using Sliding Histogram

* Calculate histogram along all the columns in the lower half of the image

![alt text][image7]

* Identify peaks by finding maximum value of these peals in left and right part of image

![alt text][image8]

* Considering these two peaks as start of lane move up to find complete lane

* Divide the image in multiple windows which will be used for sliding the histogram

* Calculate rectangles which will bound the pixels above a certain threshold, every time threshold is reached move the rectange one window up and set it's current position as mean of pixels in previous rectangle

![alt text][image9]

* Store the coordinates of each pixel in these rectangle, use these to fit a polynomial describing the lane lines

![alt text][outimage7]

#### 5. Calculate curvature of lanes

Once we have found the polynomials fitting the lane lines we can easily calculate the radius of curvature of these lines

The radius of curvature at any point x of the function x = f(y) is given as follows:

![alt text][image10]

In the case of the second order polynomial above, the first and second derivatives are:

![alt text][image12]

Equation for radius of curvature becomes:

![alt text][image11]

#### 6. Inverse transform and projection on original image

The function `detectLaneLine` takes an image as input and returns the finl output as lane lines segmented and plotted on the original image along with the radius of curvature

![alt text][outimage1]

---

### Pipeline (video)

#### 1. Processing Videos

Here's a [link to my video result][outvideo0]

---

### Discussion

#### 1. Issues and Fixes

* Even though the lane lines are more accurate and robust in adverse conditions such as change in brightness and scenary, it is still not general.
* The projection matrix is hardcoded and may change if road starts banking.
* Thresholds are hard coded and cannot be generalised  
