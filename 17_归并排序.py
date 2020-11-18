# D:\Users\Administrator\Anaconda3\python.exe
# -*- coding: UTF-8 -*-
# @Author  : Steve
# @File    : 17_归并排序.py
# @Software: PyCharm
# @Time    : 2020-11-17 下午 11:31

def merge_sort(alist):
    """归并排序"""
    if len(alist) <= 1:
        return alist
    # 递归拆分，拆分成单个元素时结束递归
    mid = len(alist) // 2
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    # 合并
    left_point, right_point = 0, 0
    result = []
    while left_point < len(left_li) and right_point < len(right_li):
        if left_li[left_point] < right_li[right_point]:
            result.append(left_li[left_point])
            left_point += 1
        else:
            result.append(right_li[right_point])
            right_point += 1

    # 退出循环时，一个数组为空，最后把另一个数组的剩余部分添加到result过来即可
    result += left_li[left_point:]
    result += right_li[right_point:]
    return result


if __name__ == '__main__':
    test_list = [504, 2, 48, 119, 16, 157, 63, 148, 50, 48]
    print("merge_sort:", merge_sort(test_list))
