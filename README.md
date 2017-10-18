# MNIST Problem Sheet
## How to use this repository?
### Step 1: Install Python
Step 1 - Download Anaconda 3 from their website [here](https://www.anaconda.com/download/).  
Step 2: Choose a Text editor of your choice. I recommend [Visual Studio Code](https://code.visualstudio.com/download).

### Step 2: Clone Repository
* Open a command prompt.  
* cd into any directory.    
* Then type:  
> git clone https://github.com/moranpatrick/MNIST-Problem-Sheet   

* Then cd into that directory.
### Step 3: Download The MNIST data Set
* Go to the website and download the training set images and training set labels. They can be found [here](http://yann.lecun.com/exdb/mnist/).
* At the root of the project you cloned from github, create a folder called data and copy those downloaded files to there.

### Step 4: Running the python Files
* If your using VS Code open the Command Terminal by pressing Ctrl + '.  
* Run each script by typing into the command terminal the following.  
> python name_of_file.py  

So to run the first problem simply type:  
> python 01-mnist.py 

* If the text editor your using does not have a command terminal simply open anaconda command prompt, change directory to where the python scripts are located and repeat the second point above in Step 4.  

## Problem set: Read the MNIST data files

These problems relate to the famous MNIST data set.The files are in a bespoke format, as described on the [website](http://yann.lecun.com/exdb/mnist/).

## 1. Read the data files

Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.

## 2. Output an image to the console

Output the third image in the training set to the console. Do this by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol.

## 3. Output the image files as PNGs

Use Python to output the image files as PNGs, saving them in a subfolder in your repository. Name the images in the format train-XXXXX-Y.png or test-XXXXX-Y.png where XXXXX is the image number (where it occurs in the data file) and Y is its label. For instance, the five-thousandth training image is labelled 2, so its file name should be train-04999-2.png. Note the images are indexed from 0, so the five-thousandth image is indexed as 4999. See below for an example of it. Commit these image files to GitHub.