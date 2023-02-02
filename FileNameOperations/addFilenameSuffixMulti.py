# Rename multiple files via GUI by adding suffix at end.

# INSTRUCTIONS:
# 1. Use Python's pip install to add the necessary libraries: "os" and "tkinter".
# 2. Run the script through Command Prompt (or Powershell or Terminal)
# 3. On the Command Prompt, type the suffix to add to the selected files. Press Enter.
# 4. Select file(s) to rename with the suffix from the "Open File" window.

# Note: Each run can only add one suffix. All selected files in Step 4. will have the same prefix defined in Step 3.

# Format: [original File Name][suffix].ext (e.g. secretFiles--2022.pdf, where [original File Name] = "secretFiles" and [suffix] = "--2022").

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
	fileNameSplit = filePathSplit[-1].split('.')
	fileName = fileNameSplit[0]
	fileExtension = fileNameSplit[-1]
	
	newFilename = workDir + fileName + addSuffix + '.' + fileExtension
	
	os.rename(r''+filePath,r''+newFilename)
