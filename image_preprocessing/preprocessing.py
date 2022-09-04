import random

import cv2.cv2 as cv2
import os
import numpy as np
import math


# OTSU二值化图片
def BinaryImage(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    tt, dst = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # dst = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 17, 3)
    # dst = otsu(img)
    return dst

# 伽马变换
def GamaTrans(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    mean = np.mean(img)
    gamma_val = math.log10(0.5) / math.log10(mean / 255)

    gamma_table = [np.power(x / 255.0, gamma_val) * 255.0 for x in range(256)]  # 建立映射表
    gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)  # 颜色值为整数
    return cv2.LUT(img, gamma_table)  # 图片颜色查表。另外可以根据光强（颜色）均匀化原则设计自适应算法。

# 非局部均值去噪
def NLM(img):
    dst = cv2.fastNlMeansDenoising(img, None, 25, 7, 21)
    return dst

# 中值滤波
def Median(img):
    dst = cv2.medianBlur(img, 5)
    return dst

if __name__ == "__main__":
    root_path = "E:\\gama_trans_data"
    save_path = "E:\\gama_trans_data"

    for a, b, c in os.walk(root_path, topdown=False):
        if not os.path.isdir(save_path + "\\" + a[-1]):
            os.mkdir(os.path.join(save_path, a[-1]))
        for file_i in c:
            file_i_path = os.path.join(a, file_i)
            print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_binary = BinaryImage(img_i)
            cv2.imencode('.jpg', img_binary)[1].tofile(save_path + "\\" + a[-1] + "\\" + file_i)
