"""
Right View of a Binary Tree (easy)
Given a binary tree, return an array containing nodes in its right view. 
The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
"""
from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    result = []
    deq = deque()
    if root:
        deq.append(root)

    while deq:
        length = len(deq)
        current_node = None
        for _ in range(length):
            current_node = deq.popleft()
            if current_node.left:
                deq.append(current_node.left)
            if current_node.right:
                deq.append(current_node.right)
        result.append(current_node)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()
