# Rename multiple files via GUI

import os
from tkinter import filedialog

newBaseFilename = input("Base Filename: ")
indexStart = int(input("Starting index: ") or "0")
fileListSring = filedialog.askopenfilenames()

fileList = list(fileListSring)

index = indexStart

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
	fileExt = filePath.split('.')[-1]

	newFilename = workDir + newBaseFilename + '{:03d}'.format(index) + '.' + fileExt
	# ('{:03d}' signifies at least 3 digits. See PyFormat to control number format)
	
	os.rename(r''+filePath,r''+newFilename)
	
	index += 1