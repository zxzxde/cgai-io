# -*- coding:utf-8 -*-
"""
该脚本获取各文件信息
"""
import os

UNIT = {'KB':1024,'M':1024*1024,'G':1024*1024*1024}

def getFileSize(path,unit='M'):
    size = 0
    if os.path.isfile(path):
        s = os.path.getsize(path)
        size = s/UNIT.get(unit,1024) if s else 0
    return size



