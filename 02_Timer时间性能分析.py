# D:\Users\Administrator\Anaconda3\python.exe
# -*- coding: UTF-8 -*-
# @Author  : Steve
# @File    : 02_Timer时间性能分析.py
# @Software: PyCharm
# @Time    : 2020-11-16 下午 3:21 

from timeit import Timer

""" 生成列表耗时测试 """


def test_1():
    test_list = []
    for i in range(1000):
        test_list = test_list + [i]


def test_2():
    test_list = []
    for i in range(1000):
        test_list.append(i)


def test_3():
    return [i for i in range(1000)]


def test_4():
    list(range(1000))


t1 = Timer("test_1()", "from __main__ import test_1")
print('+ concat ', t1.timeit(number=1000), "second")

t2 = Timer("test_2()", "from __main__ import test_2")
print('append concat ', t2.timeit(number=1000), "second")

t3 = Timer("test_3()", "from __main__ import test_3")
print('[for in] concat ', t3.timeit(number=1000), "second")

t4 = Timer("test_4()", "from __main__ import test_4")
print('list[iter] concat ', t4.timeit(number=1000), "second")

""" 弹出列表元素耗时测试 """
x = list(range(2000000))
pop_zero = Timer("x.pop(0)", "from __main__ import x")
print('pop_zero', pop_zero.timeit(number=1000), "second")

pop_end = Timer("x.pop()", "from __main__ import x")
print('pop_end', pop_end.timeit(number=1000), "second")

"""list 头插法和尾插法"""
def test_append():
    li = list(range(1000))
    for i in range(10000):
        li.append(i)


def test_insert():
    li = list(range(1000))
    for i in range(10000):
        li.insert(0, i)


t5 = Timer("test_append()", "from __main__ import test_append")
print("append cost time", t5.timeit(number=1000), 's')

t6 = Timer("test_insert()", "from __main__ import test_insert")
print("insert cost time", t6.timeit(number=1000), 's')
