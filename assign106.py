import os.path
for path in ['C:\\Users\\suraj\\OneDrive\\Desktop\\raj\\s.txt', 'raj', 'C:\\Users\\suraj\\OneDrive\\Desktop\\raj\\s1.txt', '/', '' ]:
    print('"%s" :' % path, os.path.splitext(path))