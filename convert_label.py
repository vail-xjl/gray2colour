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

# Pascal voc2012着色板，如若需要请替换为其他数据集着色板
palette = [0, 0, 0, 128, 0, 0, 0, 128, 0, 128, 128, 0, 0, 0, 128, 128, 0, 128, 0, 128, 128, 128, 128, 128,
           64, 0, 0, 192, 0, 0, 64, 128, 0, 192, 128, 0, 64, 0, 128, 192, 0, 128, 64, 128, 128, 192, 128, 128,
           0, 64, 0, 128, 64, 0, 0, 192, 0, 128, 192, 0, 0, 64, 128, 128, 64, 128, 0, 192, 128, 128, 192, 128,
           64, 64, 0, 192, 64, 0, 64, 192, 0, 192, 192, 0]

# 需要转换图像的路径，必填
file_path = ""
# 转换完成后的路径，选填，默认保存到当前目录下的【finished_labels】文件夹
save_path = "./finished_labels"


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
