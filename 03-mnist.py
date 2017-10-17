#  * Mnist Problem Sheet *
# Problem 3 - Output the image files as PNGs
# Use Python to output the image files as PNGs, saving them in a subfolder in your repository. 
# Name the images in the format train-XXXXX-Y.png or test-XXXXX-Y.png where XXXXX is the image number 
# (where it occurs in the data file) and Y is its label. For instance, the five-thousandth training image 
# is labelled 2, so its file name should be train-04999-2.png. Note the images are indexed from 0, so the 
# five-thousandth image is indexed as 4999. See below for an example of it. Commit these image files to GitHub.

# Author - Patrick Moran g00179039
import gzip # open gzip file

# This function reads labels from a specified file
def read_labels_from_file(filename):
    with gzip.open(filename, 'rb') as f: 
        magic = f.read(4) 
        magic = int.from_bytes(magic, 'big') 
        print("Labels Magic Number is: ", magic) 

        nolab = f.read(4) 
        nolab = int.from_bytes(nolab, 'big') 
        print("Total Number of labels: ", nolab)

        label_nums = [] # Label Array to hold all the labels
        # Loop around all the labels, coverting them to integers and adding them to the array
        for i in range(nolab):
            label_nums.append(int.from_bytes(f.read(1), 'big'))

        return label_nums # return array

def read_images_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        # Get Magic Number, number of images, num rows and num cols
        magic = f.read(4) 
        magic = int.from_bytes(magic, 'big') 
        print("Images Magic Number is: ", magic) 

        noimg = f.read(4) 
        noimg = int.from_bytes(noimg, 'big') 
        print("Number of images: ", noimg) # Print the number of images.
        
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

# This Function takes in a an image array and label array and saves the images as .png files with the correct labels
def save_as_png(img, lab):
    print("Creating Png's....")


# Using the Smaller Set First for quicker processing...
labels = read_labels_from_file("data/t10k-labels-idx1-ubyte.gz")
images = read_images_from_file("data/t10k-images-idx3-ubyte.gz")

# Pass Both Arrays into the save function
save_as_png(labels, images)
