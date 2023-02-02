# Standard imports
import cv2
import numpy as np;
from tkinter import filedialog # GUI library
import tkinter as tk
 
# 0.0: Input image filepath(s) with GUI
root = tk.Tk()
filez = filedialog.askopenfilenames(parent=root,title='Choose files')
filez_array = root.tk.splitlist(filez)

kern_L_str = input ("Length of lines (pixels): ")
kern_W_str = input ("Thickness of lines (pixels): ")

kern_L = int(kern_L_str)
kern_W = int(kern_W_str)

for file in filez_array:
	img_path_split = file.split('/')
	work_dir = ''
	for paths in img_path_split:
		if paths == img_path_split[-1]:
			break
		if work_dir == '':
			work_dir = paths
		else:
			work_dir = 	work_dir + '\\' + paths

	work_dir = work_dir + '\\'
	img_file_name = img_path_split[-1].split('.')
	img_name = img_file_name[0]
	
	# Read image
	img = cv2.imread(file,cv2.IMREAD_GRAYSCALE)

	# 1.1: Artificially increase image size
	img_w, img_h = img.shape[::-1]
	if img_w > img_h:
		img_scale = float(3960/img_h)
	else:
		img_scale = float(3960/img_w)

	img_resized = cv2.resize(img,None,fx=img_scale, fy=img_scale, interpolation = cv2.INTER_LINEAR)

	# 1.2: Threshold
	thresh = cv2.threshold(img_resized, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
		
	# 1.3: Dilate (to catch dotted lines)
	# dilation = cv2.dilate(thresh,np.ones((3,3),np.uint8),iterations = 1)
	dilation = cv2.GaussianBlur(thresh,(9,9),0)
	
	# 2.1: Apply Sobel X to remove horizontal lines
	# Remove horizontal (https://stackoverflow.com/questions/46274961/removing-horizontal-lines-in-image-opencv-python-matplotlib)
	horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kern_L,kern_W))
	detected_lines = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, horizontal_kernel, iterations=1)
	cv2.imwrite(work_dir + img_name + '_detection.jpeg', detected_lines)
	cnts = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if len(cnts) == 2 else cnts[1]
	
	cv2.drawContours(thresh, cnts, -1, (0,0,0), kern_W+20)
	
	# 2.2: Repair image (fill gaps)
	repair_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,6))
	#repair_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
	result = 255 - cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, repair_kernel, iterations=1)
			
	# FINAL: save
	cv2.imwrite(work_dir + img_name + '_rmvHlines.jpeg', result)
	
	del result, img_resized, img, dilation, thresh, detected_lines