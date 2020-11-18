# D:\Users\Administrator\Anaconda3\python.exe
# -*- coding: UTF-8 -*-
# @Author  : Steve
# @File    : 19_二叉树.py
# @Software: PyCharm
# @Time    : 2020-11-18 上午 10:23

class Node(object):
    """节点类"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""

    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        node = Node(elem)
        # 如果树是空的，对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            # 对已有的节点进行层次遍历
            while queue:
                # 弹出队列的第一个元素
                curr = queue.pop(0)
                if curr.lchild == None:
                    curr.lchild = node
                    return
                elif curr.rchild == None:
                    curr.rchild = node
                    return
                else:
                    # 如果左右子树都不为空，加入队列继续判断
                    queue.append(curr.lchild)
                    queue.append(curr.rchild)

    # 深度优先遍历
    def preorder(self, node):
        """递归实现先序遍历：根节点->左子树->右子树"""
        if node == None:
            return
        print(node.elem, end="")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        """递归实现中序遍历:左子树->根节点->右子树"""
        if node == None:
            return
        self.inorder(node.lchild)
        print(node.elem, end="")
        self.inorder(node.rchild)

    def postorder(self, node):
        """递归实现后序遍历:左子树->右子树->根节点"""
        if node == None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end="")

    # 广度优先遍历(层次遍历)
    def breadth_travel(self):
        """利用队列实现树的层次遍历"""
        if self.root == None:
            return
        else:
            queue = []
            queue.append(self.root)
            while queue:
                node = queue.pop(0)
                print(node.elem)
                if node.lchild != None:
                    queue.append(node.lchild)
                if node.rchild != None:
                    queue.append(node.rchild)


if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.breadth_travel()
    print("先序遍历:", end="")
    tree.preorder(tree.root)
    # print("")
    print("\n中序遍历:", end="")
    tree.inorder(tree.root)
    print("\n后序遍历:", end="")
    tree.postorder(tree.root)
