#-*- coding:utf-8 -*-
"""
对文件或目录进行重命名
"""


from ._util import *
from .Move import mv





def rename(src,des):
    """
    重命名
    :param src: 源文件或目录
    :param des: 目标文件或目录
    :return:
    """
    mv(src,des)



def addPrefix(src,prefix):
    """
    添加前缀
    :param src: 源文件路径
    :param prefix: 前缀名称
    :return:
    """
    src_dir, src_name = os.path.split(src)
    new_name = prefix + src_name
    des = os.path.join(src_dir, new_name)
    mv(src, des)


def addSuffix(src, suffix):
    """
    添加尾缀
    :param src: 源文件路径
    :param prefix: 尾缀名称
    :return:
    """
    src_dir, src_name = os.path.split(src)
    name, suf = os.path.splitext(src_name)
    new_name = name + suffix + suf
    des = os.path.join(src_dir, new_name)
    mv(src, des)
