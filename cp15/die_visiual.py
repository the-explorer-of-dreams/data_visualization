#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     die_visiual
   Description :
   Author :       william
   date：          2018/10/9
-------------------------------------------------
   Change Activity:
                   2018/10/9:
-------------------------------------------------
"""
__author__ = 'william'

import pygal
from die import Die


# 创建两个D6
die_1 = Die()
die_2 = Die()

# 掷骰子并将结果存储在一个列表中
results = []
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 10000 times."
hist.x_labels = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
