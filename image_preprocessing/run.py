import math
import os
import Mylarge
from Mylarge import large1, large2, large3, large4, large5, large6, large7, large8

if __name__ == "__main__":
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
            if y == 0:
                continue

            large_name = "large{}".format(y)
            print(large_name)
            f = getattr(Mylarge, large_name)
            f(root_path, save_path)