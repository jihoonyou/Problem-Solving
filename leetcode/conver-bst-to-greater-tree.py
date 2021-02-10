# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.update_sum = 0
        self.reverse_inorder(root)
        return root
    
    def reverse_inorder(self, node):
        if not node:
            return
        self.reverse_inorder(node.right)
        self.update_sum += node.val
        node.val = self.update_sum
        self.reverse_inorder(node.left)