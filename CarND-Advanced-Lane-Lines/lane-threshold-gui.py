from __future__ import print_function
import cv2
import argparse
import matplotlib.pyplot as plt
from utility import *

max_value = 255
max_value_D = 90

abs_threshx_low, abs_threshx_high = 0, max_value
abs_threshy_low, abs_threshy_high = 0, max_value
mag_thresh_low, mag_thresh_high = 0, max_value
dir_thresh_low, dir_thresh_high = 0, max_value_D
s_thresh_low, s_thresh_high = 0, max_value

window_capture_name = 'Image Capture'
window_detection_name = 'Object Detection'



abs_threshx_low_name = 'abs threshx low'
abs_threshx_high_name = 'abs threshx high'
abs_threshy_low_name = 'abs threshy low'
abs_threshy_high_name = 'abs threshy high'
mag_thresh_low_name = 'mag thresh low'
mag_thresh_high_name = 'mag thresh high'
dir_thresh_low_name = 'dir thresh low'
dir_thresh_high_name = 'dir thresh high'
s_thresh_low_name = 's thresh low'
s_thresh_high_name = 's thresh high'


def abs_threshx_low_trackbar(val):
    global abs_threshx_low
    global abs_threshx_high
    abs_threshx_low = val
    abs_threshx_low = min(abs_threshx_high-1, abs_threshx_low)
    print(abs_threshx,abs_threshy,mag_thresh, dir_thresh, s_thresh)
    cv2.setTrackbarPos(abs_threshx_low_name, window_detection_name, abs_threshx_low)
def abs_threshx_high_trackbar(val):
    global abs_threshx_low
    global abs_threshx_high
    abs_threshx_high = val
    abs_threshx_high = max(abs_threshx_high, abs_threshx_low+1)
    print(abs_threshx,abs_threshy,mag_thresh, dir_thresh, s_thresh)
    cv2.setTrackbarPos(abs_threshx_high_name, window_detection_name, abs_threshx_high)
def abs_threshy_low_trackbar(val):
    global abs_threshy_low
    global abs_threshy_high
    abs_threshy_low = val
    abs_threshy_low = min(abs_threshy_high-1, abs_threshy_low)
    print(abs_threshx,abs_threshy,mag_thresh, dir_thresh, s_thresh)
    cv2.setTrackbarPos(abs_threshy_low_name, window_detection_name, abs_threshy_low)
def abs_threshy_high_trackbar(val):
    global abs_threshy_low
    global abs_threshy_high
    abs_threshy_high = val
    abs_threshy_high = max(abs_threshy_high, abs_threshy_low + 1)
    print(abs_threshx,abs_threshy,mag_thresh, dir_thresh, s_thresh)
    cv2.setTrackbarPos(abs_threshy_high_name, window_detection_name, abs_threshy_high)
def mag_thresh_low_trackbar(val):
    global mag_thresh_low
    global mag_thresh_high
    mag_thresh_low = val
    mag_thresh_low = min(mag_thresh_high-1, mag_thresh_low)
    print(abs_threshx,abs_threshy,mag_thresh, dir_thresh, s_thresh)
    cv2.setTrackbarPos(mag_thresh_low_name, window_detection_name, mag_thresh_low)
def mag_thresh_high_trackbar(val):
    global mag_thresh_low
    global mag_thresh_high
    mag_thresh_high = val
    mag_thresh_high = max(mag_thresh_high, mag_thresh_low+1)
    print(abs_threshx,abs_threshy,mag_thresh, dir_thresh, s_thresh)
    cv2.setTrackbarPos(mag_thresh_high_name, window_detection_name, mag_thresh_high)
def dir_thresh_low_trackbar(val):
    global dir_thresh_low
    global dir_thresh_high
    dir_thresh_low = val
    dir_thresh_low = min(dir_thresh_high-1, dir_thresh_low)
    print(abs_threshx,abs_threshy,mag_thresh, dir_thresh, s_thresh)
    cv2.setTrackbarPos(dir_thresh_low_name, window_detection_name, dir_thresh_low)
def dir_thresh_high_trackbar(val):
    global dir_thresh_low
    global dir_thresh_high
    dir_thresh_high = val
    dir_thresh_high = max(dir_thresh_high, dir_thresh_low+1)
    print(abs_threshx,abs_threshy,mag_thresh, dir_thresh, s_thresh)
    cv2.setTrackbarPos(dir_thresh_high_name, window_detection_name, dir_thresh_high)
def s_thresh_low_trackbar(val):
    global s_thresh_low
    global s_thresh_high
    s_thresh_low = val
    s_thresh_low = min(s_thresh_high-1, s_thresh_low)
    print(abs_threshx,abs_threshy,mag_thresh, dir_thresh, s_thresh)
    cv2.setTrackbarPos(s_thresh_low_name, window_detection_name, s_thresh_low)
    
def s_thresh_high_trackbar(val):
    global s_thresh_low
    global s_thresh_high
    s_thresh_high = val
    s_thresh_high = max(s_thresh_high, s_thresh_low+1)
    print(abs_threshx,abs_threshy,mag_thresh, dir_thresh, s_thresh)
    cv2.setTrackbarPos(s_thresh_high_name, window_detection_name, s_thresh_high)


cv2.namedWindow(window_capture_name, flags=0)
cv2.namedWindow(window_detection_name, flags=0)
cv2.createTrackbar(abs_threshx_low_name, window_detection_name , abs_threshx_low, max_value, abs_threshx_low_trackbar)
cv2.createTrackbar(abs_threshx_high_name, window_detection_name , abs_threshx_high, max_value, abs_threshx_high_trackbar)

cv2.createTrackbar(abs_threshy_low_name, window_detection_name , abs_threshy_low, max_value, abs_threshy_low_trackbar)
cv2.createTrackbar(abs_threshy_high_name, window_detection_name , abs_threshy_high, max_value, abs_threshy_high_trackbar)

cv2.createTrackbar(mag_thresh_low_name, window_detection_name , mag_thresh_low, max_value, mag_thresh_low_trackbar)
cv2.createTrackbar(mag_thresh_high_name, window_detection_name , mag_thresh_high, max_value, mag_thresh_high_trackbar)

cv2.createTrackbar(dir_thresh_low_name, window_detection_name , dir_thresh_low, max_value_D, dir_thresh_low_trackbar)
cv2.createTrackbar(dir_thresh_high_name, window_detection_name , dir_thresh_high, max_value_D, dir_thresh_high_trackbar)

cv2.createTrackbar(s_thresh_low_name, window_detection_name , s_thresh_low, max_value, s_thresh_low_trackbar)
cv2.createTrackbar(s_thresh_high_name, window_detection_name , s_thresh_high, max_value, s_thresh_high_trackbar)


mtx, dist = get_cal_matrix()
image = cv2.imread("CarND-Advanced-Lane-Lines/test_images/test5.jpg")
# print(image.shape)
image = cal_image(image, mtx, dist)
while True:
    # (201, 255) (161, 234) (169, 255) (65, 90) (140, 255)
    #(22, 83) (30, 99) (45, 207) (42, 79) (0, 255)
    abs_threshx = (abs_threshx_low, abs_threshx_high)
    abs_threshy = (abs_threshy_low, abs_threshy_high)
    mag_thresh = (mag_thresh_low, mag_thresh_high)
    dir_thresh = (dir_thresh_low, dir_thresh_high)
    s_thresh = (s_thresh_low, s_thresh_high)

    # abs_threshx = (199, 255)
    # abs_threshy = (160, 233)
    # mag_thresh = (171, 255)
    # dir_thresh = (70, 90)
    # s_thresh =  (140, 255)

    ksize = 3 # Choose a larger odd number to smooth gradient measurements
    result = pipeline(image, ksize, abs_threshx, abs_threshy, mag_thresh, dir_thresh, s_thresh)
    res=cv2.bitwise_and(image,image,mask=result)
    cv2.imshow(window_capture_name, cv2.resize(image, (500, 300)))
    cv2.imshow("result", cv2.resize(result, (800, 600)))
    key = cv2.waitKey(70)
    if key == 27:
        cv2.destroyAllWindows()
        break

cv2.destroyAllWindows()