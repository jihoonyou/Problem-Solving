"""
Problem Statement #
Given a binary tree, populate an array to represent its zigzag level order traversal. 
You should populate the values of all nodes of the first level from left to right, 
then right to left for the next level and keep alternating in the same manner for the following levels.
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    deq = deque()
    reverse = True
    if root:
        deq.append(root)

    while deq:
        length = len(deq)
        node_list = deque()

        for _ in range(length):
            curr_node = deq.popleft()
            if reverse:
                node_list.append(curr_node.val)
            else:
                node_list.appendleft(curr_node.val)
            if curr_node.left:
                deq.append(curr_node.left)
            if curr_node.right:
                deq.append(curr_node.right)

        if node_list:
            result.append(list(node_list))
        reverse = not reverse
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
