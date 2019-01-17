# -*- coding: utf-8 -*-

import os

def findfile(key, inputdir='.'):
    found_list = []
    for path, dirnames, filenames in os.walk(inputdir):
        for name in filenames:
            full_name = path + '/' + name
            if key in name:
                found_list.append(full_name)
            with open(full_name, encoding='utf-8') as f:
                for l in f.readlines():
                    if key in l:
                        found_list.append(full_name + ':' + l)
    return found_list

keyword = input('请输入关键字：\n')
path = input('in:')
if not path.strip():
    path = '.'

result = findfile(keyword, path)

for r in result:
    print (r)
