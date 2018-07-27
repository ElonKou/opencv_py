#!/usr/bin/env python3  
# encoding: utf-8   

""" 
@author: Elon kou 
@contact: koudongliang@regiontec.com 
@file: grey.py 
@time: 18-7-27 下午5:19 
"""
import cv2
import numpy as np

if __name__ == "__main__":
    # img = cv2.imread('../image/cat.png')
    # grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Cat", grey)
    # cv2.imwrite("../image/cat_grey.png", grey)
    # cv2.waitKey()

    # a = np.arange(9).reshape([3, 3])
    # b = [[1.1, 0, 1], [1, 1, 0], [0, 1, 1]]
    # b = np.matrix(b).T
    # a = np.matrix(a)
    # print(a)
    # print(b)
    # print(a * b)

    grey = cv2.imread('../image/cat_grey.png')
    a = [[1, 1, 0], [2, 0, 1], [2, 0, 0]]
    a = np.array(a)
    a.dtype = 'uint8'
    for x in range(grey.shape[1] - 2):
        for y in range(grey.shape[0] - 2):
            # print(grey[x:x + 3, y:y + 3, 0].shape)
            grey[y:y + 3, x:x + 3, 0] = grey[y:y + 3, x:x + 3, 0] * a
            cv2.imshow("cat_grey", grey)
            cv2.waitKey()
