# 关于Python-个人开源包Lshengpackage说明

个人博客：https://lsheng0-0.github.io

作者：凉笙

声名：个人学习开源，仅供学习参考，非商业用途。

> 自行下载食用：

```cmd
pip install Lshengpackage
```



> ###关于Command_adb相关模块的调用介绍(更新)
>返回值0,1,2 0为成功

```python
# -*- coding: UTF-8 -*-
from Lshengpackage.simulate.adb.Command_adb import command  # 调用模块

com = command()  # 调用类
com.star()  # 开始adb进程
com.kill()  # 结束adb进程
com.dev()  # 查看当前链接设备
com.log()  # 查看日志
com.up('file_name', 'path_phone')  # file_name:上传文件的名称，需要带文件后缀，path_phone：手机文件路径/sdcard/..
com.down('file_name')  # 下载：file_name;为文件名称，需要带文件后缀
com.scr('pic_name')  # 屏幕截图保存到手机根目录/sdcard/..，保存图片的名称.默认png格式
com.install('apk_name')  # 安装程序：无需后缀，默认apk文件安装
com.uninstall('apk_name')  # 卸载程序：无需后缀，默认apk文件卸载
com.video_scr('video_name')  # 屏幕录制：保存视频到手机根目录/sdcard/..,名称,默认mp4格式
com.cut_scr('path_pic_name', 'path') #屏幕截图到本地 path_pic_name:截图手机路径 path：本地程序图片路径
com.spec_scr('path_pic_name', 'path', 'int_x1', 'int_y1', 'int_x2', 'int_y2') # 屏幕指定范围截图到本地 path_pic_name:截图手机路径 path：本地程序图片路径
#int_x1, int_y1, int_x2, int_y2 分别是左上角和右下角的点左边,转文字用
com.tap_work('x', 'y') #模拟手动点击 x，y为坐标
com.swip_work('x', 'y', 'x2', 'y2') # 模拟手动滑动，x, y, x2, y2为第一个点到第二个点
```
> ###关于超级鹰验证码识别的调用-Python
>[注册超级鹰账号](http://www.chaojiying.com/user/reg/)

用户中心 ->软件ID ->生成软件ID

调用方法：

```python
from Lshengpackage.tools.ChaoJiYing import Verification

# 处理验证码

verify = Verification()  # 调用超级鹰模块
verify_code = verify.verification_code('超级鹰登录用户名', '超级鹰登录密码', '软件ID号', img)
# 外部请求超级鹰，img为验证码路劲图片文件
print(verify_code['pic_str'])
# 打印验证码
```

> ###找图定位、转文字模块 v3.0-3.6(更新)

```python
from Lshengpackage.simulate.mock_findFr import  fr

word = fr(img='')  #图片识字
print(word)

from Lshengpackage.simulate.mock_findPic import screen_shot,find_image
screen_shot('截图的路径','截图的名') #pc桌面截图保存图片到指定位置
find_image('获取图片文件夹', '目标图片文件夹', '目标名称.png',)  #当前页面找图,找到匹配对象位置中心点（参数对应需要寻找的图片路径名称)
#成功返回中心点坐标，否则为空值
from Lshengpackage.tools.Loading import load,load_click

#页面刷新等待，直到找到目标并点击
# 设置自动防故障功能（将鼠标移动到左上角将停止程序）
load('获取图片文件夹', '目标图片文件夹', '目标名称.png')  
#直到找到目标返回坐标值
load_click('获取图片文件夹', '目标图片文件夹', '目标名称.png')  
#找到目标坐标点击,成功范围True，失败返回False 鼠标移至（0,0）退出程序
```
> ###其他的一些工具模块 v3.6(更新)
>
```python

from Lshengpackage.tools.General import  Delay,Enter_Ch

Delay.delay() #随机等待时间

Enter_Ch.insert('需要输入的文字内容') #模拟输入中文文字

from Lshengpackage.tools.SearchFile import searchfile_path,search_it
search_it('文件路径', '文件名') #检索遍历根目录下的所有文件，找到指定文件为止
searchfile_path('文件路径', '文件名') #找到指定文件后进行缓存，下次可直接提去（可用于未指定路径文件，自搜索）

```