# Standard imports
from tkinter import filedialog # GUI library
import tkinter as tk
import os
import sys
import shutil
 
# Input image filepath(s) with GUI
root = tk.Tk()
filez = filedialog.askopenfilenames(parent=root,title='Choose files')
filez_array = root.tk.splitlist(filez)

prefices_input = input("Enter list of prefices separated by commas: ")
prefices = prefices_input.split(",")

for prefix in prefices:
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
		img_extension = img_file_name[-1]
		
		img_name_new = prefix + img_name
		
		src_file = work_dir + img_name + '.' + img_extension
		dest_file = work_dir + img_name_new + '.' + img_extension
		
		shutil.copyfile(src_file, dest_file)