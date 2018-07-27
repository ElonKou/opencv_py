#!/usr/bin/env python3  
# encoding: utf-8   

""" 
@author: Elon kou 
@contact: koudongliang@regiontec.com 
@file: load_image.py 
@time: 18-7-27 下午4:31 
"""

import cv2

if __name__ == "__main__":
    img = cv2.imread('../image/cat.png')
    # img[:, :, 0] *= 50
    # img[:, :, 1] -= 20
    # img[:, :, 2] -= 20

    # img[img > 220] = 0

    b, g, r = cv2.split(img)
    # b[b > 200] = 255
    # cv2.imshow("Image", b)

    mer = cv2.merge([b, g, r])
    # cv2.imshow("Image", mer)


    # gray = b * 0.114 + r * 0.587 + r * 0.299
    gray = b * 0.114 + r * 0.587 + r * 0.299
    # cv2.imshow("Image", gray)
    cv2.waitKey()
