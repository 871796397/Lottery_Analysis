#coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import numpy as np

#######################七个号码的选数字时间走势图#####################
def trend_of_numbers(data):
    ###处理数据####
    col = data.columns
    x_labels = data[col[0]]
    x_num = range(len(x_labels))
    y_1,y_2,y_3,y_4 = data[col[1]],data[col[2]],data[col[3]],data[col[4]]
    y_5,y_6,y_7  = data[col[5]],data[col[6]],data[col[7]]

    ####制作图表####
    matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用微软雅黑显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    fig, ax = plt.subplots(figsize=(50,10), dpi=100)  # 创建画布及创建第一张空白图表
    plt.grid(alpha=0.3)  # 创建网格
    # ax1,ax2,ax3,ax4 = ax.twinx(),ax.twinx(),ax.twinx(),ax.twinx()
    # ax5,ax6,ax7 = ax.twinx(),ax.twinx(),ax.twinx()

    plt.xticks(x_num[::20],x_labels[::20],rotation=60)
    plt.xlim([0,len(x_num)])
    plt.yticks(range(max(y_5))[::2])# 设置坐标轴参数
    plt.ylim([0,max(y_5)+1])
    plt.plot(x_num, y_1, label="1号号码", linewidth="0.5")
    # plt.plot(x_num, y_2, label="2号号码", linewidth="0.5")
    # plt.plot(x_num, y_3, label="3号号码", linewidth="0.5")
    # plt.plot(x_num, y_4, label="4号号码", linewidth="0.5")
    # plt.plot(x_num, y_5, label="5号号码", linewidth="0.5")
    # plt.plot(x_num, y_6, label="6号号码", linewidth="0.5")
    # plt.plot(x_num, y_7, label="7号号码", linewidth="0.5")

    plt.title("七个号码走势图")                  # 设置大标题
    plt.xlabel("开奖期数")                           # 设置横坐标标签
    plt.ylabel("号码数值")                             # 设置纵坐标标签
    plt.legend(loc='upper center')                               # 显示(label = '直方图')图例
    #plt.show()
    plt.savefig("./000.png")#呈现图表

#######################一等奖二等奖中奖注数时间走势图#####################
def trend_of_winning_entries(data):
   ####处理数据###
    x_labels = data["期号"].sort_index(ascending=False)    #将期号列按照升序排列，作为X轴坐标值
    x_num = range(len(x_labels))            #定义x轴坐标值范围
    y_1 = data["一等奖注数"].sort_index(ascending=False)     #将一等奖注数按照升序排列，作为Y轴第一个数据
    y_2 = data["二等奖注数"].sort_index(ascending=False)     #将二等奖注数按照升序排列，作为Y轴第二个数据

    ####制作图表#####
    plt.figure(figsize=(60, 20), dpi=80)  # 设置图表的尺寸大小
    matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用微软雅黑显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号

    plt.grid(alpha=0.2)                                  # 设置网格
    plt.xticks(x_num[::30],x_labels[::30],rotation=60)     #设置图表X轴坐标值，按30间隔显示，将数字亲写60度
    plt.xlim([0, len(x_labels)])   #图表X轴坐标值范围
    plt.yticks(range(500)[::15])   # 设置图表Y坐标轴参数，按照15间隔显示
    plt.ylim([0, 500])    #图表Y轴坐标值范围
    plt.plot(x_num, y_1, label="一等奖中奖注数", color="r", linestyle="--", linewidth="0.5")   #创建一等奖注数折线图
    plt.plot(x_num, y_2, label="二等奖中奖注数", color="g", linestyle="-", linewidth="0.5")    #创建二等奖注数折线图

    plt.title(f"一等奖、二等奖中奖注数走势图")                  # 设置大标题
    plt.xlabel("开奖期数(从启动开始，用序号表示)")              # 设置横坐标标签
    plt.ylabel("中奖注数(超过500注未显示)")                     # 设置纵坐标标签
    plt.legend(loc='best')                                      # 显示图例
    #plt.show()                                                 #呈现图表
    plt.savefig("./00232")                                      #输出并保存图表

#######################中奖号码加总值的时间走势图#####################
def trend_of_number_sum(data):
    ####处理数据####
    col = data.columns
    x_data = data[col[1:8]]        #筛选出1-7号码的数据
    x_data = x_data.sum(axis=1)   #将每期1-7个中奖号码加总
    x_labels = (data["期号"])
    x_num = range(len(x_labels))
    print(x_labels)
    print(x_num)
    #####创建图表####
    matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用微软雅黑显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    fig, ax = plt.subplots(figsize=(20,6), dpi=80)  # 创建画布及创建第一张空白图表
    plt.grid(alpha=0.3)  # 创建网格

    ax.plot(x_num, x_data,linewidth=0.5)  # 创建折线图
    plt.xticks(x_num[::30],x_labels[::30],rotation=60,fontsize=8)
    ax.set_xlim([0,len(x_labels)])
    plt.yticks(range(max(x_data))[::8],fontsize=8)
    ax.set_ylim([40,max(x_data)])
    ax.set_title("每期号码加总的时间走势图")                   # 设置大标题
    ax.set_xlabel("期号")                        # 设置横坐标标签
    ax.set_ylabel("每期号码加总值")                      # 设置纵坐标标签
    plt.show()
    #plt.savefig("./号码和走势图.png")#呈现图表

if __name__ == '__main__':
    data = pd.read_excel("lottery.xlsx")  # 从excel中读取数据
    #trend_of_numbers(data)
    trend_of_winning_entries(data)
    #trend_of_number_sum(data)
