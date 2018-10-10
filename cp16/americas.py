#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     americas
   Description :
   Author :       william
   date：          2018/10/10
-------------------------------------------------
   Change Activity:
                   2018/10/10:
-------------------------------------------------
"""
__author__ = 'william'

import pygal

wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

# wm.add('North America', ['ca', 'mx', 'us'])
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.add('North America', {'ca': 100, 'mx': 200, 'us': 300})
wm.render_to_file('americas.svg')

