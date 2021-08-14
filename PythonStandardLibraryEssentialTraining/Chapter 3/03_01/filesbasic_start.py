# Basic file operations in Python


# TODO: open a file for writing data
# "w" means write, "r" means read, "a" means append, "r+" means read and write
fp = open('PythonStandardLibraryEssentialTraining/Chapter 3/03_01/testfile.txt',
          'w')
fp.write('This is sometext.\n')
fp.close()

# TODO: read a file's data
fp = open('PythonStandardLibraryEssentialTraining/Chapter 3/03_01/testfile.txt',
          'r')
data = fp.read()
print(data)
# TODO: Add data to an existing file
with open('PythonStandardLibraryEssentialTraining/Chapter 3/03_01/testfile.txt', 
          'a+') as fp:
    fp.write('This is data added to the file.\n')
    fp.seek(0)
    data = fp.read()
    print(data)