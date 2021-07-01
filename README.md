# cgai-io

#### 介绍
一个简单轻量又快速的数据流操作python库

支持跨平台，支持window文件以及目录的快速复制
支持文件及文件目录删除，支持目录删除保留原目录结构


#### 安装教程

```cmd
pip install cgai-io
```

#### 快速上手

###### 1.复制文件  
```python
from cgai_io.Copy import copyfile

src1 = r'D:\MZ\bg.jpg'
des1 = r'D:\Temp\Test\bg.jpg'

copyfile(src1,des1)
```
###### 2.复制文件目录
```python
from cgai_io.Copy import copydir

src2 = r'D:\MZ'
des2 = r'D:\Temp\Test\MZ'

copydir(src2,des2)
```

###### 3.删除文件及文件目录
```python
from cgai_io.Delete import delfile,deldir,delall


# #删除文件
# path = r'\\192.168.1.248\3d\temp\a\cmd_mac.py'
# delfile(path)


# #删除文件夹
# path = r'D:\BaiduNetdiskDownload\AA'
# deldir(path,keep_dir=True)  #保留空目录结构


#无论文件或文件夹都直接删除
# path = r'D:\BaiduNetdiskDownload\ktk_103024'
# delall(path)
```


#### 交流方式
wx:zxzxde