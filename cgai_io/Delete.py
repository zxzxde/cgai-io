# -*- coding:utf-8 -*-
"""
对不同平台提供原生快速删除方法

例：
>>>import os
>>>from cgai_io.Delete import delfile,deldir,delall
>>>
>>># #删除文件
>>># path = r'\\192.168.1.248\3d\temp\a\cmd_mac.py'
>>># delfile(path)
>>>
>>>
>>># #删除文件夹
>>># path = r'D:\BaiduNetdiskDownload\AA'
>>># deldir(path,keep_dir=True)
>>>
>>>
>>>#无论文件或文件夹都直接删除
>>># path = r'D:\BaiduNetdiskDownload\ktk_103024'
>>># delall(path)
>>>


"""

import os
import sys

def iswin():
    platform = sys.platform
    if platform == 'win32':
        return True
    else:
        return False

def isfile(_path):
    if os.path.isfile(_path):
        return True
    else:
        return False

def isdir(_path):
    if os.path.isdir(_path):
        return True
    else:
        return False


def delfile(file_path):
    """
    删除文件
    :param file_path: 文件路径
    :return:
    """
    if iswin():
        if isfile(file_path):
            os.system('"del /f /s /q "%s"' % (file_path.replace('/','\\')))
        else:
            print("删除对象非文件")
    else:
        if file_path not in ['/','/*']:
            if isfile(file_path):
                os.system("rm -rf %s"% (file_path.replace('\\','/')))
            else:
                print("删除对象非文件")

def deldir(dir_path,keep_dir=False):
    """
    删除文件目录
    :param dir_path: 文件目录路径
    :param keep_dir: 保持源目录结构
    :return:
    """
    if iswin():
        if isdir(dir_path):
            if keep_dir:
                os.system('"del /f /s /q "%s"' % (dir_path.replace('/', '\\')))
            else:
                os.system('"rd  /s /q "%s"' % (dir_path.replace('/', '\\')))
        else:
            print("删除对象非文件目录")
    else:
        if isdir(dir_path):
            if dir_path not in ['/','/*']:  #禁止删全家
                if keep_dir:
                    os.system('"find path -type f -exec rm {} \;"'.format(dir_path.replace('\\','/')))
                else:
                    os.system("rm -rf %s"% (dir_path.replace('\\','/')))
        else:
            print("删除对象非文件目录")

def delall(path,keep_dir=False):
    """
    无论文件还是文件目录都删除
    :param path:
    :param keep_dir: 保持源目录结构
    :return:
    """
    if iswin():
        if keep_dir:
            os.system('"del /f /s /q "%s"' % (path.replace('/', '\\')))
        else:
            os.system('"rd  /s /q "%s"' % (path.replace('/', '\\')))
    else:
        if path not in ['/','/*']:
            if keep_dir:
                os.system('"find path -type f -exec rm {} \;"'.format(path.replace('\\','/')))
            else:
                os.system("rm -rf %s"% (path.replace('\\','/')))