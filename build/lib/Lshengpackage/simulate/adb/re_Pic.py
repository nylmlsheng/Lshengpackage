# -*coding:utf-8 -*-
# !/usr/bin/env python
import os
import pickle
from collections import defaultdict
from PIL import Image
from Lshengpackage.simulate.mock_findPic import find_image
from Lshengpackage.tools.Loading import load_click, load, insclick


def start_picdata(pypath):
    global image_data
    with open(pypath, 'rb') as f:
        image_data = pickle.load(f)


def read_img(path, img_name):
    # 读取py的图片并缓存为临时文件
    img_data = image_data[img_name][0]
    img = Image.new(mode='RGB', size=(img_data['width'], img_data['height']))
    img.putdata(img_data['pixel_values'])
    img.save(path + 'public.png')


def refind_image(fol_path, path, img_name, _system=None, int_x=None, int_y=None, width=0, high=None, screenshot=True):
    read_img(path, img_name)
    pub = find_image(fol_path, path + 'public.png', _system, int_x, int_y, width, high, screenshot)
    if pub is not None:
        return pub


def refiloadclick_image(fol_path, path, img_name, _system=None, int_x=None, int_y=None, width=0, high=None, screenshot=True):
    read_img(path, img_name)
    pub = load_click(fol_path, path + 'public.png', _system, int_x, int_y, width, high, screenshot)  # 退出当前页再找
    if pub is True:
        return True
    else:
        return False


def refiload_image(fol_path, path, img_name, _system=None, int_x=None, int_y=None, width=0, high=None, screenshot=True):
    read_img(path, img_name)
    pub = load(fol_path, path + 'public.png', _system, int_x, int_y, width, high, screenshot)  # 退出当前页再找
    if pub is not None:
        return pub


def refiinsclick_image(fol_path, path, img_name, _system=None, int_x=None, int_y=None, width=0, high=None, screenshot=True):
    read_img(path, img_name)
    pub = insclick(fol_path, path + 'public.png', _system, int_x, int_y, width, high, screenshot)  # 退出当前页再找
    if pub is True:
        return True
    else:
        return False


# 转换文件夹下的jpg或者png图片文件为py文件
def pic_to_py(folpath, pypath):
    # pic_to_py(folpath='adb/pic/dingding', pypath='adb/image_data.py')

    # 需要转换的图片目录
    image_dir = folpath

    # 遍历目录，将每张图片转换为像素数据
    image_data = defaultdict(list)
    for filename in os.listdir(image_dir):
        # 只处理jpg和png格式的图片
        if filename.endswith('.jpg') or filename.endswith('.png'):
            filepath = os.path.join(image_dir, filename)
            with Image.open(filepath) as img:
                width, height = img.size
                # 获取所有像素的RGB值
                pixel_values = list(img.getdata())
                print(filename.split('.')[0])
                image_data[filename.split('.')[0]].append(
                    {'width': width, 'height': height, 'pixel_values': pixel_values})

    # 将像素数据保存到Python数据文件
    with open(pypath, 'wb') as f:
        pickle.dump(image_data, f)
