# D:\Users\Administrator\Anaconda3\python.exe
# -*- coding: UTF-8 -*-
# @Author  : Steve
# @File    : 06_Stack.py
# @Software: PyCharm
# @Time    : 2020-11-17 上午 11:06


class Stack(object):
    """栈"""
 
    def __init__(self):
        self.__items = []

    def is_empty(self):
        """判断栈是否为空"""
        return self.__items == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.__items)

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self.__items.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.__items.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__items:
            return self.__items[-1]
        return None


if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(6)
    print(s.size())
    print(s.pop())
    print(s.peek())
