# Rename multiple files via GUI by adding prefix at beginning.

# INSTRUCTIONS:
# 1. Use Python's pip install to add the necessary libraries: "os" and "tkinter".
# 2. Run the script through Command Prompt (or Powershell or Terminal)
# 3. On the Command Prompt, type the prefix to add to the selected files. Press Enter.
# 4. Select file(s) to rename with the prefix from the "Open File" window.

# Note: Each run can only add one prefix. All selected files in Step 4. will have the same prefix defined in Step 3.

# Format: [prefix][original File Name].ext (e.g. 2022_secretFiles.pdf, where [original File Name] = "secretFiles" and [prefix] = "2022_").

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
