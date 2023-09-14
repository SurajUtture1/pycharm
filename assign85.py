import os

path = "C:\\Users\\suraj\\OneDrive\\Desktop\\raj"
if os.path.isdir(path):
    print("\nIt is a directory")
elif os.path.isfile(path):
    print("\nIt is normal file")
else:
    print("It is special file (socket, FIFO, device file)")
print()



