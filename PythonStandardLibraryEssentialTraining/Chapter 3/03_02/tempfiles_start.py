# Working with temporary files
import os
from sys import path
import tempfile

# TODO: get information about the temp data environment
<<<<<<< HEAD
print('gettempdir():', tempfile.gettempdir())
print('gettempprefix():', tempfile.gettempprefix())

# TODO: create a temporary file using mkstemp()
(tempfh, tempfp) = tempfile.mkstemp('.temp', 'testTemp', None, True)
f = os.dopen(tempfh, 'w+t')
f.write('This is some text data.')
=======
print('gettempdir', tempfile.gettempdir())
print('gettempprefix', tempfile.gettempprefix())

# TODO: create a temporary file using mkstemp()
(tempfh, tempfp) = tempfile.mkstemp('.temp', 'testTemp', None, True)
f = os.fdopen(tempfh, 'w+t')
f.write('This is some temp data')
>>>>>>> 724a0eefbfb414b6202b17be37554509ca0b6b27
f.seek(0)
print(f.read())
f.close()
os.remove(tempfp)
<<<<<<< HEAD


# TODO: create a temp file using the TemporaryFile class
with tempfile.TemporaryFile(mode='w+t') as tfp:
    tfp.write('This is some text data.')
    tfp.seek(0)
    print(tfp.read())

=======

# TODO: create a temp file using the TemporaryFile class
with tempfile.TemporaryFile(mode='w+t') as tfp:
    tfp.write('This is some temp data')
    tfp.seek(0)
    print(tfp.read())
>>>>>>> 724a0eefbfb414b6202b17be37554509ca0b6b27

# TODO: create a temporary directory using the TemporaryDirectory class
with tempfile.TemporaryDirectory() as tdp:
    path = os.path.join(tdp, 'tempfile.txt')
<<<<<<< HEAD
    tfp = open(path, 'w+t')
    tfp.write('This is temp file in temp dir.')
    tfp.seek(0)
    print(tfp.read())
    tfp.close()
=======
    tfp = open(path,'w+t')
    tfp.write('This is a temp file in a temp dir')
    tfp.seek(0)
    print(tfp.read())
>>>>>>> 724a0eefbfb414b6202b17be37554509ca0b6b27
