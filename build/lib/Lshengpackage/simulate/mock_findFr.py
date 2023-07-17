# -*- coding: UTF-8 -*-
import pytesseract
from PIL import Image


# tesseract.exe所在的文件路径
def fr(img):
    # 读取图片
    img = Image.open(img)
    config = r'-l chi_sim+eng --psm 6'
    frc = pytesseract.image_to_string(img, config=config)
    return frc
