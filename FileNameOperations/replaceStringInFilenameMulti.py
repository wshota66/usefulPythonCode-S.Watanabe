# Rename multiple files via GUI by replacing a specific exact phrase with a new one.

# INSTRUCTIONS:
# 1. Use Python's pip install to add the necessary libraries: "os" and "tkinter".
# 2. Run the script through Command Prompt (or Powershell or Terminal)
# 3. On the Command Prompt, type the exact phrase to delete from the selected file names. Press Enter.
#    3a. Phrase to delete is case-sensitive.
# 4. On the Command Prompt, type the exact phrase to replace the deleted phrase in Step 3. from the selected file names. Press Enter.
# 5. Select file(s) to rename with the rule defined in Step 3. and 4. from the "Open File" window.

# Note: Each run can only replace the same phrase defined in Step 3. and 4. All selected files in Step 5. will have the same exact phrase removed as defined in Step 3. and 4.

# Ex: Original = "fileName.txt"
#	Old String = "Name"  (Note: case-sensitive so "name" will not work)
#	New String = "Nombre"
# RESULT = "fileNombre.txt"

import os
from tkinter import filedialog

delString = input("Old String: ")
replString = input("New String: ")
fileListSring = filedialog.askopenfilenames()

fileList = list(fileListSring)

for filePath in fileList:
	newFilename = filePath.replace(delString,replString)
	os.rename(r''+filePath,r''+newFilename)
