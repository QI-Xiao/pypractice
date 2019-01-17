# -*- coding:utf-8 -*-
import re

with open('from.txt', encoding='utf-8') as f:
    content = f.read()

text = re.findall(r'[A-z]+', content)
text.sort()
print(text)
textto = '\n'.join(text)
print(textto)
with open('to.txt', 'w', encoding='utf-8') as g:
    g.write(textto)


