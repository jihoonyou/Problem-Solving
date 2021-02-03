'''
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3627/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        one_step = head
        if not one_step or not one_step.next:
            return False
        two_step = head.next
        
        while two_step.next and two_step.next.next:
            one_step = one_step.next
            two_step = two_step.next.next
            if one_step == two_step:
                return True
        return False