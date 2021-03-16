'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]*len(prices)
        current = prices[0]
        
        for day in range(1,len(prices)):
            if current > prices[day]:
                current = prices[day]            
            dp[day] = max(dp[day-1], prices[day]-current)

        return dp[-1]