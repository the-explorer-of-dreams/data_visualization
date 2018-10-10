#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     python_repos
   Description :
   Author :       william
   date：          2018/10/10
-------------------------------------------------
   Change Activity:
                   2018/10/10:
-------------------------------------------------
"""
__author__ = 'william'

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)
print("Status code: ", response.status_code)

# 将API响应存储在一个dict中
response_dict = response.json()
print("Total repositories:",response_dict['total_count'])

# 仓库有关的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])
    plot_dict = {}
    if repo_dict['stargazers_count']:
        plot_dict['value'] = repo_dict['stargazers_count']
    if repo_dict['description']:
        plot_dict['label'] = repo_dict['description']
    if repo_dict['html_url']:
        plot_dict['xlink'] = repo_dict['html_url']

    plot_dicts.append(plot_dict)


# 可视化
my_style = LS('#336699', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.label_font_size = 14
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

# 第一个仓库
repo_dict = repo_dicts[0]
print("\nkeys:", len(repo_dict))
print("name: ", repo_dict['name'])
print("html_url: ", repo_dict['html_url'])
print("stargazers_count: ", repo_dict['stargazers_count'])