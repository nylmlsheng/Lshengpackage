# !/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import sys
import pyautogui
from time import sleep

from Lshengpackage.simulate.adb.Command_adb import command
from Lshengpackage.simulate.mock_findPic import find_image


# 加载
def load(fol_path, target_path, _system, int_x=None, int_y=None, width=0, high=None,
         screenshot=True):
    """
        :param img: 循环等待的值
        :type img: img
        :return: 鼠标(1,1),返回 'N'
        :rtype:
        """
    while True:
        sleep(0.1)
        iocn = find_image(fol_path, target_path, _system, int_x, int_y, width, high, screenshot)
        if iocn is not None:
            sleep(0.1)
            return iocn
        x, y = pyautogui.position()
        if x & y == 0:
            sys.exit()
            # 暂时先这样结束进程
        else:
            pass


def load_click(fol_path, target_path, _system, int_x=None, int_y=None, width=0, high=None,
         screenshot=True):
    """
    加载点击
    """
    sleep(0.1)
    iocn = load(fol_path, target_path, _system, int_x, int_y, width, high, screenshot)
    # print(iocn)
    if iocn is not None:
        if _system == 'adb':
            sleep(0.1)
            command().tap_work(int(iocn[0]), int(iocn[1]))
        else:
            sleep(0.1)
            pyautogui.click(int(iocn[0]), int(iocn[1]))
            return True
    else:
        return False


def insclick(fol_path, target_path, _system, int_x=None, int_y=None, width=0, high=None,
         screenshot=True):
    """
    加载点击
    """
    sleep(0.1)
    iocn = find_image(fol_path, target_path, _system, int_x, int_y, width, high, screenshot)
    if iocn is not None:
        sleep(0.1)
        if _system == 'adb':
            command().tap_work(int(iocn[0]), int(iocn[1]))
            return True
        else:
            pyautogui.click(int(iocn[0]), int(iocn[1]))
            return True
    else:
        return False
