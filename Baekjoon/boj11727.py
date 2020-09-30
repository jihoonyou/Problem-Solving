"""
2×n 타일링 2
https://www.acmicpc.net/problem/11727
"""
import sys

N = int(sys.stdin.readline())

dp = [0]*(N+1)

for i in range(1, N+1):
    if i == 1:
        dp[1] = 1
    elif i == 2:
        dp[2] = 3
    else:
        dp[i] = (dp[i-1] + dp[i-2]*2)

print(dp[N] % 10007)
