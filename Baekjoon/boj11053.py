'''
가장 긴 증가하는 부분 수열
https://www.acmicpc.net/problem/11053
'''
import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

dp = [1]*len(A)

for i in range(1,N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], 1+dp[j])

print(max(dp))