import numpy as np
import math
import os

if __name__ == '__main__':
    count = 0
    for root, dirs, files in os.walk(r"D:\FilesforUseing\代码\swin_transformer\binary_data", topdown=False):
        print(files)
        count=count+1

    print(count)