# D:\Users\Administrator\Anaconda3\python.exe
# -*- coding: UTF-8 -*-
# @Author  : Steve
# @File    : 07_Queue.py
# @Software: PyCharm
# @Time    : 2020-11-17 上午 11:32

class Deque(object):
    """双队列"""

    def __init__(self):
        self.__list = []

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):

        """返回队列的大小"""
        return len(self.__list)

    def add_front(self,item):

        """往队列头中添加一个item元素"""
        self.__list.insert(0,item)

    def add_rear(self,item):

        """往队列尾中添加一个item元素"""
        self.__list.append(item)



    def remove_front(self):

        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    def remove_rear(self):

        """从队列尾部删除一个元素"""
        return self.__list.pop()

    def travel(self):
        for i in self.__list:
            print(i,end=" ")
        print("")

if __name__ == '__main__':
    q = Deque()
    print(q.is_empty())
    q.add_front(1)
    q.add_rear(2)
    q.add_front(3)
    q.add_front(4)
    print(q.size())
    q.travel()
    print(q.remove_front())
    print(q.remove_rear())
    q.travel()

