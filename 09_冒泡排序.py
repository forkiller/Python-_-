# D:\Users\Administrator\Anaconda3\python.exe
# -*- coding: UTF-8 -*-
# @Author  : Steve
# @File    : 09_冒泡排序.py
# @Software: PyCharm
# @Time    : 2020-11-17 下午 12:09
import timeit
from timeit import Timer

def bubble_sort(alist):
    n = len(alist)
    for j in range(0,n-1):
        for i in range(0,n-1-j):
            if alist[i+1] < alist[i]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
    return alist

if __name__ == '__main__':
    test_list = [54,2,48,19,16,157,63,148,50,48]
    print("bubble_sort:",bubble_sort(test_list))

    t1 = Timer("bubble_sort([54,2,48,19,16,157,63,148,50,48])","from __main__ import bubble_sort")
    t1_time = t1.timeit(number=1000)
    print(f"bubble_sort:{t1_time:.2e}",'s')
    print(f"bubble_sort:{t1_time}",'s')

    new_list = sorted(test_list)
    print("sorted:", new_list)
    t2 = timeit.Timer("sorted([54,2,48,19,16,157,63,148,50,48])")
    t2_time = t2.timeit(number=1000)
    print(f"sorted:{t2_time:.2e}",'s')
    print(f"sorted:",t2_time,'s')


