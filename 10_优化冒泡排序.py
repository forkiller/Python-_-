# D:\Users\Administrator\Anaconda3\python.exe
# -*- coding: UTF-8 -*-
# @Author  : Steve
# @File    : 10_优化冒泡排序.py
# @Software: PyCharm
# @Time    : 2020-11-17 下午 12:31

import timeit
from timeit import Timer

def bubble_sort(alist):
    """优化冒泡排序的内层循环"""
    n = len(alist)
    for j in range(0,n-1):
        # 交换次数
        exchange_count = 0
        for i in range(0,n-1-j):
            if alist[i+1] < alist[i]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                exchange_count += 1
        # 如果从头到尾都没有交换数值，则交换次数为0，
        # 表示该顺序表是已排序的,最优时间复杂度：O(n)
        if 0 == exchange_count:
            return alist
    return alist

if __name__ == '__main__':
    test_list = [54,2,48,19,16,157,63,148,50,48,54,2,48,19,16,157,63,148,50,48]
    print("test_list:",bubble_sort(test_list))

    t1 = Timer(f"bubble_sort({test_list})", "from __main__ import bubble_sort")
    t1_time = t1.timeit(number=100000)
    print(f"t1_time:{t1_time:.5e}","s")

    test_list2 = [2, 2, 16, 16, 19, 19, 48, 48, 48, 48, 50, 50, 54, 54, 63, 63, 148, 148, 157, 157]
    t2 = Timer(f"bubble_sort({test_list2})", "from __main__ import bubble_sort")
    t2_time = t2.timeit(number=100000)
    print(f"t2_time:{t2_time:.5e}", "s")


