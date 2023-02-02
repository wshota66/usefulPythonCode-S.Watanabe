# https://www.learnopencv.com/blob-detection-using-opencv-python-c/

# Standard imports
import cv2
import numpy as np;
from tkinter import filedialog # GUI library
from tkinter import *
 
root = Tk()
# Prompt user to choose HTML file with GUI
open_dir = "C:\\Users\\shota\\Desktop\\Attachments"
save_dir = "C:\\Users\\shota\\Desktop\\Attachments"
root.filename =	 filedialog.askopenfilename(initialdir = open_dir,title = "Select file",filetypes = (("jpg files","*.jpg *.jpeg *.png"),("All files","*.*")))
 
# Read image
im_raw = cv2.imread(root.filename, cv2.IMREAD_GRAYSCALE)

# Removing noise: Apply Guassian blur to filter noise, threshold to remove more noise
im = cv2.GaussianBlur(im_raw,(7,7),0)
ret3,im = cv2.threshold(im,75,255,cv2.THRESH_BINARY)  # cv2.THRESH_BINARY or cv2.THRESH_BINARY_INV

# Removing even more noise with erosion, then fill gaps using dilate. Easier to count these.
kernel = np.ones((5,5),np.uint8)
im = cv2.erode(im,kernel,iterations = 1)
kernel = np.ones((20,20),np.uint8)
im = cv2.dilate(im,kernel,iterations = 1)

# Setup SimpleBlobDetector parameters.
detector = cv2.SimpleBlobDetector_create()
params = cv2.SimpleBlobDetector_Params()

# Thresholding : Convert the source images to several binary images by thresholding the source image with thresholds starting at minThreshold. These thresholds are incremented  by thresholdStep until maxThreshold. So the first threshold is minThreshold, the second is minThreshold + thresholdStep, the third is minThreshold + 2 x thresholdStep, and so on.
# Grouping : In each binary image,  connected white pixels are grouped together.  Let’s call these binary blobs.
# Merging  : The centers of the binary blobs in the binary images are computed, and  blobs located closer than minDistBetweenBlobs are merged.
# Center & Radius Calculation :  The centers and radii of the new merged blobs are computed and returned.

# By Size :   You can filter the blobs based on size by setting the parameters filterByArea = 1, and appropriate values for minArea  and maxArea. E.g.  setting minArea  = 100 will filter out all the blobs that have less then 100 pixels.
# By Shape : Now shape has three different parameters.
# Circularity :  This just measures how close to a circle the blob is. E.g. a regular hexagon has higher circularity than say a square. To filter by circularity, set filterByCircularity = 1.  Then set appropriate values for minCircularity and maxCircularity.  Circularity is defined as

# \frac{4*\pi*Area}{perimeter * perimeter}
# This means that a circle has a circularity of 1, circularity of a square is 0.785, and so on.

# Convexity : A picture is worth a thousand words.  Convexity is defined as the (Area of the Blob / Area of it’s convex hull). Now, Convex Hull of a shape is the tightest convex shape that completely encloses the shape.  To filter by convexity, set filterByConvexity = 1, followed by setting 0 ≤ minConvexity ≤ 1 and maxConvexity ( ≤ 1) Concave versus Convex Shape
# Inertia Ratio : Don’t let this scare you. Mathematicians often use confusing words to describe something very simple. All you have to know is that this measures how elongated a shape is. E.g. for a circle, this value is 1, for an ellipse it is between 0 and 1, and for a line it is 0. To filter by inertia ratio, set filterByInertia = 1, and set 0 ≤ minInertiaRatio ≤ 1 and maxInertiaRatio (≤ 1 ) appropriately. 

# Change thresholds
params.minThreshold = 0 # 127
params.maxThreshold = 255 # 255

# Filter by Area.
params.filterByArea = True
params.minArea = 250 # 1500

# Filter by Circularity
params.filterByCircularity = False
params.minCircularity = 0.1 # 0.1

# Filter by Convexity
params.filterByConvexity = False
params.minConvexity = 0.87 # 0.87

# Filter by Inertia
params.filterByInertia = False
params.minInertiaRatio = 0.01 # 0.01

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(im)

# Count blobs.
count = len(keypoints)
print(count)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.namedWindow("Keypoints",cv2.WINDOW_NORMAL)
cv2.imshow("Keypoints", im_with_keypoints)
cv2.resizeWindow("Keypoints", 600,600)
cv2.waitKey(0)