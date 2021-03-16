'''
https://leetcode.com/problems/container-with-most-water/
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        most_water = 0
        while l < r:
            width = r - l
            most_water = max(most_water, width*min(height[l],height[r]))
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return most_water