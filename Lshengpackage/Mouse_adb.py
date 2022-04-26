# -*- coding:utf-8 -*-
# !/usr/bin/env python
import os


class mouse:
    def __init__(self, tap_work, swip_work):
        self.tap_work = tap_work
        self.swip_work = swip_work

    def tap_work(self, x, y):
        os.system('adb shell input tap {} {}'.format(x, y))

    def swip_work(self, x, y, x2, y2):
        os.system('adb shell input swipe {} {} {} {}'.format(x, y, x2, y2))
