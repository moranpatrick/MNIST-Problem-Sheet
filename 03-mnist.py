#  * Mnist Problem Sheet *
# Problem 3 - Output the image files as PNGs
# Use Python to output the image files as PNGs, saving them in a subfolder in your repository. 
# Name the images in the format train-XXXXX-Y.png or test-XXXXX-Y.png where XXXXX is the image number 
# (where it occurs in the data file) and Y is its label. For instance, the five-thousandth training image 
# is labelled 2, so its file name should be train-04999-2.png. Note the images are indexed from 0, so the 
# five-thousandth image is indexed as 4999. See below for an example of it. Commit these image files to GitHub.

# Author - Patrick Moran g00179039
import gzip # open gzip file
import numpy as np
import PIL.Image as pil # into pil array

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
def save_as_png(lab, img):
    # Counter 
    i = 0
    # Loop through the array of images
    for img in img:
        pngImg = img # Create a copy
        # convert img array to pngImg using numpy so pil can be used on it.
        pngImg = np.array(pngImg)
        # Gives us a monochromatic image. Allows the retrieval of the RGB values.
        pngImg = pil.fromarray(pngImg)
        # Convert to an RGB Image
        pngImg = pngImg.convert('RGB')
        # Save the png file in the folder png_files and the image number and corrosponding label
        pngImg.save("png_files/test-" + str(i) + "-" + str(lab[i]) + ".png")
        i += 1


# Read in the images and labels in an array data structure
labels = read_labels_from_file("data/train-labels-idx1-ubyte.gz")
images = read_images_from_file("data/train-images-idx3-ubyte.gz")

# Pass Both Arrays into the save function to save all the png files
save_as_png(labels, images)


