#-*- coding:utf-8 -*-
"""
打包压缩与解压文件或目录
"""
import os
import shutil
import zipfile



def pack(src,des):
    """
    打包文件或目录
    :param src: 源文件或目录
    :param des: zip路径
    :return:
    """

    if os.path.isfile(src):
        z = zipfile.ZipFile(des,"w")
        name = os.path.split(src)[1]
        z.write(src,name)
        z.close()
    elif os.path.isdir(src):
        des_dir = os.path.splitext(des)[0]
        shutil.make_archive(des_dir,'zip',root_dir=src)



def unpack(src,des_dir):
    """
    解压文件或目录
    :param src: zip路径
    :param des_dir: 解压目录
    :return:
    """
    z = zipfile.ZipFile(src,'r')
    z.extractall(des_dir)
    z.close()


