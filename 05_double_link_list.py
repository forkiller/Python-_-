# D:\Users\Administrator\Anaconda3\python.exe
# -*- coding: UTF-8 -*-
# @Author  : Steve
# @File    : 05_double_link_list.py
# @Software: PyCharm
# @Time    : 2020-11-16 下午 6:42

from singlenode import SingleLinkList


class Node(object):
    """双向链表节点"""
    def __int__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(SingleLinkList):
    """双向链表"""
    def add(self, item):
        """链表头部添加元素"""
        node = Node(item)
        # 将新节点的链接域指向头结点，即 _head 指向的位置
        node.next = self._head
        # 将链表的头_head 指向新节点
        self._head = node
        node.next.prev = node

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        # 先判断链表是否为空
        if self.is_empty():
            self._head = node
        else:
            curr = self._head
            """用 curr.next == None 让指针定位到最后一个元素，
            当 curr.next = None 时，curr即为最后一个元素
            """
            while curr.next != None:
                curr = curr.next
            curr.next = node
            node.prev = curr

    def insert(self, pos, item):
        """指定位置添加元素"""
        node = Node(item)
        # 判断 pos 的值,若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(node)
        # 若指定位置pos大于链表长度，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(node)
        else:
            curr = self._head
            count = 0
            """
            让指定定位到指定位置的前一个元素处，修改前一个元素的next
            """
            while count < pos:
                curr = curr.next
                count += 1
            # 退出循环是 curr 指向 指定位置的元素
            node.next = curr
            node.prev = curr.prev
            node.prev.next = node
            curr.prev = node

    def remove(self, item):
        """删除节点,先找到节点在删除
        用以前一后2个指针来处理
        """
        if self.is_empty():
            return
        curr = self._head
        while curr != None:
            if curr.elem == item:
                # 链接只有一个头节点
                if curr == self._head:
                    self._head = curr.next
                    if curr.next:
                        curr.next.prev = None
                else:
                    curr.prev.next = curr.next
                    if curr.next:
                        curr.next.prev = curr.prev
                break
            else:
                curr = curr.next

    def search(self, item):
        """查找节点是否存在"""
        curr = self._head
        # curr.next != None 会漏下最后一个元素
        while curr != None:
            if curr.elem == item:
                return True
            curr = curr.next
        return False


if __name__ == '__main__':
    sll = SingleLinkList()
    print(sll.is_empty())
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.add(1)
    sll.travel()
    sll.insert(3, 100)
    sll.travel()
    print("length=", sll.length())
    print("isExist=", sll.search(101))
    sll.remove(100)
    sll.travel()
