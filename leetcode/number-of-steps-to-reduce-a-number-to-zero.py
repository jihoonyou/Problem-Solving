'''
https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3637/s
'''
class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
       
        while num:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            count += 1
        
        return count