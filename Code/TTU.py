import cv2
import os
import matplotlib.pyplot as plt
import numpy as np


def equalize_histogram(image):
    if len(image.shape) == 3 and image.shape[2] == 3:  # Check if the image is color (BGR)
        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image
    
    # Equalize histogram
    equalized = cv2.equalizeHist(gray)
    
    return equalized

def plot_histogram(images, title):
    plt.figure(figsize=(8, 4))
    for image in images:
        plt.hist(image.flatten(), 256, [0, 256], alpha=0.5)

    plt.title(title)
    # plt.legend(['Image 1', 'Image 2', 'Image 3'])  # Adjust the legend based on the number of images
    plt.show()

def process_images(folder_path):
    # Create output directory
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    # Dictionary to store images based on category
    category_images = {'R': [], 'G': [], 'B': []}
    
    # Loop through images in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png')):
            # Read image
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)
            
            # Check image characteristics
            print(f'Image: {filename}, Shape: {image.shape}')
            
            # Separate channels
            b, g, r = cv2.split(image)
            
            # Process images based on channel prefix
            if filename.startswith('R'):
                r_equalized = equalize_histogram(r)
                category_images['R'].append(r_equalized)
            elif filename.startswith('G'):
                g_equalized = equalize_histogram(g)
                category_images['G'].append(g_equalized)
            elif filename.startswith('B'):
                b_equalized = equalize_histogram(b)
                category_images['B'].append(b_equalized)
    
    # Plot histograms for each category
    for category, images in category_images.items():
        plot_histogram(images, f'{category} Histogram')

# Provide the path to the folder containing the images
folder_path = r'C:\Users\Vatsla Adhikari\Downloads\10'

process_images(folder_path)
