"""
Problem Statement
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level from left to right in separate sub-arrays.
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    deq = deque()
    if root:
        deq.append(root)

    while deq:
        length = len(deq)
        node_list = []
        for _ in range(length):
            current_node = deq.popleft()
            node_list.append(current_node.val)
            if current_node.left:
                deq.append(current_node.left)
            if current_node.right:
                deq.append(current_node.right)
        if node_list:
            result.append(node_list)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
