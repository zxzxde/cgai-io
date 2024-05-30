#-*- coding:utf-8 -*-
"""
移动文件或目录
"""
import subprocess
from ._util import *


def mv(src,des,wait=True):
    """
    移动文件或文件夹
    :param src: 源文件或目录
    :param des: 目标文件或目录
    :return:
    """
    if iswin():
        src_file = src.replace('/', '\\')
        des_file = des.replace('/', '\\')
        p = subprocess.Popen(['move',src_file,des_file],shell=True)
    else:
        p = subprocess.Popen(['mv',src_file,des_file],shell=True)

    if wait:
        p.wait()
    
def mvfile(src,des,wait=True):
    """
    移动文件
    :param src: 源文件
    :param des: 目标文件
    :return: 
    """
    if isfile(src):
        mv(src,des,wait)
    else:
        raise Exception("输入非文件")

def mvdir(src,des,wait=True):
    """
    移动文件目录
    :param src: 源文件目录
    :param des: 目标文件目录
    :return:
    """
    if isdir(src):
        mv(src,des,wait)
    else:
        raise Exception("输入非文件目录")



