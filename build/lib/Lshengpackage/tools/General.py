# !/usr/bin/env python
# -*-coding:utf-8 -*-


import time
import random
import pyautogui
import pyperclip


# 随机数等待时间
class Delay:
    @classmethod
    def delay(cls, rand_start_time=0.3, rand_end_time=0.8):
        """
        随机延迟, 默认 0.5 ~ 1 之间随机
        :return:
        """
        random.seed(time.time())
        rand_time = random.uniform(rand_start_time, rand_end_time)
        time.sleep(rand_time)


# 模拟输入法中文操作
class Enter_Ch:
    @classmethod
    def insert(cls,sub):
        """
        :param sub: 需要打印的内容
        :type sub: str
        :return:
        :rtype:
        """
        pyperclip.copy(sub)
        pyautogui.hotkey('ctrl', 'v')
