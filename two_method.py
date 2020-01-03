#coding=utf-8
import requests
import time
import pandas as pd
import numpy as np

url = f"http://www.lottery.gov.cn/historykj/history_1.jspx?_ltype=dlt"
header={"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
new_title = ['期号','first1','first2','first3','first4','first5','last1','last2','一等奖注数', '一等奖奖金(元)',\
             '二等奖注数','二等奖奖金(元)','销售额(元)','奖池奖金（元）','开奖日期','1~2','2~3','3~4','4~5','last1~last2']

res = requests.get(url, headers=header).text  # 获取网页内容
df = pd.read_html(res)[0].values  # 获取表格数据

#处理数据
def get_data(list):
    # 将8到15之间的数据两两相加，再插入数组中
    list = np.insert(list, 8, [list[8] + list[10], list[9] + list[11], list[12] + list[14], list[13] + list[15]])
    list = np.delete(list, -4)  # 删除“nan“
    list = np.delete(list, np.s_[12:20])  # 删除“8到15之间的数据“
    # 将1到7之间的数据两两相减，再添加到数组末尾
    list = np.append(list, [list[2] - list[1], list[3] - list[2], list[4] - list[3], list[5] - list[4],
                            list[7] - list[6]])
    return list

###method-1：以行数据处理，并以行的子列表元素存列表中
data_list = []
for list in df:
    list =get_data(list)
    data_list.append(list)  #将处理好的数据装入空列表data_list中
dataframe = pd.DataFrame(data_list,columns=new_title)
#dataframe.to_excel("lottery01.xls")
#print(dataframe)

###method-2：以行数据处理，并以列的子列表元素存列表中
data_list1 = []
for i in range(20):
    data_1 = []
    for list in df:
        list =get_data(list)
        data_1.append(list[i])   #将处理好的数据装入空列表data_list中
    data_list.append(data_1)

dataframe1 = pd.DataFrame(data_list,columns=new_title)
#dataframe1.to_excel("lottery02.xls")
#print(dataframe)