# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 11:47:37 2023

@author: Hitika dalwadi
"""

from skimage import io, util
import skimage.color
import skimage.filters
import glob
from tensorflow.keras.models import load_model
import os
import numpy as np
from skimage.transform import resize
from skimage.io import imread, imshow
import cv2

IMG_WIDTH = 128
IMG_HEIGHT = 128
IMG_CHANNELS = 3

TRAIN_PATH = 'images/train_images/train/'
# TRAIN_PATH = 'images/train_images/'
TRAIN_MASK = 'images/train_images/mask'
TEST_PATH = 'images/test/'

num = len([f for f in os.listdir(TRAIN_PATH) if os.path.isfile(os.path.join(TRAIN_PATH, f))])

print("Number of images in directory:", num)

# test images
X_test = np.zeros((num, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)
sizes_test = []

print('Resizing test images') 
for n, id_ in zip(range(num), os.listdir(TEST_PATH)):
    path = TEST_PATH + id_
    print(path)
    img = imread(path)[:,:,:IMG_CHANNELS]
    sizes_test.append([img.shape[0], img.shape[1]])
    img = resize(img, (IMG_HEIGHT, IMG_WIDTH), mode='constant', preserve_range=True)
    X_test[n] = img

for img in X_test:
    cv2.imshow('Original Image',img)
    cv2.waitKey(50) 


# Release the window
cv2.destroyAllWindows()

loaded_model = load_model("Semantic_instrument_seg.h5")
loaded_model.summary()

Z = loaded_model.predict(X_test)


abc = Z[120]
imshow(abc)

for i in Z:
    cv2.imshow('Model Image',i)
    cv2.waitKey(50) 
# Release the window
cv2.destroyAllWindows()  