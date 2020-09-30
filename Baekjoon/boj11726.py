"""
2×n 타일링
https://www.acmicpc.net/problem/11726
"""
import sys

N = int(sys.stdin.readline())

dp = [0]*(N+1)

for i in range(1, N+1):
    if i == 1:
        dp[1] = 1
    elif i == 2:
        dp[2] = 2
    else:
        dp[i] = (dp[i-2] + dp[i-1])

print(dp[N] % 10007)

# 해설 https://assb.tistory.com/33