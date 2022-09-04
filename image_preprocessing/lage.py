import math
import random

import cv2.cv2 as cv2
import os
import numpy as np



# 水平翻转
# def Horizontal(image):
#     return cv2.flip(image, 1, dst=None)

# 垂直翻转
# def Vertical(image):
#     return cv2.flip(image, 0, dst=None)

# 平移
def Move(img, x=10, y=15):
    img_info = img.shape
    height = img_info[0]
    width = img_info[1]
    mat_translation = np.float32([[1, 0, x], [0, 1, y]])
    dst = cv2.warpAffine(img, mat_translation, (width, height))
    return dst


# 图像缩放
def Scale(image, scale=0.6):
    return cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)


# 旋转，R可控制图片放大缩小
def Rotate(image, angle=15, scale=1):
    w = image.shape[0]
    h = image.shape[1]
    m = cv2.getRotationMatrix2D((w / 2, h / 2), angle, scale)
    return cv2.warpAffine(image, m, (w, h))


# 变暗
def Darker(image, percetage=0.9):
    image_copy = image.copy()
    w = image.shape[0]
    h = image.shape[1]
    for xi in range(0, w):
        for yi in range(0, h):
            image_copy[xi, yi, 0] = np.clip(int(image[xi, yi, 0] * percetage), a_max=255, a_min=0)
            image_copy[xi, yi, 1] = np.clip(int(image[xi, yi, 1] * percetage), a_max=255, a_min=0)
            image_copy[xi, yi, 2] = np.clip(int(image[xi, yi, 2] * percetage), a_max=255, a_min=0)
    return image_copy


# 变亮
def Brighter(image, percetage=1.1):
    image_copy = image.copy()
    w = image.shape[0]
    h = image.shape[1]
    for xi in range(0, w):
        for yi in range(0, h):
            image_copy[xi, yi, 0] = np.clip(int(image[xi, yi, 0] * percetage), a_max=255, a_min=0)
            image_copy[xi, yi, 1] = np.clip(int(image[xi, yi, 1] * percetage), a_max=255, a_min=0)
            image_copy[xi, yi, 2] = np.clip(int(image[xi, yi, 2] * percetage), a_max=255, a_min=0)
    return image_copy


# 添加椒盐噪声
def sp_noise(noise_img, proportion):
    '''
    添加椒盐噪声
    proportion的值表示加入噪声的量，可根据需要自行调整
    return: img_noise
    '''
    height, width = noise_img.shape[0], noise_img.shape[1]  # 获取高度宽度像素值
    num = int(height * width * proportion)  # 一个准备加入多少噪声小点
    for i in range(num):
        w = random.randint(0, width - 1)
        h = random.randint(0, height - 1)
        if random.randint(0, 1) == 0:
            noise_img[h, w] = 0
        else:
            noise_img[h, w] = 255
    return noise_img


# 高斯噪声
def gaussian_noise(img, mean=0, sigma=1):
    # 将图片灰度标准化
    img = img / 255
    # 产生高斯 noise
    noise = np.random.normal(mean, sigma, img.shape)
    # 将噪声和图片叠加
    gaussian_out = img + noise
    # 将超过 1 的置 1，低于 0 的置 0
    gaussian_out = np.clip(gaussian_out, 0, 1)
    # 将图片灰度范围的恢复为 0-255
    gaussian_out = np.uint8(gaussian_out * 255)
    # 将噪声范围搞为 0-255
    # noise = np.uint8(noise*255)
    return gaussian_out  # 这里也会返回噪声，注意返回值


# 模糊
def Blur(img):
    blur = cv2.GaussianBlur(img, (7, 7), 1.5)
    return blur


# 图像扭曲
def AffineTrans1(img):
    rows, cols, _ = img.shape
    #
    # pts1 = np.float32([[0, 0], [0, 30], [30, 30], [30, 0]])
    # pts2 = np.float32([[5, 0], [-5, 30], [25, 30], [35, 0]])
    # warp_mat = cv2.getPerspectiveTransform(pts1, pts2)
    # dst = cv2.warpPerspective(img, warp_mat, (rows, cols))

    pts1 = np.float32([[20, 20], [30, 20], [20, 0]])  # 源图像中的三角形顶点坐标
    pts2 = np.float32([[20, 20], [30, 20], [25, 0]])  # 目标图像中的三角形顶点坐标
    M = cv2.getAffineTransform(pts1, pts2)  # 计算出仿射变换矩阵
    dst = cv2.warpAffine(img, M, (cols, rows))  # 应用仿射变换
    return dst

def AffineTrans2(img):
    rows, cols, _ = img.shape
    #
    # pts1 = np.float32([[0, 0], [0, 30], [30, 30], [30, 0]])
    # pts2 = np.float32([[5, 0], [-5, 30], [25, 30], [35, 0]])
    # warp_mat = cv2.getPerspectiveTransform(pts1, pts2)
    # dst = cv2.warpPerspective(img, warp_mat, (rows, cols))

    pts1 = np.float32([[20, 0], [30, 0], [20, 20]])  # 源图像中的三角形顶点坐标
    pts2 = np.float32([[20, 0], [30, 0], [25, 20]])  # 目标图像中的三角形顶点坐标
    M = cv2.getAffineTransform(pts1, pts2)  # 计算出仿射变换矩阵
    dst = cv2.warpAffine(img, M, (cols, rows))  # 应用仿射变换
    return dst

def AffineTrans3(img):
    rows, cols, _ = img.shape
    #
    pts1 = np.float32([[0, 0], [0, 30], [30, 30], [30, 0]])
    pts2 = np.float32([[5, 0], [-5, 30], [25, 30], [35, 0]])
    warp_mat = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, warp_mat, (rows, cols))

    # pts1 = np.float32([[20, 20], [30, 20], [20, 0]])  # 源图像中的三角形顶点坐标
    # pts2 = np.float32([[20, 20], [30, 20], [25, 0]])  # 目标图像中的三角形顶点坐标
    # M = cv2.getAffineTransform(pts1, pts2)  # 计算出仿射变换矩阵
    # dst = cv2.warpAffine(img, M, (cols, rows))  # 应用仿射变换
    return dst

if __name__ == "__main__":
    name = "百"
    path = "E:\\binary_data"

    for root, dirs, files in os.walk(path, topdown=False):

        if root == "E:\\binary_data":
            break
        print(root)
        save_path = root_path = root
        if len(files) < 256:
            x = len(files)
            y = int(math.log(int(256 / x), 2) + 0.5)
            print(y, x * 2 ** y)

            large_name = "large{}()".format(y)
            print(large_name)
            eval(Mylarge.large_name)()
