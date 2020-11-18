# D:\Users\Administrator\Anaconda3\python.exe
# -*- coding: UTF-8 -*-
# @Author  : Steve
# @File    : singlenode.py
# @Software: PyCharm
# @Time    : 2020-11-16 下午 4:25

class SingleNode():
    """ 单链表节点"""

    def __init__(self, item):
        # _item 存放数据元素
        self.elem = item
        # _next 下一节点的标识
        self.next = None


class SingleLinkList():
    """单链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """链表是否为空,判断头指针是否为空即可"""
        return self._head == None

    def length(self):
        """链表长度,遍历链表，尾节点指向None，当未到达尾部时"""
        count = 0
        curr = self._head
        while curr != None:
            count += 1
            curr = curr.next
        return count

    def travel(self):
        """遍历整个链表"""
        curr = self._head
        while curr != None:
            print(curr.elem, end=" ")
            curr = curr.next
        print("")

    def add(self, item):
        """链表头部添加元素"""
        node = SingleNode(item)
        # 将新节点的链接域指向头结点，即 _head 指向的位置
        node.next = self._head
        # 将链表的头_head 指向新节点
        self._head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = SingleNode(item)
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

    def insert(self, pos, item):
        """指定位置添加元素"""
        node = SingleNode(item)
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
            while count < pos - 1:
                curr = curr.next
                count += 1
            node.next = curr.next
            curr.next = node

    def remove(self, item):
        """删除节点
        用以前一后2个指针来处理
        """
        if self.is_empty():
            return
        curr = self._head
        pre = None
        while curr != None:
            if curr.elem == item:
                # 删除只有一个头节点的链表，curr==self._head 等价于 not pre
                if curr == self._head:
                    self._head = curr.next
                else:
                    pre.next = curr.next
                break
            else:
                pre = curr
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

    new_sll = SingleLinkList()
    new_sll.add(1)
    new_sll.travel()
    new_sll.remove(1)
    new_sll.travel()
    print(new_sll.is_empty())
