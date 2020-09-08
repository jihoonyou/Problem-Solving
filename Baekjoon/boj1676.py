"""
팩토리얼 0의 개수
https://www.acmicpc.net/problem/1676
"""
import sys

N = int(sys.stdin.readline())
res = 1

while N:
    res *= N
    N -= 1

res_in_str = str(res)

for idx,digit in enumerate(res_in_str[::-1]):
    if digit != '0':
        print(idx)
        break

# print(N//5 + N//25 + N//125) https://itadventure.tistory.com/22 해설 참조