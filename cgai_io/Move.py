#-*- coding:utf-8 -*-
"""
移动文件或目录
"""
from ._util import *


def mv(src:str,des:str):
    """
    移动文件或文件夹
    :param src: 源文件或目录
    :param des: 目标文件或目录
    :return:
    """
    if iswin():
        subprocess.Popen('move {} {}'.format(src,des))
    else:
        subprocess.Popen('mv {} {}'.format(src, des))


def mvfile(src:str,des:str):
    """
    移动文件
    :param src: 源文件
    :param des: 目标文件
    :return: 
    """
    if isfile(src):
        mv(src,des)
    else:
        raise Exception("输入非文件")

def mvdir(src:str,des:str):
    """
    移动文件目录
    :param src: 源文件目录
    :param des: 目标文件目录
    :return:
    """
    if isdir(src):
        mv(src,des)
    else:
        raise Exception("输入非文件目录")



