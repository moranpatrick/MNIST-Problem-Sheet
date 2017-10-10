#  * Mnist Problem Sheet *
# Problem 2 - OUTPUT AN IMAGE TO THE CONSOLE
# Output the third image in the training set to the console. 
# Do this by representing any pixel value less than 128 as a full 
# stop and any other pixel value as a hash symbol.

# Author - Patrick Moran g00179039
import gzip # open gzip file

def read_images_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        # Get Magic Number, number of images, num rows and num cols
        magic = f.read(4) 
        magic = int.from_bytes(magic, 'big') 
        
        noimg = f.read(4) 
        noimg = int.from_bytes(noimg, 'big') 
       
        nocol = f.read(4) 
        nocol = int.from_bytes(nocol, 'big') 
        
        norow = f.read(4) 
        norow = int.from_bytes(norow, 'big') 
            
        images = [] # Image array.
        # Loop through all images, rows and columns to get pixel position
        for i in range(noimg):
            row = []
            for r in range(norow):
                cols = []
                for c in range(nocol):
                    cols.append(int.from_bytes(f.read(1), 'big'))
                row.append(cols)
            images.append(row)

        return images # Return The Image Array

# Function to print out an image to the console
def print_out_image(image_array):
    for row in image_array:
        for col in row:
            # If a pixel value is less than 128 print a '.' otherwise print '#'
            print("." if col <= 127 else "#", end="")
        print()

# Read in all all the training images. (Takes a few minutes depending on computer performance)
train_images = read_images_from_file("data/train-images-idx3-ubyte.gz")
# Print out the third image in the training images set.
print_out_image(train_images[2])