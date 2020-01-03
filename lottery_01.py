#coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import numpy as np

#######################中奖号码数字的数量和出现的频数#####################
def number_find(data):
    plt.figure(figsize=(16, 10), dpi=80)                             # 设置图表的尺寸大小
    matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']     # 用微软雅黑显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False                # 正常显示负号

    for i in range(1,8):
        # col = data.columns[i]  # 定位列元素
        # counts = pd.value_counts(data[col])  # 获取列元素中数字的统计结果，从大到小排列
        x_data = data[data.columns[i]].to_list()      # 将目标列数据转换成列表
        x_list = range(min(x_data), max(x_data) + 1)  # 设置X轴坐标值区间

        x_box = []    # 将相同数字的统计出来放入新的列表中
        for list in x_list:
            num = x_data.count(list)
            x_box.append(num)

        number =[]   # 获取数量最多和第二多的数字
        x_box_ = x_box.copy()
        x_box_.remove(max(x_box_))
        for xl in x_list:
            if x_data.count(xl)==max(x_box):
                number.append(xl)
            if x_data.count(xl) == max(x_box_):
                number.append(xl)

        for x,y in zip(x_list,x_box):                 #在柱子上标数字
            plt.text(x, y + 0.01, "%.2f%%" %(y/sum(x_box)*100),
              ha="center", va="bottom", fontsize=8,rotation=30)

        plt.grid(alpha=0.2)                                  # 设置网格
        plt.xticks(x_list)                                   # 设置坐标轴参数
        plt.bar(x_list,x_box,width=0.8,color='b',            # 创建图像
                label=f'''蓝柱长度表示数字的数量
第{i}个号码中：数字{number[0]}的占比最多，
数字{number[1]}占比次之''')
        plt.title(f"第{i}个号码的数字分布")                  # 设置大标题
        plt.xlabel("选号码的数字")                           # 设置横坐标标签
        plt.ylabel("数字的数量")                             # 设置纵坐标标签
        plt.legend(loc='best')                               # 显示(label = '直方图')图例
        plt.show()                                           #呈现图表
        #plt.savefig("./mat_条形图.png")                     #保存图表

#######################中奖号码加总值的频数，使用折线图#####################
def number_sum(data):
    plt.figure(figsize=(16, 10), dpi=80)  # 设置图表的尺寸大小
    matplotlib.rcParams['font.sans-serif'] = ['STXihei']  # 用黑体显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号

    col = data.columns
    x_data7 = data[col[1:8]]        #筛选出1-7号码的数据
    x_data5 = data[col[1:6]]        #筛选出1-5号码的数据
    x_data2 = data[col[6:8]]        #筛选出6-7号码的数据
    x_data7_sum = x_data7.sum(axis=1)   #将每期1-7个中奖号码加总
    x_data5_sum = x_data5.sum(axis=1)   #将每期1-5个中奖号码加总
    x_data2_sum = x_data2.sum(axis=1)   #将每期6-7个中奖号码加总
    #x_data7_count = pd.value_counts(x_data7_sum)
    d = 5
    bins7 = max(x_data7_sum)-min(x_data7_sum)+1
    bins5 = max(x_data5_sum)-min(x_data5_sum)+1
    bins2 = max(x_data2_sum) - min(x_data2_sum) + 1

    plt.grid(linestyle='-.', alpha=0.3)                              # 设置网格
    # plt.hist(x_data7_sum, bins7, label="1-7号码和")                # 创建直方图
    # plt.xticks(range(min(x_data7_sum), max(x_data7_sum) + d, d))   # 设置X轴坐标
    #plt.hist(x_data5_sum, bins5, color="g",label="1-5号码和")  # 创建直方图
    #plt.xticks(range(min(x_data5_sum), max(x_data5_sum) + d, d))
    plt.hist(x_data2_sum, bins2, color="r",label="6-7号码和")  # 创建直方图
    plt.xticks(range(min(x_data2_sum), max(x_data2_sum) + 1, 1))
    # plt.plot(x_data7_sum.index, x_data7_sum, label="1-7号", color="r", linestyle="--", linewidth="1")
    # plt.plot(x_data5_sum.index, x_data5_sum, label="1-5号", color="g", linestyle="-.", linewidth="1")
    # plt.plot(x_data2_sum.index, x_data2_sum, label="6-7号", color="b", linestyle="-", linewidth="1")
    plt.title("每期号码和的数量分布")                   # 设置大标题
    plt.xlabel("号码和数字大小")                        # 设置横坐标标签
    plt.ylabel("号码和数字的数量")                      # 设置纵坐标标签
    plt.legend(loc='best')                              # 设置图例标签
    plt.show()                                          #呈现图表
    #plt.savefig("./mat_条形图.png")    #保存图表

#######################中奖号码数字最多的，出现最多的其他数字#####################
def number_most(data):
    plt.figure(figsize=(16, 10), dpi=80)  # 设置图表的尺寸大小
    matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用微软雅黑显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号

    for i in range(1, 8):
        col1 = data.columns[i]                      #定位列元素
        counts1 = pd.value_counts(data[col1])       #获取列元素中数字的统计结果，从大到小排列
        most_number = counts1.index[0]              #获取数量最多的数字
        x_data = data[data[col1] == most_number]    #留下数量最多的数字的所有行

        x_labels,second_numbers = [],[] #在最多数字的筛选下，将其他列数字最多的存进列表
        for xi in range(1,8):
            if xi == i:
                continue
            col2 = x_data.columns[xi]                       # 定位筛选后的列元素
            counts2 = pd.value_counts(x_data[col2])         # 获取列元素中数字的统计结果，从大到小排列
            x_labels.append(f'{xi}号({counts2.index[0]})')  # 存X轴值标签
            second_numbers.append(counts2.values[0])        # 存数字最多的数量

        for x, y in zip(range(len(x_labels)), second_numbers):             # 在柱子上标数字
            plt.text(x, y + 0.01, f'{y}',ha="center", va="bottom", fontsize=15)
        plt.xticks(range(len(x_labels)),x_labels,fontsize=15)        # 设置坐标轴参数
        plt.bar(range(len(x_labels)), second_numbers, width=0.6)     # 创建图像
        plt.title(f'第{i}个号码的最多数字{most_number}的情况下,其他号码中占比最多的数字',fontsize=20,)  # 设置大标题
        plt.xlabel("选号码的数字",fontsize=15)  # 设置横坐标标签
        plt.ylabel("数字的数量",fontsize=15)  # 设置纵坐标标签
        plt.show()  # 呈现图表

#######################临近号码差值的分布#####################
def number_near(data):
    plt.figure(figsize=(12, 8), dpi=80)  # 设置图表的尺寸大小
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号

    col = data.columns
    x_data = data[col[-5:]]  # 筛选出倒数5列数据

    for i in range(5):
        col_counts = x_data[x_data.columns[i]].value_counts()
        x_box = col_counts.values
        bins = col_counts.index

        for x, y in zip(bins, x_box):             # 在柱子上标数字
            plt.text(x, y + 0.01, f'{y}',ha="center", va="bottom", fontsize=12)
        plt.grid(linestyle='-.', alpha=0.3)                  # 设置网格
        plt.xticks(bins)                                   # 设置坐标轴参数
        plt.bar(bins,x_box,width=0.8)                       # 创建条形图

        plt.title(f"{x_data.columns[i]}号码数字差值的数量分布")                   # 设置大标题
        plt.xlabel(f"号码差值数字{x_data.columns[i]}")                          # 设置横坐标标签
        plt.ylabel("差值的频数")                            # 设置纵坐标标签
        plt.show()                                          #呈现图表
        #plt.savefig("./mat_条形图.png")    #保存图表

if __name__ == '__main__':
    data = pd.read_csv("lottery1.csv")               #从csv中读取数据
    #data = pd.read_excel("lottery.xlsx")            #从excel中读取数据
    #number_find(data)    # 输出直方分析图
    #number_most(data)    #输出筛选后的分析图
    #number_sum(data)    #输出折线分析图
    #number_near(data)   #输出分析图
