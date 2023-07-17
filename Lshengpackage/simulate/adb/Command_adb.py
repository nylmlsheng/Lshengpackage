# -*coding:utf-8 -*-
# !/usr/bin/env python

from PIL import ImageFile
from PIL import Image
import os


class command:
    def dev(self):
        # 查看当前链接设备
        com = os.popen('adb devices').read()
        return com

    #
    def state(self):
        # 返回连接状态
        com = os.popen('adb get-state').read()
        return com

    #
    def connect(self, ip):
        # 连接ip+端口号
        com = os.popen('adb connect {}'.format(ip)).read()
        return com

    #
    def insert(self, text):
        com = os.system('adb shell input text {}'.format(text))  # 输入文本
        return com

    def log(self):
        # 查看日志
        com = os.popen('adb logcat').read()
        return com

    def kill(self):
        # 结束adb服务
        com = os.system('adb kill-server')
        return com

    def star(self):
        # 开始adb服务
        com = os.system('adb start-server')
        return com

    def install(self, apk_name):
        # 安装软件
        com = os.system('adb install -r {}.apk'.format(apk_name))
        return com

    def uninstall(self, apk_name):
        # 卸载
        com = os.system('adb uninstall {}.apk'.format(apk_name))
        return com

    def update(self, file_name, path_phone):
        # 上传SDCard/../..手机端路径
        com = os.system('adb push {} {}'.format(file_name, path_phone))
        return com

    def download(self, file_name):
        # 下载
        com = os.system('adb uninstall {}'.format(file_name))
        return com

    def scr(self, path_pic_name):
        # 屏幕截图到手机根目录
        com = os.system('adb shell screencap -p /sdcard/{}.png'.format(path_pic_name))
        return com

    def video_scr(self, video_name):
        # 录屏，默认mp4格式
        com = os.system('adb shell screenrecord /sdcard/{}.mp4'.format(video_name))
        return com

    def cut_scr(self, fol_path):
        # 屏幕截图到本地
        # pic_name:屏幕截图生成地址+名称，默认为手机的根目录,默认的来
        # path为文件夹目录下
        self.scr(fol_path.split('\\')[-1])
        com = os.system("adb pull /sdcard/{}.png {}".format(fol_path.split('\\')[-1], fol_path))
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        return com

    def spec_scr(self, pic_path, int_x1, int_y1, int_x2, int_y2):
        """
        指定截图保存
        左上角的点到右下角的点
        """
        self.cut_scr(pic_path)
        img = Image.open(pic_path)
        # (4)将图片验证码截取
        code_image = img.crop((int_x1, int_y1, int_x2, int_y2))
        code_image.save(pic_path)  # 原地址重写
        return True

    def tap_work(self, x, y):
        """
        模拟点击操作
        """
        com = os.system('adb shell input tap {} {}'.format(x, y))
        return com

    def swip_work(self, x, y, x2, y2):
        """
        模拟滑动操作
        """
        com = os.system('adb shell input swipe {} {} {} {}'.format(x, y, x2, y2))
        return com

    def get_ui(self, path):
        os.popen('adb shell uiautomator dump /sdcard/ui.xml')  # 获得屏幕控件信息
        re = os.popen(r'adb pull /sdcard/ui.xml {}+ui.xml'.format(path))  # 获得屏幕控件信息
        return re
