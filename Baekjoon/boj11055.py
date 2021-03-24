'''
가장 큰 증가 부분 수열
https://www.acmicpc.net/problem/11055
'''
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [el for el in A]

for i in range(1,N):

    for j in range(i):
        if A[j]<A[i]:
            dp[i] = max(dp[i], dp[j]+A[i])
print(max(dp))
