# D:\Users\Administrator\Anaconda3\python.exe
# -*- coding: UTF-8 -*-
# @Author  : Steve
# @File    : 18_二分查找.py
# @Software: PyCharm
# @Time    : 2020-11-18 上午 12:09

def binary_search(alist, item):
    """非递归实现，alist需确保是有序表"""
    first = 0
    last = len(alist) - 1
    # first <= last 时，顺序表只有1个元素
    while first <= last:
        mid = (first + last) // 2
        if item == alist[mid]:
            print("index=", mid)
            return True
        # 查找值小于中间值，在左子表中查找
        if item < alist[mid]:
            # 左子表的最后一个元素时中间值mid的前一个
            last = mid - 1
        else:
            # 右子表的第一个元素时中间值mid的后一个
            first = mid + 1
    return False


def binary_search2(alist, item):
    """递归实现"""
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if item == alist[mid]:
            print("index=", mid)
            return True
        else:
            if item < alist[mid]:
                # 左子表的最后一个元素时中间值mid的前一个
                return binary_search2(alist[:mid], item)
            else:
                # 右子表的第一个元素时中间值mid的后一个
                return binary_search2(alist[mid+1:], item)


if __name__ == '__main__':
    testlist = [2, 16, 48, 49, 50, 63, 119, 148, 157, 504]
    print(binary_search(testlist, 48))
    print(binary_search2(testlist, 13))
