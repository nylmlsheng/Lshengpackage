# 关于Python-个人开源包Lshengpackage说明

个人博客：https://lsheng0-0.github.io

作者：凉笙

声名：个人学习开源，仅供学习参考，非商业用途。

自行下载食用：

```python
pip install Lshengpackage
```



> ###关于Command_adb相关模块的调用介绍
>

```python
# -*- coding: UTF-8 -*-
from Lshengpackage.Command_adb import command #调用模块

com = command()		#调用类
com.star()      #开始adb进程
com.kill()      #结束adb进程
com.dev()       #查看当前链接设备
com.log()       #查看日志
com.up('file_name','path_phone')    #file_name:上传文件的名称，需要带文件后缀，path_phone：手机文件路径/sdcard/..
com.down('file_name')   #下载：file_name;为文件名称，需要带文件后缀
com.scr('pic_name')     #屏幕截图保存到手机根目录/sdcard/..，保存图片的名称.默认png格式
com.install('apk_name')     #安装程序：无需后缀，默认apk文件安装
com.uninstall('apk_name')   #卸载程序：无需后缀，默认apk文件卸载
com.video_scr('video_name')     #屏幕录制：保存视频到手机根目录/sdcard/..,名称,默认mp4格式
```

