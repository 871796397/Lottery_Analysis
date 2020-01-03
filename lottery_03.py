#coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import numpy as np

########################清洗及分析数据表#######################
def cleanTbale(data):
    # 清洗数据，留下期号，中奖注数，中奖金额，销售金额，奖池金额  开奖日期
    col = data.columns
    nums = [1, 2, 3, 4, 5, 6, 7, -5, -4, -3, -2, -1]
    x_data = data.drop(col[nums], axis=1)   #删掉号码的列

    colu = x_data.columns
    x_data = x_data[x_data[colu[1]] > 0]   ##清除一等奖注数为0 的所有行

    ##将一等奖奖金_元 / 一等奖注数 得到结果新建一列(一等奖单注奖金 )添加到末尾列
    x_data = x_data.eval('一等奖单注奖金 = 一等奖奖金_元 // 一等奖注数')  ##列名称不能有括号，否则报错
    x_data = x_data.eval('二等奖单注奖金 = 二等奖奖金_元 // 二等奖注数')
    #print(x_data)
    # 计算单注奖金 = 奖金/中奖注数
    return x_data

########################一等奖中奖注数和单注奖金(百万元)的散点图#######################
def numberEntries_bonus_f(data):
    col = data.columns   #原数组的列名称

    ###处理数据###
    first_col =pd.value_counts(data[col[1]])     # 统计一等奖注数，按注数的数量的降序排列
    mean_Entrie = []         # 存放 相同注数的均值 的列表

    for f in first_col.index:                    # 遍历一等奖注数
        choice_f = data[data[col[1]]==f]
        mean_Entrie.append(int(choice_f[choice_f.columns[-2]].mean()))   #将相同一等奖中奖数的单注奖金列取均值，并添加到列表中
    xy_nums = pd.DataFrame(data=[first_col.index,mean_Entrie],index=['x_num','y_num']).T  #创建数组，并行列转置
    xy_nums = xy_nums.sort_values(by='x_num')  #将 以x_num为升序 将数组重新排列

    x_num = xy_nums['x_num']
    y_num = xy_nums['y_num'] // 10000
    print(y_num)
    d = max(x_num)//len(x_num)+3

    ###创建图表###
    matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用微软雅黑显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    fig, ax = plt.subplots(figsize=(16, 8), dpi=80)
    ax.scatter(x_num,y_num,label="一等奖注数和单注奖金")
    ax.grid(linestyle='-.', alpha=0.3)
    ax.legend(loc="best")

    plt.xticks(range((max(x_num)-min(x_num))+d)[::d])
    plt.yticks(range((max(y_num)-min(y_num))+d*8)[::d*8])
    ax.set_title("一等奖中奖注数和单注奖金关系")  # 设置大标题
    ax.set_xlabel("一等奖中奖注数")  # 设置横坐标标签
    ax.set_ylabel("一等奖等奖单注奖金(万元)")

    ax.set_xlim([0,max(x_num)+d])
    ax.set_ylim([0,max(y_num)+d])
    plt.show()
########################二等奖中奖注数和单注奖金(百万元)的散点图#######################
def numberEntries_bonus_s(data):
    col = data.columns   #原数组的列名称

    ###处理数据###
    second_col = pd.value_counts(data[col[3]])   # 统计二等奖注数，按注数的数量的降序排列
    mean_Entrie = []         # 存放 相同注数的均值 的列表
    for s in second_col.index:                  # 遍历二等奖注数
        choice = data[data[col[3]] == s]
        mean_Entrie.append(int(choice[choice.columns[-1]].mean()))  #将相同二等奖中奖数的单注奖金列取均值，并添加到列表中
    xy_nums = pd.DataFrame(data=[second_col.index,mean_Entrie],index=['x_num','y_num']).T  #创建数组，并进行行列转置
    xy_nums = xy_nums.sort_values(by='x_num')  # 将 以x_num为升序 将数组重新排列

    x_num = xy_nums['x_num']
    y_num = xy_nums['y_num'] // 100
    d = max(x_num)//len(x_num)+36
    for i in y_num:
        print(i)
    ###创建图表###
    matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用微软雅黑显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    fig, ax = plt.subplots(figsize=(16, 8), dpi=80)
    ax.scatter(x_num,y_num,label="单注奖金1万以下，中奖注数400注以下 的分布")

    ax.grid(linestyle='-.', alpha=0.3)
    ax.legend(loc="best")

    plt.xticks(range((max(x_num)-min(x_num)))[::10])
    plt.yticks(range((max(y_num)-min(y_num)))[::5])
    ax.set_title("二等奖中奖注数和单注奖金关系")  # 设置大标题
    ax.set_xlabel("二等奖中奖注数")  # 设置横坐标标签
    ax.set_ylabel("二等奖单注奖金(百元)")
    ax.set_xlim([0,400])
    ax.set_ylim([0,100])
    plt.show()
#########################奖池金额与销售金额的走势图 （百万元）############################
def jackpot_salesVolume1(data):
    ##处理数据##
    data = data.sort_values(by="期号")      # 将 以期号为升序 将数组重新排列
    data = data[data["奖池奖金_元"] > 0]    #将奖池奖金为0的行删除

    x_label = data["期号"]
    jackpots = data["奖池奖金_元"]//1000000  #设置成百万元
    next_sales = data["销售额_元"]//1000000   #设置成百万元
    x = range(len(x_label))    #获取x坐标值

    ###创建图表###
    matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用微软雅黑显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    fig, ax = plt.subplots(figsize=(24, 8), dpi=80)   #创建画布及创建第一张空白图表
    ax1 = ax.twinx()  # 新建第二张空白图表
    plt.grid(alpha=0.3)             #创建网格
    plt.xticks(x[::10], x_label[::10], rotation=60)    #设置X轴的坐标数字
    plt.xlim([800,len(x_label)])                        #设置X轴坐标值范围

    ax.set_yticks(range(int(max(jackpots)))[::250])   #设置第一张图表的Y轴坐标值
    ax.set_ylim([0, int(max(jackpots))])               #设置第一张图表的Y轴坐标值范围
    ax.set_title("奖池金额与销售金额的关系")   #设置图表标题
    ax.set_xlabel("彩票期数")           #设置X轴标签
    ax.set_ylabel("奖池金额(百万元)")   #设置第一张图表Y轴标签

    ax1.set_yticks(range(int(max(next_sales)))[::10])  #设置第二张图表的Y轴坐标值
    ax1.set_ylim([0, int(max(next_sales))])      #设置第二张图表的Y轴坐标值范围
    ax1.set_ylabel("销售金额(百万元)")   #设置第二张图表Y轴标签
    a, = ax.plot(x, jackpots, color="r", linestyle="--", linewidth="1")  #给第一张图表上折线图
    b, = ax1.plot(x, next_sales, color="g", linestyle="-", linewidth="1")#给第二张图表上折线图
    plt.legend([a, b], ["奖池金额","销售金额"], loc=2)   # 两个折线的图例合并放一起
    plt.show()
#########################奖池大小与下期销售额的散点图 （百万元）############################
def jackpot_salesVolume2(data):
    ##处理数据##
    data = data[data["奖池奖金_元"] > 0]    #将奖池奖金为0的行删除
    data = data.sort_values(by="销售额_元")  # 将 以期号为升序 将数组重新排列
    jackpots = data["奖池奖金_元"]//1000000  #设置成百万元
    sales = data["销售额_元"]//1000000   #设置成百万元
    x = range(max(sales))

    ###创建图表###
    matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 用微软雅黑显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    fig, ax = plt.subplots(figsize=(24, 8), dpi=80)   #创建画布及创建第一张空白图表
    plt.grid(alpha=0.3)             #创建网格

    plt.xticks(x[::5],rotation=60)    #设置X轴的坐标数字
    ax.set_xlim([150,max(sales)+5])                        #设置X轴坐标值范围
    ax.set_yticks(range(int(max(jackpots)))[::250])   #设置第一张图表的Y轴坐标值
    ax.set_ylim([0, int(max(jackpots))+100])               #设置第一张图表的Y轴坐标值范围
    ax.set_title("奖池金额与销售金额的关系")   #设置图表标题
    ax.set_xlabel("销售金额(百万元)")           #设置X轴标签
    ax.set_ylabel("奖池金额(百万元)")   #设置第一张图表Y轴标签
    ax.scatter(sales, jackpots, color="g")  # 给第一张图表上折线图
    plt.show()

if __name__ == '__main__':
        # data = pd.read_csv("lottery1.csv")               #从csv中读取数据
        data = pd.read_excel("lottery.xlsx")  # 从excel中读取数据
        x_data = cleanTbale(data)
        #numberEntries_bonus_f(x_data)
        numberEntries_bonus_s(x_data)
        #jackpot_salesVolume1(data)
        #jackpot_salesVolume2(data)