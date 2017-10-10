#  * Mnist Problem Sheet *
# Problem 1 - READ THE DATA FILES
# Download the image and label files. Have Python decompress 
# and read them byte by byte into appropriate data structures in memory.

# Author - Patrick Moran g00179039
import gzip # open gzip file

# This function reads labels from a specified file
def read_labels_from_file(filename):
    with gzip.open(filename, 'rb') as f: # Open the file.
        magic = f.read(4) # Read the first 4 bytes to get the magic number.
        magic = int.from_bytes(magic, 'big') # Convert from bytes into an integer.
        print("Magic is: ", magic) # Magic number should be 2049.

        nolab = f.read(4) # Read the next 4 bytes to get the number of labels.
        nolab = int.from_bytes(nolab, 'big') # Convert into an integer.
        print("Number of labels: ", nolab) # Print the number if labels.

# This function reads images from a specified file
def read_images_from_file(filename):
    with gzip.open(filename, 'rb') as f: # Open the file.
        magic = f.read(4) # Read the first 4 bytes to get the magic number.
        magic = int.from_bytes(magic, 'big') # Convert from bytes into an integer.
        print("Magic is: ", magic) # Magic number should be 2051.

        noimg = f.read(4) # Read the next 4 bytes to get the number of images.
        noimg = int.from_bytes(noimg, 'big') # Convert from bytes into an integer.
        print("Number of images: ", noimg) # Print the number of images.

        nocol = f.read(4) # Read the next 4 bytes to get the number of columns.
        nocol = int.from_bytes(nocol, 'big') # Convert from bytes into an integer.
        print("Number of column: ", nocol) # Print the number of Columns.

        norow = f.read(4) # Read the next 4 bytes to get the number of rows.
        norow = int.from_bytes(norow, 'big') # Convert from bytes into an integer.
        print("Number of labels: ", norow) # Print the number of Rows.



# Read in Test and Training Labels
print("**TRAINING LABELS**")
read_labels_from_file("data/train-labels-idx1-ubyte.gz")
print("**TEST LABELS**")
read_labels_from_file("data/t10k-labels-idx1-ubyte.gz")

# Read in in Test and Training Images
print("**TRAINING IMAGES**")
read_images_from_file("data/train-images-idx3-ubyte.gz")
print("**TEST IMAGES**")
read_images_from_file("data/t10k-images-idx3-ubyte.gz")