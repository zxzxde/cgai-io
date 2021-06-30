# -*- coding:utf-8 -*-
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

def copyfile(src_file,des_file):
    """
    复制文件
    :param src_file: 源文件路径 
    :param des_file: 复制文件路径
    :return: 
    """
    if isfile(src_file):
        if iswin():
            os.system('copy "%s" "%s"' % (src_file, des_file))
        else:
            os.system('cp "%s" "%s"' % (src_file, des_file))
    else:
        print('复制对象非文件类型')

def copydir(src_dir,des_dir):
    """
    复制文件夹
    :param src_dir: 源目录路径
    :param des_dir:  复制文件夹路径
    :return:
    """
    if isdir(src_dir):
        if iswin():
            os.system('xcopy "%s" "%s" /s /e /v /y /i' % (src_dir, des_dir))
        else:
            os.system('cp -r "%s" "%s"' % (src_dir, des_dir))
    else:
        print('复制对象非目录类型')


