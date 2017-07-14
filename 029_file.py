#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开一个文件
fo = open("CUITstudentNumber.txt", "wb")
for i in range(2014110000,2014130000):
    x=str(i)
    fo.write(x);
    fo.write('\n')

# 关闭打开的文件
fo.close()