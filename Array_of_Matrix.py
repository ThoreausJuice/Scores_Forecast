#!/usr/bin/env python3

import numpy as np

# 有效成绩矩阵生成函数
def Matrix_Generation_function(Second_Processing, Grades_Matrix):
	if Second_Processing[5] == '正常考试':
		if Second_Processing[4] == '必修':
			if round(float(Second_Processing[3])) != 0:
				if round(float(Second_Processing[6])) > 6:
					Second_Processing[6] = 6
				Grades_Matrix[round(float(Second_Processing[6])) -1] += round(float(Second_Processing[3]) ** 2 * 0.01 + 0.5) + 0.0001 * float(Second_Processing[3])
		if Second_Processing[4] == '限选':
			if round(float(Second_Processing[3])) != 0:
				Grades_Matrix[5 + round(float(Second_Processing[6]))] += round(float(Second_Processing[3]) ** 2 * 0.01 + 0.5) + 0.0001 * float(Second_Processing[3])
		if Second_Processing[4] == '任选':
			if round(float(Second_Processing[3])) != 0:
				Grades_Matrix[11 + round(float(Second_Processing[6]))] += round(float(Second_Processing[3]) ** 2 * 0.01 + 0.5) + 0.0001 * float(Second_Processing[3])
	if Second_Processing[5] == '补考' or Second_Processing[5] == '重考':
		if round(float(Second_Processing[3])) != 0:
			if round(float(Second_Processing[6])) > 6:
				Second_Processing[6] = 6
			Grades_Matrix[17 + round(float(Second_Processing[6]))] += round(float(Second_Processing[3]) ** 2 * 0.01 + 0.5) + 0.0001 * float(Second_Processing[3])
	if Second_Processing[5] == '重修':
		if round(float(Second_Processing[3])) != 0:
			if round(float(Second_Processing[6])) > 6:
				Second_Processing[6] = 6
			Grades_Matrix[23 + round(float(Second_Processing[6]))] += round(float(Second_Processing[3]) ** 2 * 0.01 + 0.5) + 0.0001 * float(Second_Processing[3])
	return(Grades_Matrix)

def Create_Generation(Original_String):
	# 构造参照UUID
	Reference_UUID = None
	# 构造5行6列的0成绩矩阵
	Grades_Matrix = np.zeros(30, float)
	# 构造参照数组
	Reference_Match = []
	# 初次处理标识
	Flag = 1
	# 第一次处理
	First_Processing = Original_String.split('\n')
	# 将 "成绩和"矩阵 追加至数组末端
	for line in First_Processing:
		# 对每行进行第二次处理
		Second_Processing = line.split(',')
		# 当UUID遇上一次存储不同时，更新参照UUID，参照数组追加成绩矩阵，清零成绩矩阵
		if Second_Processing[0] != Reference_UUID:
			Reference_UUID = Second_Processing[0]
			if Flag != 1:
				Reference_Match.append(Grades_Matrix)
				Grades_Matrix = np.zeros(30, float)
			Flag = 0
			Grades_Matrix = Matrix_Generation_function(Second_Processing, Grades_Matrix)
		# 否则，建立有效成绩矩阵
		else:
			Grades_Matrix = Matrix_Generation_function(Second_Processing, Grades_Matrix)
	Reference_Match.append(Grades_Matrix)

	# 将 "成绩和"矩阵 处理为平均成绩矩阵
	for ele in Reference_Match:
		for i in range(0, 30):
			if ele[i] != 0:
				Number_of_Grades = ele[i] - round(ele[i])
				ele[i] = round(ele[i] / (Number_of_Grades * 100) + 0.5) + Number_of_Grades
				
	return(Reference_Match)