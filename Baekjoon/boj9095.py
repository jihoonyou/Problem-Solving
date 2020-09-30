"""
1, 2, 3 더하기
https://www.acmicpc.net/problem/9095
"""
import sys

T = int(sys.stdin.readline())
dp = [0]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,len(dp)):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    

for _ in range(T):
    N = int(sys.stdin.readline())
    print(dp[N])