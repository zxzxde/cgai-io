#-*- coding:utf-8 -*-
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