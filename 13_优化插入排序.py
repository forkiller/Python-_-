#!/usr/bin/env python
# -*- coding: utf-8
# @Author   : Steve
# @File     : 插入排序.py
# @Software : PyCharm
# @Time     : 2020-11-17 15:25

def insert_sort(alist):
    n = len(alist)
    # 如果后一个元素小于前一个元素，则交换次序
    for j in range(1,n):
        # 最后一个数值和倒二个数值比较，使用降序
        while j > 0:
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
                j -= 1
            else:
                """当顺序表已排好次序时，进入循环后直接跳出"""
                break

    return alist


if __name__ == '__main__':
    alist = [54, 228, 90, 87, 67, 84, 84, 82, 23, 19]
    print(insert_sort(alist))

    list2 = [54, 90, 87, 67, 84, 84, 82, 23, 19, 228]
    print(insert_sort(list2))
