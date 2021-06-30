# cgai-io

#### 介绍
一个简单轻量又快速的数据流操作python库

支持跨平台，支持window文件以及目录的快速复制



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

