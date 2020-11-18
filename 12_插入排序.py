#!/usr/bin/env python
# -*- coding: utf-8
# @Author   : Steve
# @File     : 插入排序.py
# @Software : PyCharm
# @Time     : 2020-11-17 15:25

def insert_sort(alist):
    n = len(alist)
    # 如果后一个元素小于前一个元素，则交换次序
    for i in range(1,n):
        # 最后一个数值和倒二个数值比较，使用降序
        for j in range(i,0,-1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
    return alist


if __name__ == '__main__':
    alist = [54, 228, 90, 87, 67, 84, 28, 82, 23, 19]
    print(insert_sort(alist))
