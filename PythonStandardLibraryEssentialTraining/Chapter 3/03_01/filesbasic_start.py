# Basic file operations in Python


# TODO: open a file for writing data
# "w" means write, "r" means read, "a" means append, "r+" means read and write
fp = open('testfile.txt', 'w')
fp.write('This is sometext.\n')
fp.close()

# TODO: read a file's data
fp = open('testfile.txt', 'r')
data = fp.read()
print(data)


# TODO: Add data to an existing file
with open('testfile.txt', 'a+') as fp:
    fp.write('This is data added on the file.')
    fp.seek(0)
    data = fp.read()
    print(data)