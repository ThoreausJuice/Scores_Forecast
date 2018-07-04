#!/usr/bin/env python3
# 网页应用程序版

from Array_of_Matrix import *
import numpy as np
from random import *
import sys

np.seterr(all = 'raise')

# 读取待预测者及待预测科目信息
Student_id = '5120150697'
with open('studentid.csv', 'r') as Original_File:
	Original_String = Original_File.read().split('\n')
	for ele in Original_String:
		Second_Processing = ele.split(',')
		if Second_Processing[0] == Student_id:
			UUID = Second_Processing[1]
# UUID = '419c6fac-21aa-11e8-8234-9061ae17b27c'
Subject_type = '必修'
Test_Type = '正常考试'
crs = '2'

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
# 将处理后的列表变回字符串
Symbol = '\n'
Be_processed_without_UUID = Symbol.join(Be_processed_without_UUID)
Be_processed_only_UUID = Symbol.join(Be_processed_only_UUID)

# print(Be_processed_without_UUID)
Control_Group = Create_Generation(Be_processed_without_UUID)

# 构建待预测者成绩组，即测试组
Test_Group = Create_Generation(Be_processed_only_UUID)

# 构建待预测者待预测的成绩信息列表，即单元测试
First_Processing = UUID + ',管他什么课号,无所谓什么学科名,0,' + Subject_type + ',' + Test_Type + ',' + crs

# Min角度标识
Min_Angle = 1000
# 最小距离矩阵标识
Min_Matrix = []
# 待预测坐标
z = None
# 待预测成绩
Forecast_value = None
# 预测区间
Interval = 10

for x in Test_Group:
	# 对单元测试进行分片处理
	Second_Processing = First_Processing.split(',')
	# 求取待预测坐标
	if Second_Processing[5] == '正常考试':
		if Second_Processing[4] == '必修':
			if round(float(Second_Processing[6])) > 6:
				Second_Processing[6] = 6
			z = round(float(Second_Processing[6]))
		if Second_Processing[4] == '限选':
			z = round(float(Second_Processing[6])) + 5
		if Second_Processing[4] == '任选':
			z = round(float(Second_Processing[6])) + 11
	if Second_Processing[5] == '补考' or Second_Processing[5] == '重考':
		if round(float(Second_Processing[6])) > 6:
			Second_Processing[6] = 6
		z = round(float(Second_Processing[6])) + 17
	if Second_Processing[5] == '重修':
		if round(float(Second_Processing[6])) > 6:
			Second_Processing[6] = 6
		z = round(float(Second_Processing[6])) + 23
	# 矩阵匹配运算
	Lx = np.sqrt(x.dot(x))
	for y in Control_Group:
		Ly = np.sqrt(y.dot(y))
		if Lx * Ly == 0:
			continue
		else:
			cos_angle = x.dot(y) / (Lx * Ly)
		# break
		# print(cos_angle)
		Radian = np.arccos(cos_angle)
		Angle = Radian * 180 / np.pi
		if Min_Angle > Angle:
			Min_Angle = Angle
			Min_Matrix = y
	# 求取预测值
	M_Number = round((Min_Matrix[z] - round(Min_Matrix[z])) * 10000) / 100
	X_Number = round((x[z] - round(x[z])) * 10000) / 100

	if Min_Matrix[z] * x[z] != 0:
		Forecast_value = round((Min_Matrix[z] * M_Number + x[z] * X_Number) / (M_Number + X_Number) + 0.5) #+ randrange(-1, 1)
	# 当预测值为nan时,取所有成绩有效均值
	else:
		Forecast_value = 0
		for ele in x:
			Forecast_value += round(ele ** 2 / 100) + ele / 10000
		Forecast_value = round(round(Forecast_value) / (Forecast_value - round(Forecast_value)) / 100 + 0.5)

	# 非正常考试值
	Abnormal = 0
	for ele in x[18:]:
		if int(ele) == 0:
			Abnormal += 1
	if Abnormal == 12:
		Forecast_value += 5
	if Abnormal <= 6:
		Forecast_value -= 5
	
	# 对优秀值进行回归
	if Forecast_value >= 95:
		Forecast_value = 100 - Interval
	if Forecast_value <= 5:
		Forecast_value = Interval

print(Forecast_value)