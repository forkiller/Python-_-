# D:\Users\Administrator\Anaconda3\python.exe
# -*- coding: UTF-8 -*-
# @Author  : Steve
# @File    : 04_SinCyclLinkedList.py
# @Software: PyCharm
# @Time    : 2020-11-16 下午 6:31

class Node():
    def __int__(self, item):
        self.elem = item
        self.next = None


class SinCyclLinkedList():
    def __int__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """返回链表的长度"""
        if self.is_empty():
            return 0
        curr = self._head
        count = 1
        while curr.next != self._head:
            count += 1
            curr = curr.next
        # 退出循环时，curr = None
        return count

    def travel(self):
        """遍历"""
        curr = self._head
        while curr.next != self._head:
            print(curr.elem)
            curr = curr.next
        print("")

    def add(self, item):
        """在头部添加一个节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            node.next = self._head
            curr = self._head
            while curr.next != self._head:
                curr = curr.next
            curr.next = node
            self._head = node

    def append(self, item):
        """在尾部添加一个节点"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            curr = self._head
            while curr.next != self._head:
                curr = curr.next
            curr.next = node
            node.next = self._head

    def insert(self, pos, item):
        """在指定位置pos添加节点"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            curr = self._head
            count = 0
            while count < (pos - 1):
                curr = curr.next
                count += 1
            # 退出循环时，curr 指向 pos-1的节点
            node.next = curr.next
            curr.next = node

    def remove(self, item):
        """删除一个节点"""
        if self.is_empty():
            return False
        curr = self._head
        pre = None

        # 头删
        if curr.elem == item:
            # 链表不止1个元素
            if curr.next != self._head:
                while curr.next != self._head:
                    curr = curr.next
                curr.next = self._head.next
                self._head = self._head.next
            # 链表只有1个元素
            else:
                self._head = None
            return True
        # 中删和尾删
        else:
            pre = self._head
            while curr.next != self._head:
                # 中删
                if curr.elem == item:
                    pre.next = curr.next
                    return True
                else:
                    curr = curr.next
                    pre = curr
            # 尾删
            if curr.elem == item:
                pre.next = self._head
                return True
        return False

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return
        curr = self._head
        while curr.next != self._head:
            if curr.elem == item:
                return True
            else:
                curr = curr.next
        return False

if __name__ == '__main__':
    sll = SinCyclLinkedList()
    print(sll.is_empty())
    sll.append(5)
    sll.append(6)
    sll.append(7)
    sll.add(4)
    sll.travel()
    sll.insert(3, 100)
    sll.travel()
    print(sll.length())
    print(sll.search(101))
    sll.remove(4)
    sll.travel()
