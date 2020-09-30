"""
1로 만들기
https://www.acmicpc.net/problem/1463
"""
import sys

X = int(sys.stdin.readline())

dp = [0]*(X+1)

for i in range(2, X+1):
    if i % 6 == 0:
        dp[i] = min(1 + dp[i//3], 1 + dp[i-1], 1 + dp[i//2])
    elif i % 3 == 0:
        dp[i] = min(1 + dp[i//3], 1 + dp[i-1])
    elif i % 2 == 0:
        dp[i] = min(1 + dp[i//2], 1 + dp[i-1])
    else:
        dp[i] = 1 + dp[i-1]
print(dp[X])
