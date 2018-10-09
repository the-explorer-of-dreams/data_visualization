#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     highs_lows
   Description :
   Author :       william
   date：          2018/10/9
-------------------------------------------------
   Change Activity:
                   2018/10/9:
-------------------------------------------------
"""
__author__ = 'william'

import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename='death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing date")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print(highs)
    #根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', linewidth=1, alpha=0.5)
    plt.plot(dates, lows, c='blue', linewidth=1, alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


    # 设置图形的格式
    plt.title("Daily high and low temperature, 2014")
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()