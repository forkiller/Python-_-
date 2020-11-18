# D:\Users\Administrator\Anaconda3\python.exe
# -*- coding: UTF-8 -*-
# @Author  : Steve
# @File    : 16_快速排序.py
# @Software: PyCharm
# @Time    : 2020-11-17 下午 9:40

def quick_sort(alist, first, last):
    if first >= last:
        # 顺序表只有1个元素时，结束
        return
    low = first
    high = last
    mid_val = alist[first]

    while low < high:
        while low < high and alist[high] >= mid_val:
            """内循环中的low < high不能删除，因为确实low<high判断会导致low>high"""
            high -= 1
        # 退出循环时，[high]<mid
        alist[low] = alist[high]

        while low < high and alist[low] < mid_val:
            low += 1
        # 退出循环时，[high]>mid
        alist[high] = alist[low]

    # 退出大循环时，low=high,此时所指位置为基准元素的正确位置
    alist[low] = mid_val

    # 二分，递归
    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, 0, low - 1)
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low + 1, last)

    return alist


if __name__ == '__main__':
    test_list = [504, 2, 48, 19, 16, 157, 63, 148, 50, 48]
    print("quick_sort:", quick_sort(test_list, 0, len(test_list) - 1))
