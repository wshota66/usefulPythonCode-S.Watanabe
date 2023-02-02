import cv2
import numpy as np
from tkinter import filedialog # GUI library
import tkinter as tk

# 0.0: Input image filepath(s) with GUI
root = tk.Tk()
filez = filedialog.askopenfilenames(parent=root,title='Choose files')
filez_array = root.tk.splitlist(filez)
scale_str = input ("Scale factor (number. not percent): ")
img_scale = float(scale_str)

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

	# 1.0: Preprocess to improve Tesseract acccuracy
	# 1.1: Artificially increase image size
	img = cv2.imread(file,-1)	
	img_resized = cv2.resize(img,None,fx=img_scale, fy=img_scale, interpolation = cv2.INTER_LINEAR)

	# # 1.2: Removing noise: Apply Guassian blur to filter noise, threshold to remove more noise
	# blur = cv2.GaussianBlur(img_resized,(5,5),0)
	# kernel_sharp = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
	# sharp = cv2.filter2D(blur, -1, kernel_sharp)
	# ret3,thresh1 = cv2.threshold(sharp,175,255,cv2.THRESH_BINARY)

	cv2.imwrite(work_dir + img_name + 'resized.jpeg', img_resized)
	
	del img
	del img_resized