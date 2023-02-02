# Rename multiple files via GUI by completely changing the file name and add a counting index at the end.

# INSTRUCTIONS:
# 1. Use Python's pip install to add the necessary libraries: "os" and "tkinter".
# 2. Run the script through Command Prompt (or Powershell or Terminal)
# 3. On the Command Prompt, type the Base File Name to add to the selected files. Press Enter.
# 4. On the Command Prompt, type the starting index number. Press Enter.
# 5. Select file(s) to rename from the "Open File" window.

# Note: Each run can only add one prefix. All selected files in Step 4. will have the same prefix defined in Step 3.

# Format: [Base File Name]_[index].ext (e.g. BassFile_001.txt)
# [index] is format "000" counting up by 1 per file.

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
