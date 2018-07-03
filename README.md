# Scores_Forecast
    专业实习之学生成绩预测

## 文件说明
    Python文件：
        成绩矩阵生成：Array_of_Matrix.py
        数据集生成：DataSet_Generation.py
        成绩预测：Predict.py
    
    数据集文件：
        原始数据集：exam.csv
        选出100个人的成绩：2.csv
        从100个人的成绩中选出100个单科成绩作为单元测试：Unit_Test.csv
        100个人的剩余成绩：Test_Group.csv
    
## 文件功能及函数简介
    Array_of_Matrix.py：
        (该文件为库文件，供Predict.py文件调用)
        包含两个可调用函数：
            1.矩阵生成函数：Matrix_Generation_function
                (供Create_Generation函数调用)
                接收2个参数：
                    (1)经过二次处理的单条成绩信息列表
                        即将单条成绩信息通过逗号分隔而成的列表
                    (2)单行30列的numpy 0矩阵
                返回1个参数：
                    (1)经过处理的单行30列numpy 0矩阵
                        即将目标人物所有成绩分类求和写入矩阵对应处，整数部分的数值为成绩总和，小数位的数值为成绩数量的记录
            2.创建生成函数：Create_Generation
                (调用Matrix_Generation_function函数，自身被文件Predict.py调用)
                接收1个参数：
                    (1)原始字符串
                        即从csv文件中直接读取的原始字符串
                返回1个参数：
                    (1)参照列表：
                        将所有处理好的平均成绩矩阵组成的列表
    
    DataSet_Generation.py：
        (数据集生成文件，可执行)
        主要作用为：将已经过清洗的数据集文件分成控制组、测试组及单元测试组。
        (控制组用于作为knn的比对数据集，测试组所得结果与单元测试组比对得出正确率。)

    Predict.py:
        (预测文件，可执行)
        向量knn法，手动pca，求取最小夹角匹配项，对预测极值进行回归。