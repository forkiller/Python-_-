#!/usr/bin/env python
# -*- coding: utf-8
# @Author   : Steve
# @File     : 选择排序.py
# @Software : PyCharm
# @Time     : 2020-11-17 15:10

def selection_sort(alist):
    """选择排序，每次都选择极值，放在指定位置"""
    n = len(alist)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if alist[j] < alist[min_index]:
                min_index = j
        # 退出循环时，min_index指向当次循环中的最小数值（即最小数的索引）

        # 如果选择出的数据不在正确位置，择交换数值
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


if __name__ == '__main__':
    alist = [54, 228, 90, 87, 67, 84, 28, 82, 23, 19]
    print(selection_sort(alist))
