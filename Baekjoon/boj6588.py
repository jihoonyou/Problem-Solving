"""
골드바흐의 추측
https://www.acmicpc.net/problem/6588
"""
import sys

N = 1000000
sieve = [False,False] + [True]*(N-1)

for i in range(2,N+1):
    if sieve[i]:
        for j in range(i*2,N+1,i):
            sieve[j] = False

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    for i in range(3, N//2+1):
        if sieve[i] and sieve[N-i]:
            print('{} = {} + {}'.format(N, i, N-i))
            break
    else:
        print('Goldbach\'s conjecture is wrong.')