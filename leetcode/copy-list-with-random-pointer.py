'''
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3635/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dup_node_dict = {}

        node = head
        while node:
            dup_node_dict[node] = Node(node.val)
            node = node.next
            
        node = head
        while node:
            dup_node_dict[node].next = dup_node_dict.get(node.next)
            dup_node_dict[node].random = dup_node_dict.get(node.random)
            node = node.next
        
        return dup_node_dict.get(head)