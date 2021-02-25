import cv2
import numpy as np
import pandas as pd
from PIL import Image

# transform category here
filename = "../data/ADEChallengeData2016/annotations/training/ADE_train_00000001.png"
img = cv2.imread(filename)
print(img.shape, img.dtype)
masked = np.where(img == 4, 4, 0)
print(masked.shape, masked.dtype)
Image.fromarray(masked.astype(np.uint8)).show()
