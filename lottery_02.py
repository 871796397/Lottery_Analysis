#coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import numpy as np

#######################第1、2等奖中奖注数出现的频数#####################
def statistic_of_winning_entries(data):
    plt.figure(figsize=(20,10), dpi=80)                             # 设置图表的尺寸大小
    matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']     # 用微软雅黑显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False                # 正常显示负号

    col_first = data.columns[8]  # 定位列元素
    col_second = data.columns[10]  # 定位列元素

    first_counts = pd.value_counts(data[col_first])  # 获取列元素中数字的统计结果，从大到小排列
    second_counts = pd.value_counts(data[col_second])

    print(second_counts)
    counts = [first_counts,second_counts]
    for i,co in enumerate(counts):
        for x,y in zip(co.index,co.values):                 #在柱子上标数字
            plt.text(x, y + 0.01,"%.2f%%" %(y/sum(co.values)*100),ha="center", va="bottom", fontsize=8,rotation=30)
        plt.grid(alpha=0.2)                                  # 设置网格
        plt.xticks(range(len(co.index))[::1],co.index[::1],fontsize=8,rotation=90)
        plt.bar(range(len(co.index)),co.values,width=0.8,color='b')         # 创建图像
        plt.title(f"{i+1}等奖中奖注数数量图")                  # 设置大标题
        plt.xlabel("中奖的注数)")                           # 设置横坐标标签
        plt.ylabel("中奖注数的数量")                             # 设置纵坐标标签
        plt.show()                                           #呈现图表

#######################高频数的中奖注数与中奖号码的关系#####################
def high_freq_winner(data):
    plt.figure(figsize=(16, 8), dpi=80)  # 设置图表的尺寸大小
    matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用微软雅黑显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号

    col1 = data.columns[8]     # 定位一等奖注数
    col2= data.columns[10]     # 定位二等奖注数
    first_re_data = data[data[col1] > 10]   # 选择一等奖注数大于10注的数据
    second_re_data = data[data[col2] > 100] # 选择二等奖注数大于100注的数据
    for i in range(1,8):
        column = second_re_data.columns[i]
        col_sum = second_re_data[column].value_counts()   #将7个号码的数字进行相同数量统计
        print(col_sum)

        plt.grid(alpha=0.3)
        plt.bar(range(len(col_sum)),col_sum.values,)
        plt.xticks(range(len(col_sum)),col_sum.index)
        plt.title(f"二等奖注数大于100的情况下，第{i}号码数字数量分布图")
        plt.xlabel("号码的数字")
        plt.ylabel("数字的数量")
        plt.show()

#######################高频数的中奖注数后三期中奖号码分布情况#####################
def high_freq_after_three_stage(data):
    plt.figure(figsize=(16, 8), dpi=80)  # 设置图表的尺寸大小
    matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用微软雅黑显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号

    col1 = data.columns[8]     # 定位一等奖注数
    col2= data.columns[10]     # 定位二等奖注数

    afterthree = data.iloc[0:1,:]

    for i,val in enumerate(data[col1]):
        if val > 10:
            #indexs =data[data[col1].isin([val])]
            afterthree=afterthree.append(data.iloc[i+1:i+4])   #获取大于10注的后面三行数据

    for i in range(1,8):
        column = afterthree.columns[i]
        col_sum = afterthree[column].value_counts()   #将7个号码的数字进行相同数量统计
        #print(col_sum)

        plt.grid(alpha=0.3)
        plt.bar(range(len(col_sum)),col_sum.values,)
        plt.xticks(range(len(col_sum)),col_sum.index)
        plt.title(f"一等奖注数大于10的情况下，后3期第{i}号码数字数量分布图")
        plt.xlabel("号码的数字")
        plt.ylabel("数字的数量")
        plt.show()

if __name__ == '__main__':
    #data = pd.read_csv("lottery1.csv")               #从csv中读取数据
    data = pd.read_excel("lottery.xlsx")            #从excel中读取数据
    statistic_of_winning_entries(data)
    #high_freq_winner(data)
    #high_freq_after_three_stage(data)
