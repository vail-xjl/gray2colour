#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Time    : 2022/8/31 15:54
# @File    : convert_label.py
# @Author  : Xue Jinlong
from PIL import Image
from tqdm import tqdm
import numpy as np
import os

palette = [0, 0, 0, 128, 0, 0, 0, 128, 0, 128, 128, 0, 0, 0, 128, 128, 0, 128, 0, 128, 128, 128, 128, 128,
           64, 0, 0, 192, 0, 0, 64, 128, 0, 192, 128, 0, 64, 0, 128, 192, 0, 128, 64, 128, 128, 192, 128, 128,
           0, 64, 0, 128, 64, 0, 0, 192, 0, 128, 192, 0, 0, 64, 128, 128, 64, 128, 0, 192, 128, 128, 192, 128,
           64, 64, 0, 192, 64, 0, 64, 192, 0, 192, 192, 0]
threshold = "0.5"
file_path = "/home/imu_zhengyuan/xjl/eps/PATH/TO/SAVE_{}/voc12_eps/result/cam_png".format(threshold)
save_path = "./finished_labels_{}".format(threshold)


def gen_image(file_name):
    image = Image.open(os.path.join(file_path, file_name))
    img = np.asarray(image)
    out = Image.fromarray(np.uint8(img), mode='P')
    out.putpalette(palette)
    out_name = os.path.join(save_path, file_name)
    out.save(out_name)


def main():
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    files = os.listdir(file_path)
    for file in tqdm(files):
        gen_image(file)
    print("finished!")


if __name__ == '__main__':
    main()
