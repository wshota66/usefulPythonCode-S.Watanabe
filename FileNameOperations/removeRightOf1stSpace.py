# Rename multiple files via GUI by removing everything on the right of the first space character (except extension).

# INSTRUCTIONS:
# 1. Use Python's pip install to add the necessary libraries: "os" and "tkinter".
# 2. Run the script through Command Prompt (or Powershell or Terminal)
# 3. Select file(s) to rename from the "Open File" window.

# Note: All files selected will have the right of its first space, including the space, removed, with the exception of its extension.

# Ex: "fileName done delete me - John.txt" becomes "fileName.txt"

# Standard imports
from tkinter import filedialog # GUI library
import tkinter as tk
import os
 
# Input image filepath(s) with GUI
root = tk.Tk()
filez = filedialog.askopenfilenames(parent=root,title='Choose files')
filez_array = root.tk.splitlist(filez)

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
	
	img_name_space_split = img_name.split(' ') # split by 'space' character.
	img_name_new = img_name_space_split[0] # keep only the first word.
	
	src_file = work_dir + img_name + '.' + img_extension
	dest_file = work_dir + img_name_new + '.' + img_extension
	
	os.rename(src_file,dest_file)
