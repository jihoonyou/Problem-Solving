"""
소인수분해
https://www.acmicpc.net/problem/11653
"""
import sys

N = int(sys.stdin.readline())

for i in range(2, int(N**0.5)+1):
    while N % i == 0:
        N = N // i
        print(i)
    
if N > 1:
    print(N)