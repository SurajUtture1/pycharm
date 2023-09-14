import glob
import os

files = glob.glob("C:\\Users\\suraj\\OneDrive\\Desktop\\raj\\*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))