'''
수 찾기
https://www.acmicpc.net/problem/1920
'''
import sys

_ = int(sys.stdin.readline())
N = sorted(map(int, sys.stdin.readline().split()))
_ = int(sys.stdin.readline())
M = map(int, sys.stdin.readline().split())

for m in M:
    left, right = 0, len(N) - 1
    flag = False
    while left <= right:
        mid = (left + right) // 2
        if m == N[mid]:
            print(1)
            flag = True
            break
        elif m > N[mid]:
            left = mid + 1
        else:
            right = mid - 1
    if not flag:
        print(0)
