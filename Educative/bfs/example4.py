"""
Problem Statement
Given a binary tree, populate an array to represent the averages of all of its levels.
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    nodes = deque()
    if root:
        nodes.append(root)
    while nodes:
        length = len(nodes)
        nodes_sum = 0
        for _ in range(len(nodes)):
            current_node = nodes.popleft()
            nodes_sum += current_node.val
            if current_node.left:
                nodes.append(current_node.left)
            if current_node.right:
                nodes.append(current_node.right)
        result.append(nodes_sum/length)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()
