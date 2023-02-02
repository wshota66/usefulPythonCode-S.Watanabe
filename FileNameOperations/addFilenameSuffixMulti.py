# Rename multiple files via GUI

import os
from tkinter import filedialog

addSuffix = input("Filename Suffix: ")
fileListSring = filedialog.askopenfilenames()

fileList = list(fileListSring)

for filePath in fileList:
	filePathSplit = filePath.split('/')
	workDir = ''
	for paths in filePathSplit:
		if paths == filePathSplit[-1]:
			break
		if workDir == '':
			workDir = paths
		else:
			workDir =	workDir + '\\' + paths

	workDir = workDir + '\\'
	file_name_full = img_path_split[-1].split('.')
	file_name = img_file_name[0] + addSuffix
	file_extension = img_file_name[-1]
	
	newFilename = workDir + file_name + '.' + file_extension
	
	os.rename(r''+filePath,r''+newFilename)