# Rename multiple files via GUI

import os
from tkinter import filedialog

delString = input("String to remove: ")
fileListSring = filedialog.askopenfilenames()

fileList = list(fileListSring)

for filePath in fileList:
	newFilename = filePath.replace(delString,'')
	os.rename(r''+filePath,r''+newFilename)