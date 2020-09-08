"""
팩토리얼
https://www.acmicpc.net/problem/10872
"""
import sys

N = int(sys.stdin.readline())
res = 1

while N:
    res *= N
    N -= 1

print(res)