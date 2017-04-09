#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'Dowfree'

import os


# 查找当前目录下含有所有包含关键字的文件
def find_file(path, key, extension):
    if extension == 'open':
        return [os.path.join(path, x) for x in os.listdir(path) if key in x and os.path.isfile(os.path.join(path, x))]
    elif extension == 'close':
        return [os.path.join(path, x) for x in os.listdir(path) if key in x.split('.')[0]
                and os.path.isfile(os.path.join(path, x))]
    else:
        raise ValueError('extension has only two choices: open and close')


# 获得当前目录的所有子目录
def find_dir(path):
    return [os.path.join(path, x) for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]


# 遍历所有子目录文件
def list_file(path, key, extension='open', all_file=[]):
    all_file += find_file(path, key, extension)
    for x in find_dir(path):
        list_file(x, key, extension, all_file)
    return all_file


# 用户的调用函数
def show_file(path, key, extension='open'):
    return list_file(path, key, extension, all_file=[])

print(list_file(r'C:\Users\free\Desktop\application', 'k'))
