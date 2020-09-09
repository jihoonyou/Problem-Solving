"""
Problem Statement #
Given a binary tree and a node, find the level order successor of the given node in the tree. 
The level order successor is the node that appears right after the given node in the level order traversal.
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):
    deq = deque()
    if root:
        deq.append(root)
    while deq:
        current_node = deq.popleft()
        if current_node.left:
            deq.append(current_node.left)
        if current_node.right:
            deq.append(current_node.right)
        if current_node.val == key:
            break
    return deq[0] if deq else None
            


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)


main()
