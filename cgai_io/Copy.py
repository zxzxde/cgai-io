# -*- coding:utf-8 -*-
from ._util import *
import subprocess

def copyfile(src_file,des_file,auto_create=True,wait=False):
    """
    复制文件
    :param src_file: 源文件路径 
    :param des_file: 复制文件路径
    :param auto_create: 自动创建目录
    :param wait: 是否阻塞已等待完成
    :return:
    """
    if isfile(src_file):
        if auto_create:
            _dir = os.path.dirname(des_file)
            if not os.path.exists(_dir):
                os.makedirs(_dir)
        if iswin():
            src_file = src_file.replace('/', '\\')
            des_file = des_file.replace('/', '\\')
            # os.popen('copy "%s" "%s"' % (src_file, des_file))
            p = subprocess.Popen(['copy',src_file,des_file],shell=True)
        else:
            # os.popen('cp "%s" "%s"' % (src_file, des_file))
            p = subprocess.Popen(['cp',src_file,des_file],shell=True)
        
        if wait:
            p.wait()

    else:
        print('复制对象非文件类型')

def copydir(src_dir,des_dir,auto_create=True,wait=False):
    """
    复制文件夹
    :param src_dir: 源目录路径
    :param des_dir:  复制文件夹路径
    :param auto_create: 自动创建目录
    :param wait: 是否阻塞已等待完成
    :return:
    """
    if isdir(src_dir):
        if auto_create:
            _dir = os.path.dirname(des_dir)
            if not os.path.exists(_dir):
                os.makedirs(_dir)
        if iswin():
            src_dir = src_dir.replace('/', '\\')
            des_dir = des_dir.replace('/', '\\')
            p = subprocess.Popen(['xcopy',src_dir,des_dir,'/s','/e','/v','/y','/i'],shell=True)
        else:
            p = subprocess.Popen(['cp','-r',src_dir,des_dir],shell=True)

        if wait:
            p.wait()
    else:
        print('复制对象非目录类型')



def copyall(src,des,auto_create=True,wait=False):
    """
    复制文件或文件夹
    :param src:
    :param des:
    :param auto_create: 自动创建目录
    :param wait: 是否阻塞已等待完成
    :return:
    """
    src = src.replace('/', '\\')
    des = des.replace('/', '\\')
    p = None
    if isfile(src):
        if auto_create:
            _dir = os.path.dirname(des)
            if not os.path.exists(_dir):
                os.makedirs(_dir)
        if iswin():
            p = subprocess.Popen(['xcopy',src,des],shell=True)
        else:
            p = subprocess.Popen(['cp',src,des],shell=True)

    if isdir(src):
        _dir = os.path.dirname(des)
        if not os.path.exists(_dir):
            os.makedirs(_dir)
        if iswin():
            p = subprocess.Popen(['copy',src,des,'/s','/e','/v','/y','/i'],shell=True)
        else:
            p = subprocess.Popen(['cp','-r',src,des],shell=True)

    if p and wait:
        p.wait()