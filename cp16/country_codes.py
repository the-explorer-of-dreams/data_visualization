#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     country_codes
   Description :
   Author :       william
   date：          2018/10/10
-------------------------------------------------
   Change Activity:
                   2018/10/10:
-------------------------------------------------
"""
__author__ = 'william'

from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """根据国家名字返回国家的两位编码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    return None


if __name__ == '__main__':
    print(get_country_code('Guam'))