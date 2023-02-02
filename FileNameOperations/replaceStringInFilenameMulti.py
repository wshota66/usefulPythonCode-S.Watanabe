# Rename multiple files via GUI

import os
from tkinter import filedialog

delString = input("Old String: ")
replString = input("New String: ")
fileListSring = filedialog.askopenfilenames()

fileList = list(fileListSring)

for filePath in fileList:
	newFilename = filePath.replace(delString,replString)
	os.rename(r''+filePath,r''+newFilename)