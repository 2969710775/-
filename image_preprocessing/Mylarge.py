import math
import os
import numpy as np
from cv2 import cv2
from lage import Scale, Move, sp_noise, Rotate, AffineTrans2, AffineTrans3

def large1(root_path, save_path):

    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = lage.Scale(img_i)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_Scale.jpg")
    #
    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = lage.Move(img_i)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_Move.jpg")
    #
    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = lage.sp_noise(img_i, proportion=0.05)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_sp_noise.jpg")
    #
    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = lage.Rotate(img_i, angle=15)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"rotate_15.jpg")
    #
    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = lage.Rotate(img_i, angle=-30)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"rotate_-30.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:
            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = AffineTrans2(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Affine2.jpg")

    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = lage.Scale(img_i, 1.2)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Scale1.2.jpg")
    #
    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = lage.AffineTrans3(img_i)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Affine3.jpg")

def large2(root_path, save_path):

    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = Scale(img_i)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_Scale.jpg")
    #
    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = Move(img_i)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_Move.jpg")
    #
    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = sp_noise(img_i, proportion=0.05)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_sp_noise.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Rotate(img_i, angle=15)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"rotate_15.jpg")

    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = Rotate(img_i, angle=-30)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"rotate_-30.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:
            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = AffineTrans2(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Affine2.jpg")

    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = Scale(img_i, 1.2)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Scale1.2.jpg")
    #
    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = AffineTrans3(img_i)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Affine3.jpg")

def large3(root_path, save_path):

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Scale(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_Scale.jpg")

    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = Move(img_i)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_Move.jpg")
    #
    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = sp_noise(img_i, proportion=0.05)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_sp_noise.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Rotate(img_i, angle=15)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"rotate_15.jpg")

    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = Rotate(img_i, angle=-30)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"rotate_-30.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:
            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = AffineTrans2(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Affine2.jpg")

    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = Scale(img_i, 1.2)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Scale1.2.jpg")
    #
    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = AffineTrans3(img_i)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Affine3.jpg")

def large4(root_path, save_path):

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Scale(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_Scale.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Move(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_Move.jpg")

    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = sp_noise(img_i, proportion=0.05)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_sp_noise.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Rotate(img_i, angle=15)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"rotate_15.jpg")

    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = Rotate(img_i, angle=-30)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"rotate_-30.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:
            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = AffineTrans2(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Affine2.jpg")

    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = Scale(img_i, 1.2)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Scale1.2.jpg")
    #
    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = AffineTrans3(img_i)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Affine3.jpg")

def large5(root_path, save_path):

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Scale(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_Scale.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Move(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_Move.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = sp_noise(img_i, proportion=0.05)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_sp_noise.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Rotate(img_i, angle=15)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"rotate_15.jpg")

    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = Rotate(img_i, angle=-30)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"rotate_-30.jpg")
    #
    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:
            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = AffineTrans2(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Affine2.jpg")

    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = Scale(img_i, 1.2)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Scale1.2.jpg")
    #
    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = AffineTrans3(img_i)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Affine3.jpg")

def large6(root_path, save_path):

    # for a, b, c in os.walk(root_path, topdown=False):
        # for file_i in c:
        #
        #     file_i_path = os.path.join(a, file_i)
        #     print(file_i_path)
        #     img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
        #
        #     img_i = Scale(img_i)
        #     cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_Scale.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Move(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_Move.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = sp_noise(img_i, proportion=0.05)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_sp_noise.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Rotate(img_i, angle=15)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"rotate_15.jpg")

    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = Rotate(img_i, angle=-30)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"rotate_-30.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:
            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = AffineTrans2(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Affine2.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:
            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Scale(img_i, 1.2)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Scale1.2.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:
            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = AffineTrans3(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Affine3.jpg")

def large7(root_path, save_path):

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Scale(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_Scale.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Move(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_Move.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = sp_noise(img_i, proportion=0.05)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_sp_noise.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Rotate(img_i, angle=15)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"rotate_15.jpg")

    # for a, b, c in os.walk(root_path, topdown=False):
    #     for file_i in c:
    #
    #         file_i_path = os.path.join(a, file_i)
    #         print(file_i_path)
    #         img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)
    #
    #         img_i = Rotate(img_i, angle=-30)
    #         cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"rotate_-30.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:
            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = AffineTrans2(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Affine2.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:
            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Scale(img_i, 1.2)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Scale1.2.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:
            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = AffineTrans3(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Affine3.jpg")

def large8(root_path, save_path):
    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Scale(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_Scale.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Move(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_Move.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = sp_noise(img_i, proportion=0.05)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"_sp_noise.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Rotate(img_i, angle=15)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"rotate_15.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:

            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Rotate(img_i, angle=-30)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path+"\\"+file_i+"rotate_-30.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:
            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = AffineTrans2(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Affine2.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:
            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = Scale(img_i, 1.2)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Scale1.2.jpg")

    for a, b, c in os.walk(root_path, topdown=False):
        for file_i in c:
            file_i_path = os.path.join(a, file_i)
            #print(file_i_path)
            img_i = cv2.imdecode(np.fromfile(file_i_path, dtype=np.uint8), 1)

            img_i = AffineTrans3(img_i)
            cv2.imencode('.jpg', img_i)[1].tofile(save_path + "\\" + file_i + "Affine3.jpg")

if __name__ == "__main__":
    path = "E:\\binary_data"
    count = 0
    total = 0

    for a, b, c in os.walk(path, topdown=False):
        count = count+1
        print(a)
        print(len(c))
        total = total + len(c)
    print(count, total)