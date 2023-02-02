# Standard imports
import cv2
import numpy as np;
from tkinter import filedialog # GUI library
import tkinter as tk
 
# 0.0: Input image filepath(s) with GUI
root = tk.Tk()
filez = filedialog.askopenfilenames(parent=root,title='Choose files')
filez_array = root.tk.splitlist(filez)

Select = input ("Blur Type G, B or A (see code for details): ") # Select blur type: G, B or A
Size_str = input ("Kernel Size (odd integers): ") # Select blur type: G, B or A

size = int(Size_str)

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
		img_scale = float(4000/img_h)
	else:
		img_scale = float(4000/img_w)

	img_resized = cv2.resize(img,None,fx=img_scale, fy=img_scale, interpolation = cv2.INTER_LINEAR)

	# 1.2: Removing noise: Apply Guassian blur to filter noise, threshold to remove more noise
	if Select == "G": # Gaussian Blur
		blur = cv2.GaussianBlur(img_resized,(size,size),0)
	elif Select == "B": # Box Blur
		blur = cv2.blur(img_resized,(size,size),0)
	elif Select == "A": # Averaging Blur
		kernel = np.ones((size,size))
		blur = cv2.filter2D(img_resized, 0, kernel)
	# kernel_sharp = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
	# sharp = cv2.filter2D(blur, -1, kernel_sharp)
	ret3,thresh1 = cv2.threshold(blur,125,255,cv2.THRESH_BINARY)

	# FINAL: save
	cv2.imwrite(work_dir + img_name + '_hashtagFiltered.jpeg', thresh1)
	
	del img
	del thresh1, img_resized, blur