'''
https://leetcode.com/problems/number-of-1-bits/
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_count = 0
        while n:
            bit_count += (1 & n)
            n = n >> 1
        return bit_count