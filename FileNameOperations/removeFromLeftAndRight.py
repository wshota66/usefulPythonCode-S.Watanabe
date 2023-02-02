# Rename multiple files via GUI by removing specified number of characters from the left and number of characters from the right.

# INSTRUCTIONS:
# 1. Use Python's pip install to add the necessary libraries: "os" and "tkinter".
# 2. Run the script through Command Prompt (or Powershell or Terminal)
# 3. On the Command Prompt, type the number of characters to remove from the left of the file name. Press Enter
# 4. On the Command Prompt, type the number of characters to remove from the right of the file name. Press Enter
# 5. Select file(s) to rename with the prefix from the "Open File" window.

# Note: Each run can only remove the same number of characters per file. All selected files in Step 5. will have the same number of characters removed as defined in Steps 3. and 4.

# Visual note: [Left] --> [fileName] <-- [Right] (extension not included)

# Ex: original = fileNameULTRA.pdf
#	trimLeft = 4
#	trimRight = 2
# RESULT = NameULT.pdf

# Standard imports
from tkinter import filedialog # GUI library
import tkinter as tk
import os
 
# Input image filepath(s) with GUI
root = tk.Tk()
filez = filedialog.askopenfilenames(parent=root,title='Choose files')
filez_array = root.tk.splitlist(filez)

trimLeft = int(input('Remove how many characters from the Left?: '))
trimRight = int(input('Remove how many characters from the Right?: '))

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
		
	if trimRight > 0:
		nameLen = len(img_name)
		img_name_new = img_name[0:0-trimRight]
	else:
		img_name_new = img_name
		
	if trimLeft > 0:
		img_name_new = img_name_new[trimLeft:]
	else:
		img_name_new = img_name_new
		
	src_file = work_dir + img_name + '.' + img_extension
	dest_file = work_dir + img_name_new + '.' + img_extension
	
	os.rename(src_file,dest_file)
