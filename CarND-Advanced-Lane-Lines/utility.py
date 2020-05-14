import glob 
import cv2
import argparse
import matplotlib.pyplot as plt
import numpy as np

def abs_sobel_threshold(img, orient='x', sobel_kernel=3, abs_thresh=(0, 255)):
    # Calculate directional gradient
    if orient == "x":
        sobel_edge = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = sobel_kernel)
    else:
        sobel_edge = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = sobel_kernel)
    # Apply threshold
    abs_sobel_edge = np.absolute(sobel_edge)
    scaled_sobel_edge = np.uint8((255 * abs_sobel_edge)/(np.max(abs_sobel_edge)))
    grad_binary = np.zeros_like(scaled_sobel_edge)
    grad_binary[(scaled_sobel_edge >= abs_thresh[0]) & (scaled_sobel_edge <= abs_thresh[1])] = 1
    
    return grad_binary

def mag_threshold(img, sobel_kernel=3, mag_thresh = (0, 255)):
    # Calculate gradient magnitude
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = sobel_kernel)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = sobel_kernel)
    abs_sobel = np.sqrt(np.square(sobel_x) + np.square(sobel_y))
    # Apply threshold
    scaled_sobel_edge = np.uint8((255 * abs_sobel)/(np.max(abs_sobel)))
    mag_binary = np.zeros_like(scaled_sobel_edge)
    mag_binary[(scaled_sobel_edge >= mag_thresh[0]) & (scaled_sobel_edge <= mag_thresh[1])] = 1
    
    return mag_binary

def dir_threshold(img, sobel_kernel=3, dir_thresh=(20, 90)):
    # Calculate gradient direction
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = sobel_kernel)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = sobel_kernel)  
    abs_sobel_x = np.absolute(sobel_x)
    abs_sobel_y = np.absolute(sobel_y)
    angle = np.arctan2(abs_sobel_y, abs_sobel_x)
    # Apply threshold
    dir_binary = np.zeros_like(angle)
    dir_binary[(angle >= (dir_thresh[0] * (np.pi/180))) & (angle <= (dir_thresh[1] * (np.pi/180)))] = 1    
    return dir_binary

def sat_threshold(img, s_thresh = (170, 255)):
    hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    s_channel = hls[:,:,2]
    sat_binary = np.zeros_like(s_channel)
    sat_binary[(s_channel >= s_thresh[0]) & (s_channel <= s_thresh[1])] = 1
    
    return sat_binary

def pipeline(img, ksize, abs_threshx = (0, 255), abs_threshy = (0, 255),  mag_thresh = (0, 255), dir_thresh = (20, 90), s_thresh = (0, 255)):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gradx = abs_sobel_threshold(gray, 'x', ksize, abs_threshx)
    grady = abs_sobel_threshold(gray, 'y', ksize, abs_threshy)
    mag_binary = mag_threshold(gray, ksize, mag_thresh)
    dir_binary = dir_threshold(gray, ksize, dir_thresh)
    sat_binary = sat_threshold(img, s_thresh)
    # print(np.max(sat_binary), sat_binary.shape)
    assert(gradx.shape == grady.shape == mag_binary.shape == dir_binary.shape == sat_binary.shape)
    
    combined = np.zeros_like(dir_binary)
    combined[(((gradx == 1) & (grady == 1)) & ((mag_binary == 1) & (dir_binary == 1))) | (sat_binary ==1)] = 1

    return np.array(combined * 255, dtype = np.uint8)

def get_cal_matrix():
    '''Calculate the transformation matrix for correcting image dis'''
    nx = 9 
    ny = 6
    images = glob.glob('CarND-Advanced-Lane-Lines/camera_cal/calibration*.jpg')  #fetch path of all images
    objpoints = []
    imgpoints = []
    objp = np.zeros((nx * ny, 3), np.float32)
    objp[:,:2] = np.mgrid[0:nx, 0:ny].T.reshape(-1,2)
    for img_path in images:
        img = cv2.imread(img_path, 0)
        ret, corners = cv2.findChessboardCorners(img,
                                                (nx, ny),
                                                 None)
        if ret == True:
            imgpoints.append(corners)
            objpoints.append(objp)
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img.shape, None, None)
    return mtx, dist

def cal_image(img, mtx, dist):
    '''Undistort images using transformation matrix'''
    return cv2.undistort(img, mtx, dist, None, mtx)
