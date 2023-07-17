# -*- coding: UTF-8 -*-

# 检索目录下文件
import os
import pandas as pd
global road


# 找文件
def search_it(paths, filename):
    
    global road  # 表明这里的road是全局变量road
    
    # 检查给定路径是否存在,不存在会因为报错而退出
    try:
        file_lis = os.listdir(paths)
    except:
        return False
    
    # 获取文件路径列表,暴力就是在所有的文件路径中进行比对
    file_lis = os.listdir(paths)
    
    if file_lis.__contains__(filename):  # 判断是否在当前路径下
        # 控制台输出路劲
        road = os.path.join(paths, filename)
        # 如果找到，返回True
        return True
    else:  # 不在就打开其下的文件夹,继续往下找
        for item in file_lis:
            # 递归的查找这个文件
            if search_it(os.path.join(paths, item), filename):
                return True
        return False


def search_in_csv(filename):
    pa = pd.read_csv('path_.csv')
    for i in pa:
        if i.split('|')[0] == filename:
            path = i.split('|')[1]
            return path


def _find_file_path(paths, filename):
    if not search_it(paths, filename):
        return False
    else:
        global road
        data_ = filename + '|' + road
        data = [data_]
        scr = pd.DataFrame(data=data)
        scr.to_csv('path_.csv', index=False, header=False)
        return road


# 首次找出路径并保存到存档，会需要点时间
def searchfile_path(paths, filename):
    if os.path.exists('path_.csv'):
        path = search_in_csv(filename)
        if path:
            return path
        else:
            _find_file = _find_file_path(paths, filename)
            if _find_file:
                return _find_file
            else:
                return False
    
    else:
        _find_file = _find_file_path(paths, filename)
        if _find_file:
            return _find_file
        else:
            return False
