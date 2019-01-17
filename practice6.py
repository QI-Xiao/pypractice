# -*- coding:utf-8 -*-
import random
import string

numb = []
for i in range(0, 200):
    l = string.ascii_letters
    l = list(l)
    random.shuffle(l)
    l=''.join(l[:8])
    numb.append(l)
print(numb)

