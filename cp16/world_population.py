#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     world_population
   Description :
   Author :       william
   date：          2018/10/10
-------------------------------------------------
   Change Activity:
                   2018/10/10:
-------------------------------------------------
"""
__author__ = 'william'

import json
from country_codes import get_country_code
import pygal
from pygal.style import RotateStyle, LightColorizedStyle

# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

gb_populations = {}
gb_pops_1, gb_pops_2, gb_pops_3 = {}, {}, {}
for pop_dict in pop_data:
    if pop_dict['Year'] == 2016:
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        # print(country_name + ":" + str(population))
        country_code = get_country_code(country_name)

        if country_code:
            gb_populations[country_code] = population

for code, pop in gb_populations.items():
    if pop < 10000000:
        gb_pops_1[code] = pop
    elif pop < 100000000:
        gb_pops_2[code] = pop
    else:
        gb_pops_3[code] = pop

print(len(gb_pops_1), len(gb_pops_2), len(gb_pops_3))
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'world population, 2016'

wm.add('0-1bn', gb_pops_1)
wm.add('1-10bn', gb_pops_2)
wm.add('>10bn', gb_pops_3)

wm.render_to_file('gb_populations.svg')