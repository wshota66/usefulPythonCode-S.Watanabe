# Rename multiple files via GUI

import os
import re
from tkinter import filedialog

delString = input("Old String: ") # this file: moves this input to the location found by RegEx.
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
	fileExt = filePath.split('.')[-1]
	
	newFilename = fileName.replace(delString,'')
	
	#REMOVE
	newFilename = newFilename.replace('umamusume_inGame_','')
	
	print(newFilename)
	
	# Find first capital
	regRes_1stCap = re.search(r'[A-Z]', newFilename)
	
	if regRes_1stCap: # falsy if noneType
		start = regRes_1stCap.start()
		end = regRes_1stCap.end()
	else:
		# Find first Number
		regRes_1stNum = re.search(r'[0-9]', newFilename)
		start = regRes_1stNum.start()
		end = regRes_1stNum.end()

	print(start,", ",end)
	
	newFilename = newFilename.replace(newFilename[start:end], '_' + delString + newFilename[start:end])
	print(newFilename)
	
	#REMOVE
	newFilename = workDir + 'umamusume_inGame_' + newFilename
	print(newFilename)
	
	os.rename(r''+filePath,r''+newFilename)