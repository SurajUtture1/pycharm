import os.path
import time
print('File          :',__file__)
print('Access time   :',time.ctime(os.path.getatime(__file__)))
print('Modified time :',time.ctime(os.path.getmtime(__file__)))