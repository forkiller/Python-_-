# D:\Users\Administrator\Anaconda3\python.exe
# -*- coding: UTF-8 -*-
# @Author  : Steve
# @File    : 01_引入.py
# @Software: PyCharm
# @Time    : 2020-11-16 下午 2:42

"""
如果 a+b+c=1000，且 a^2 + b^2 = c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
"""
import time

import math
def test():
    start = time.time()
    for a in range(1001):
        for b in range(1001):
            for c in range(1001):
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                    print(f"a={a},b={b},c={c}")

    print(f'cost time:{time.time()-start:.2f}s') # 1669.11s=27min

start = time.time()
for a in range(1001):
    for b in range(1001):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print(f"a={a},b={b},c={c}")

print(f'cost time:{time.time()-start:.2f}s')



start = time.time()
for c in range(int(math.sqrt(2) *1000 -1000),1000):
    for b in range(1001-c):
        a = 1000 - c - b
        if a ** 2 + b ** 2 == c ** 2:
            print(f"a={a},b={b},c={c}")

print(f'cost time:{time.time()-start:.2f}s')

