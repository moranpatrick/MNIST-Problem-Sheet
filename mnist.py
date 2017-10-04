# Problem 1 - Read the image files - Download the image and label files, 
# have Python decompress them and read them byte by byte into appropriate data structures in memory.
# Patrick Moran

# References :
# https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python

import gzip
#open the file
f = gzip.open('data/train-images-idx3-ubyte.gz', 'rb')

# Get the magic number which we know is 2051
magic = f.read(4)
print(magic)

# Convert the Magic number To Decimal
print(int.from_bytes(magic, byteorder='big'))

#close the file
f.close()