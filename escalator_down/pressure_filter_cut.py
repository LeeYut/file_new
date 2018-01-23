# -*- coding: utf-8 -*- 
import os
import numpy as np
import pandas as pd


def pressure_difference(folder, file, index):
    df = pd.read_csv(folder + '/' + file)
    #需要修改这里的tag，时间轴
    time = df.time
    #需要修改这里的tag，气压数据
    pressure_values = df.p.values
    pressure_values_filter = []
    for i in range(len(pressure_values)-5):
        pressure_values_filter.append(np.mean(pressure_values[i:i+5]))
    difference_value = [0]
    for i in range(1, len(pressure_values_filter)):
        difference_value.append(pressure_values_filter[i] - pressure_values_filter[i-1])
    new_df = pd.DataFrame({'p':difference_value})
    #输出文件是bb.csv
    new_df.to_csv(os.path.join(folder,"b_diff" + str(index) +".csv"), index = False)	
	
file_list = os.listdir("pressure_filter_cut")
for i in range(len(file_list)):
    #可以在这里修改序数
    pressure_difference("pressure_filter_cut/" , file_list[i], 7+i)
 