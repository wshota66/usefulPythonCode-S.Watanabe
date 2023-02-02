# Rename multiple files via GUI by deleting a specific exact phrase.

# INSTRUCTIONS:
# 1. Use Python's pip install to add the necessary libraries: "os" and "tkinter".
# 2. Run the script through Command Prompt (or Powershell or Terminal)
# 3. On the Command Prompt, type the exact phrase to delete from the selected file names. Press Enter.
#    3a. Phrase to delete is case-sensitive.
# 4. Select file(s) to rename with the prefix from the "Open File" window.

# Note: Each run can only delete the same phrase defined in Step 3. All selected files in Step 4. will have the same exact phrase removed as defined in Step 3.

import os
from tkinter import filedialog

delString = input("String to remove: ")
fileListSring = filedialog.askopenfilenames()

fileList = list(fileListSring)

for filePath in fileList:
	newFilename = filePath.replace(delString,'')
	os.rename(r''+filePath,r''+newFilename)
