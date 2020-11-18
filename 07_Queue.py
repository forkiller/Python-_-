# D:\Users\Administrator\Anaconda3\python.exe
# -*- coding: UTF-8 -*-
# @Author  : Steve
# @File    : 07_Queue.py
# @Software: PyCharm
# @Time    : 2020-11-17 上午 11:32

class Queue(object):
    """队列"""

    def __init__(self):
        self.__list = []

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):

        """返回队列的大小"""
        return len(self.__list)

    def enqueue(self,item):

        """往队列中添加一个item元素"""
        # 以列表末尾为队列尾部
        self.__list.append(item)

        """
        1.入队操作较多时，选用顺序表尾部添加，入队append()时间复杂度为O(1)
        2.出队操作较多时，选用顺序表头部添加，出队pop()时间复杂度为O(1)
        """

    def dequeue(self):

        """从队列头部删除一个元素"""
        self.__list.pop(0)

if __name__ == '__main__':
    q = Queue()
    print(q.is_empty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.size())
    print(q.dequeue())

