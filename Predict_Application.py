#!/usr/bin/env python3
# 网页应用程序版

from Array_of_Matrix import *
import numpy as np
from random import *
import sys

np.seterr(all = 'raise')

# 读取待预测者及待预测科目信息
UUID = '419c6fac-21aa-11e8-8234-9061ae17b27c'
Subject_type = 1
Test_Type = 1
crs = 1

# 读取对照组
with open('exam.csv', 'r') as Original_File:
	Original_String = Original_File.read()

# 第一次处理
First_Processing = Original_String.split('\n')

# 删除待预测者的所有成绩,并将处理后的成绩存入新列表,被预测者的成绩信息存入另一新列表
Be_processed_without_UUID = []
Be_processed_only_UUID = []
for ele in First_Processing:
    # 对每行内容(UUID,课程号,课程名,成绩,学科类型,考试类型,学分)进行分片处理
    Second_Processing = ele.split(',')
    if Second_Processing[0] != UUID:
        Be_processed_without_UUID.append(ele)
    if Second_Processing[0] == UUID:
        Be_processed_only_UUID.append(ele)

# print(Be_processed_only_UUID)