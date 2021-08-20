#-*- coding:utf-8 -*-

import cgai_io as ci


# #复制文件
# src = r'D:\Temp\GAN.png'
# des = r'D:\Temp\GAN_bak.png'
# ci.copyfile(src,des)
# ci.copyall(src,des)


# #复制文件目录
src = r'D:\Temp\AA'
des = r'D:\Temp\C\BB'
# ci.copydir(src,des)
ci.copyall(src,des)



# #删除文件
# des = r'D:\Temp\2_bak.jpg'
# ci.delfile(des)

# # 删除文件目录
# des = r'D:\Temp\BB'
# ci.deldir(des)

# # 删除文件或目录
# des = r'D:\Temp\BB'
# ci.delall(des)

# #移动文件
# src = r'D:\Temp\AA'
# des = r'D:\Temp\BB'
# ci.mvfile(src,des)

# # 移动文件目录
# src = r'D:\Temp\AA'
# des = r'D:\Temp\testA\AA'
# ci.mvdir(src,des)

# # 移动文件或目录
# src = r'D:\Temp\testA\AA'
# des = r'D:\Temp\AA'
# ci.mv(src,des)


# 重命名文件或目录
# src = r'D:\Temp\AA\A.jpg'
# des = r'D:\Temp\AA\B.jpg'
# ci.rename(src,des)

# src = r'D:\Temp\AA'
# des = r'D:\Temp\BB'
# ci.rename(src,des)


# # 文件添加前缀
# src = r'D:\Temp\BB\B.jpg'
# prefix = 'img_'
# ci.addPrefix(src,prefix)  # r'D:\Temp\BB\img_B.jpg'

# # 文件目录添加前缀
# src = r'D:\Temp\BB'
# prefix = 'dir_'
# ci.addPrefix(src,prefix) # r'D:\Temp\dir_BB'


# # 文件添加尾缀
# src =r'D:\Temp\dir_BB\img_B.jpg'
# suffix = '_001'
# ci.addSuffix(src,suffix) #D:\Temp\dir_BB\img_B_001.jpg

# # 文件目录添加尾缀
# src = r'D:\Temp\dir_BB'
# suffix = '_v001'
# ci.addSuffix(src,suffix)  # r'D:\Temp\dir_BB_v001'



# # 文件打包
#
# src = r'D:\Temp\dir_BB\img_B.jpg'
# des = r'D:\Temp\dir_BB\B.zip'
# ci.pack(src,des)


# # 文件夹打包
# src = r'D:\Temp\dir_BB'
# des = r'D:\Temp\BB.zip'
# ci.pack(src,des)



# # 解压文件或目录
# src_zip = r'D:\Temp\A\BB.zip'
# des_dir = r'D:\Temp\A\C'
# ci.unpack(src_zip,des_dir)