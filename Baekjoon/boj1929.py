"""
소수 구하기
https://www.acmicpc.net/problem/1929
"""
import sys

M,N = map(int, sys.stdin.readline().split())

sieve = [False,False] + [True]*(N-1)

for i in range(2,N+1):
    if sieve[i]:
        if i >= M:
           print(i)
        for j in range(i*2, N+1,i):
            sieve[j] = False