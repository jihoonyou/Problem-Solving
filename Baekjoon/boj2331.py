"""
반복순열
https://www.acmicpc.net/problem/2331
"""
import sys

A, P = map(int, sys.stdin.readline().split())
D = [A]
i = 0

while True:
    num = D[i]
    new_num = 0
    while num:
        temp = num % 10
        new_num += temp**P
        num = num // 10
    if new_num in D:
        D.append(new_num)
        i += 1
        break
    else:
        D.append(new_num)
        i += 1

print(D.index(D[i]))
