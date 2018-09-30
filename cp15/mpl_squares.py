#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     mpl_squares
   Description :
   Author :       william
   date：          2018/9/30
-------------------------------------------------
   Change Activity:
                   2018/9/30:
-------------------------------------------------
"""
__author__ = 'william'

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot( input_values, squares, linewidth=4)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=10)
plt.show()