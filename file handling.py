# file creation
'''f = open("C:\\Users\\suraj\\OneDrive\\Desktop\\suraj\c.txt", "x")
print("file created")'''

# file write
'''d = open("C:\\Users\\suraj\\OneDrive\\Desktop\\suraj\c.txt", "w")
d.write("success\n raju")
print("wrote")'''

# file read
'''g = open("C:\\Users\\suraj\\OneDrive\\Desktop\\suraj\c.txt", "r")
print(g.read(10))'''
# read line
'''g = open("C:\\Users\\suraj\\OneDrive\\Desktop\\suraj\c.txt", "r")
#print(g.readline())
print(g.readlines())'''

# exception
'''try:
    t = open("C:\\Users\\suraj\\OneDrive\\Desktop\\suraj\z.txt", "r")
    print(t.readlines())
except:
    print("file not found")
else:
    t.close()
    print("closed ")'''

'''try:
    with open("C:\\Users\\suraj\\OneDrive\\Desktop\\suraj\c.txt") as c2:
        with open("C:\\Users\\suraj\\OneDrive\\Desktop\\suraj\z.txt", "w") as c3:
            for i in c2:
                c3.write(i)
except:
    print("file not found")
else:
    c2.close()
    print("closed")'''

import os

if os.path.exists("C:\\Users\\suraj\\OneDrive\\Desktop\\suraj\c.txt"):
    os.remove("C:\\Users\\suraj\\OneDrive\\Desktop\\suraj\c.txt")
    print("deleted")
else:
    print("not found")
