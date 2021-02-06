'''
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3630/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        result = []
        self.dfs(root, result, 0)
        
        return result
        
        
    def dfs(self, node, trace, depth):
        if depth == len(trace):    
            trace.append(node.val)
        if node.right:
            self.dfs(node.right, trace, depth + 1)
        if node.left:
            self.dfs(node.left, trace, depth + 1)