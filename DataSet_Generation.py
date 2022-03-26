#!/usr/bin/env python3

# 读取单元测试
with open('2.csv', 'r') as Original_File:
	Original_String = Original_File.read()

# 读取原始对照集
with open('exam.csv', 'r') as Original_File:
	Original_Control_Group = Original_File.read().split('\n')

# 第一次处理
First_Processing = Original_String.split('\n')

# 构造单元测试数组
Unit_Test = []
# 构造测试组
Test_Group = list(First_Processing)
# 构造对照组
Control_Group = list(Original_Control_Group)
# 构造参照UUID
Reference_UUID = None
# 构造截取标识
flag = 0
# 构造删除标识
i = 0

# 筛选分离单元测试组与测试组
for line in First_Processing:
	# 对每行进行分片处理
	Second_Processing = line.split(',')
	if Second_Processing[0] != Reference_UUID:
		Reference_UUID = Second_Processing[0]
		flag = 0
		if round(float(Second_Processing[3])) != 0:
			Unit_Test.append(line)
			Test_Group[i] = 0
			flag = 1
	elif flag == 0:
		if round(float(Second_Processing[3])) != 0:
			Unit_Test.append(line)
			Test_Group[i] = 0
			flag = 1
	i += 1

# 分离对照组
for UT_line in Unit_Test:
	# 对每行进行分片处理
	UT_Second_Processing = UT_line.split(',')
	# 构造删除标识
	j = 0
	for OCG_line in Original_Control_Group:
		# 对每行进行分片处理
		OCG_Second_Processing = OCG_line.split(',')
		if OCG_Second_Processing[0] == UT_Second_Processing[0]:
			Control_Group[j] = 0
		j += 1

with open('Unit_Test.csv', 'w') as New_File:
	# 构造回车标识
	enter = 0
	for ele in Unit_Test:
		if enter == 1:
			New_File.write('\n')
		New_File.write(ele)
		enter = 1

with open('Test_Group.csv', 'w') as New_File:
	# 构造回车标识
	enter = 0
	for ele in Test_Group:
		# print(ele)
		# print(type(ele))
		if ele != 0:
			if enter == 1:
				New_File.write('\n')
			New_File.write(ele)
		enter = 1

with open('Control_Group.csv', 'w') as New_File:
	# 构造回车标识
	enter = 0
	for ele in Control_Group:
		if ele != 0:
			if enter == 1:
				New_File.write('\n')
			New_File.write(ele)
		enter = 1