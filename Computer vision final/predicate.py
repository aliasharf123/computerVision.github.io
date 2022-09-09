import functools

import cv2
import os
import numpy as np


def detect_boxes(image_path):
    image = cv2.imread(image_path, 0)
    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 45, 15)
    _, labels = cv2.connectedComponents(thresh)
    mask = np.zeros(thresh.shape, dtype="uint8")
    total_pixels = image.shape[0] * image.shape[1]
    lower = total_pixels // 70
    upper = total_pixels // 20
    for (i, label) in enumerate(np.unique(labels)):
        if label == 0:
            continue
        labelMask = np.zeros(thresh.shape, dtype="uint8")
        labelMask[labels == label] = 255
        numPixels = cv2.countNonZero(labelMask)

        if numPixels > lower and numPixels < upper:
            mask = cv2.add(mask, labelMask)



    cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(len(cnts))
    for cntr in cnts:
        x, y, w, h = cv2.boundingRect(cntr)
        if(h > 100):
          cv2.rectangle(mask, (x, y), (x + w, y + h), (124,252,0), 3)
    cv2.imshow("result", mask)
    return "Done"


cv2.waitKey(0)