# D:\Users\Administrator\Anaconda3\python.exe
# -*- coding: UTF-8 -*-
# @Author  : Steve
# @File    : 15_希尔排序.py
# @Software: PyCharm
# @Time    : 2020-11-17 下午 6:18

def shell_sort(alist):
    n = len(alist)
    grap = n // 2  # grap 类似步长，当初始步长为1，即插入排序
    while grap >= 1:
        for i in range(grap, n):
            # 一直交换，至到索引为0停止
            while i > 0:
                # 插入排序,交换次序
                if alist[i] < alist[i - grap]:
                    alist[i], alist[i - grap] = alist[i - grap], alist[i]
                    i -= grap # while 终止条件
                else:
                    break
        # 缩短步长,每循环一次，就缩短一次
        grap //= 2

    return alist


if __name__ == '__main__':
    test_list = [54, 2, 48, 19, 16, 157, 63, 148, 50, 48]
    print("shell_sort:", shell_sort(test_list))
