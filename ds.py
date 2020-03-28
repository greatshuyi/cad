# -*- coding: utf-8 -*-

from collections import deque


class DSTreeNode(object):

    def __init__(self, parent=None, child=None, sibling=None, element=None):
        self.__parent = parent
        self.__child = child
        self.__sibling = sibling
        self.__element = element
        self.__depth = 0

    @property
    def depth(self):
        if self.__parent is not None:
            if self.__parent.__depth + 1 == self.__depth:
                return self.__depth
            else:
                return self.__parent.__depth + 1
        else:
            return self.__depth

    @depth.setter
    def set_depth(self, val):
        self.__depth = val


    @property
    def is_leaf(self):
        return self.__child is None


class DSTreePosition(object):

    def __init__(self, container, node):
        self.container = container
        self.node = node

    @property
    def element(self):
        return self.node.element

    @property
    def parent(self):
        self.node = self.node.parent
        return self

    @property
    def child(self):
        self.node = self.node.child
        return self

    @property
    def sibling(self):
        self.node = self.node.sibling
        return self

    def children(self):
        if self.node.child is not None:
            self.node = self.node.child
            yield self

        while self.node.sibling is not None:
            self.node = self.node.sibling
            yield self

    def __eq__(self, other):
        return type(other) is type(self) and other.node is self.node


class DSTree(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def _validate_node(self, node):
        return node.container is self

    def insert_root(self, element):
        n = DSTreeNode(element=element)
        n.depth = 0
        if self.root is not None:
            self.root.parent = n
            n.child = self.root
        self.size += 1
        return n

    def insert_child(self, node, element):
        n = DSTreeNode(parent=node, element=element)
        if node.child is not None:
            n.sibling = node.child
        node.child = n
        self.size += 1
        return n

    def insert_children(self, node, elements):
        prev = None
        nodes = []
        for element in elements:
            n = DSTreeNode(parent=node, element=element, sibling=prev)
            n.depth = node.depth + 1
            prev = n
            nodes.append(n)

        if node.child is not None:
            node[-1].sibling = node.child

        node.child = nodes[0]
        self.size += len(elements)
        return nodes[0]

    def all_order(self, node):

        if not self._validate_node(node):
            return

        stack = deque()
        stack.append(node)
        first = True

        while stack:

            n = stack[0]
            yield n, first    # node, is_first_access

            child = n.child
            if first and child is not None and self._validate_node(child):
                stack.appendleft(child)
                first = True
                continue

            n = stack.popleft()
            yield n, False

            sibling = n.sibling
            if first and sibling is not None and self._validate_node(sibling)
                stack.appendleft(sibling)
                first = True
                continue















