#!/usr/bin/env python3  
# encoding: utf-8   

""" 
@author: Elon kou 
@contact: koudongliang@regiontec.com 
@file: calcHist.py 
@time: 18-7-30 下午6:26 
"""

import cv2
import numpy as np


def calcAndDrawHist(image, color):
    hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256, 256, 3], np.uint8)
    hpt = int(0.9 * 256)
    for h in range(256):
        intensity = int(hist[h] * hpt / maxVal)
        cv2.line(histImg, (h, 256), (h, 256 - intensity), color)
    return histImg


if __name__ == '__main__':
    image = cv2.imread("../image/cat.png", 1)
    # hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
    # cv2.imshow("histImgB", hist)
    # cv2.waitKey()
    b, g, r = cv2.split(image)

    histImgB = calcAndDrawHist(b, [255, 0, 0])
    histImgG = calcAndDrawHist(g, [0, 255, 0])
    histImgR = calcAndDrawHist(r, [0, 0, 255])

    cv2.imshow("histImgB", histImgB)
    cv2.imshow("histImgG", histImgG)
    cv2.imshow("histImgR", histImgR)
    # cv2.imshow("Img", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
