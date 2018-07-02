#!/usr/bin/env python3

from Array_of_Matrix import *
import numpy as np
from random import *

np.seterr(all='raise')

# 读取对照组
with open('Control_Group.csv', 'r') as Original_File:
	Original_String = Original_File.read()

Control_Group = Create_Generation(Original_String)

# 读取测试组
with open('Test_Group.csv', 'r') as Original_File:
	Original_String = Original_File.read()

Test_Group = Create_Generation(Original_String)

# 读取单元测试
with open('Unit_Test.csv', 'r') as Original_File:
	Original_String = Original_File.read()
# 第一次处理
First_Processing = Original_String.split('\n')

# Min角度标识
Min_Angle = 1000
# 最小距离矩阵标识
Min_Matrix = []
# 待预测坐标
z = None
# 待预测成绩
Forecast_value = None
# 位移变量i
i = 0
# 预测区间
Interval = 6
# 预测错误计数
fail = 0

for x in Test_Group:
	# 对每行单元测试进行分片处理
	Second_Processing = First_Processing[i].split(',')
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

	# 与真实值进行比对
	Min_Value = Forecast_value - Interval
	Max_Value = Forecast_value + Interval
	if Min_Value <= float(Second_Processing[3]) <= Max_Value:
		print('预测正确，当前正确率为：' + str(100 - fail) + ' %')
		print('预测值：' + str(Forecast_value) + ' 真实值：' + Second_Processing[3] + '\n')
	else:
		fail += 1
		print('预测错误，当前正确率为：' + str(100 - fail) + ' %')
		print('预测值：' + str(Forecast_value) + ' 真实值：' + Second_Processing[3] + '\n')
	# 重置Min角度标识
	Min_Angle = 361
	# 位移变量增1
	i += 1
	# 重置待预测坐标
	z = None
	# 重置待预测成绩
	Forecast_value = None

print('\n单元测试结束，最终正确率为：' + str(100 - fail) + ' %\n')