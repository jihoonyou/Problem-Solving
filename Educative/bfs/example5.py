"""
Problem Statement
Find the minimum depth of a binary tree. 
The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    depth = 0
    deq = deque()
    if root:
        deq.append(root)

    while deq:
        depth += 1
        length = len(deq)
        for _ in range(length):
            current_node = deq.popleft()
            if not current_node.left and not current_node.right:
                return depth
            if current_node.left:
                deq.append(current_node.left)
            if current_node.right:
                deq.append(current_node.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
