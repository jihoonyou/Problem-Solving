'''
https://leetcode.com/problems/insert-interval/
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end, i = 0, 1, 0

        while i < len(intervals) and newInterval[start] > intervals[i][start]:
            i += 1
        intervals.insert(i,newInterval)
        result = [intervals[0]]
        
        for i in range(1,len(intervals)):
            interval = intervals[i]
            if result[-1][end] >= interval[start]:
                result[-1][end] = max(interval[end],result[-1][end])
            else:
                result.append(interval)
        return result