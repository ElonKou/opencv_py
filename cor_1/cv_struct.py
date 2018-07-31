#!/usr/bin/env python3  
# encoding: utf-8   

""" 
@author: Elon kou 
@contact: koudongliang@regiontec.com 
@file: struct.py 
@time: 18-7-30 下午6:38 
"""
import cv2
import numpy as np

if __name__ == "__main__":
    image = cv2.imread("../image/cat.png", 0)
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # element = np.narrage(12).reshape(3, 4)
    element = np.array([[1, 2, 1], [1, 1, 1], [3, 1, 1], [2, 2, 2]])
    dilate = cv2.dilate(image, element)
    erode = cv2.erode(image, element)

    # result = cv2.absdiff(dilate, erode)
    # retval, result = cv2.threshold(result, 50, 255, cv2.THRESH_BINARY)
    # result = cv2.bitwise_not(result)
    # cv2.imshow("result", result)
    cv2.imshow("result", dilate)
    cv2.imshow("result_2", erode)
    cv2.waitKey(0)
