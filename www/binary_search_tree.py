#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Gu Xianxiong'

class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BST:
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            self.insert(data)


    def search(self, node, parent, data):
        """查找

        当二叉查找树不为空时:
            首先将给定值与根结点的关键字比较，若相等，则查找成功
            若小于根结点的关键字值，递归查左子树
            若大于根结点的关键字值，递归查右子树
            若子树为空，查找不成功

        Args:
            node: a Node instance, the node for compare with.
            parent: a Node instance, parent node of the param 'node', use to return.
            data: given value

        Return:
            flag: bool, result for search node.
            n: a Node instance.
            p: a Node instance, new node insert into its child
        Raises:
        """
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)


    def insert(self, data):
        """插入

        树的结构在查找过程中，当树中不存在关键字等于给定值的结点时再进行插入
        当查找不成功时，在返回的父节点下插入新的叶子节点。大于父节点为右孩子，小于父节点为左孩子

        Args:
            data: a Node instance.

        Return:
        Raises:
        """
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
        if data > p.data:
            p.rchild = new_node
        else:
            p.lchild = new_node


    def delete(self, root, data):
        """删除

        1. 如果待删除的节点是叶子节点，那么可以立即被删除
        2. 如果节点只有一个儿子，则将此节点parent的指针指向此节点的儿子，然后删除节点
        3. 如果节点有两个儿子，则将其右子树的最小数据代替此节点的数据，并将其右子树的最小数据删除

        Args:
            root: a Node instance.
            data:

        Return:
        Raises:
        """
        flag, n, p = self.search(root, root, data)
        if flag is False:
            print
            "无该关键字，删除失败"
        else:
            if n.lchild is None:
                if n == p.lchild:
                    p.lchild = n.rchild
                else:
                    p.rchild = n.rchild
                del p
            elif n.rchild is None:
                if n == p.lchild:
                    p.lchild = n.lchild
                else:
                    p.rchild = n.lchild
                del p
            else:  # 左右子树均不为空
                pre = n.rchild
                if pre.lchild is None:
                    n.data = pre.data
                    n.rchild = pre.rchild
                    del pre
                else:
                    next = pre.lchild
                    while next.lchild is not None:
                        pre = next
                        next = next.lchild
                    n.data = next.data
                    pre.lchild = next.rchild
                    del p




    def preOrderTraverse(self, node):
        """先序遍历

        1. 访问根节点
        2. 先序遍历左子树
        3. 先序遍历右子树

        Args:
            node: a Node instance.

        Return:
        Raises:
        """
        if node is not None:
            print(node.data)
            self.preOrderTraverse(node.lchild)
            self.preOrderTraverse(node.rchild)


    def inOrderTraverse(self, node):
        """中序遍历

        1. 中序遍历左子树
        2. 访问根节点
        3. 中序遍历右子树

        Args:
            node: a Node instance.

        Return:
        Raises:
        """
        if node is not None:
            self.inOrderTraverse(node.lchild)
            print(node.data)
            self.inOrderTraverse(node.rchild)


    def postOrderTraverse(self, node):
        """ 后序遍历.

        1. 后序遍历左子树
        2. 后序遍历右子树
        3. 访问根节点

        Args:
            node: a Node instance.

        Return:
        Raises:
        """
        if node is not None:
            self.postOrderTraverse(node.lchild)
            self.postOrderTraverse(node.rchild)
            print(node.data)


if __name__ == '__main__':
    a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
    bst = BST(a)  # 创建二叉查找树

    print("---preOrder---")
    bst.preOrderTraverse(bst.root)  # 前序遍历
    print("---inOrder---")
    bst.inOrderTraverse(bst.root)  # 中序遍历
    print("---postOrder---")
    bst.postOrderTraverse(bst.root) # 后序遍历
