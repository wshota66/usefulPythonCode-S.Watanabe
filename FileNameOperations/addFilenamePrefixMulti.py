# Rename multiple files via GUI

import os
from tkinter import filedialog

addPrefix = input("Filename Prefix: ")
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
	fileName = filePathSplit[-1]
	
	newFilename = workDir + addPrefix + fileName
	
	os.rename(r''+filePath,r''+newFilename)