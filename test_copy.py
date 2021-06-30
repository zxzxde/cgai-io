# -*- coding:utf-8 -*-
from cgai_io.Copy import copyfile,copydir


#copy file
src1 = r'D:\MZ\bg.jpg'
des1 = r'D:\Temp\Test\bg.jpg'

# copyfile(src1,des1)

#copy direction

src2 = r'D:\MZ'
des2 = r'D:\Temp\Test\MZ'

copydir(src2,des2)

