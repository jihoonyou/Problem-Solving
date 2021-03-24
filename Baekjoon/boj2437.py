'''
저울
https://www.acmicpc.net/problem/2437
'''
import sys

N = int(sys.stdin.readline())

weights = sorted(map(int,sys.stdin.readline().split()))

current_weight = 0
for weight in weights:
    if current_weight + 1 >= weight:
        current_weight += weight
    else:
        break
# 1 2  4
# 0 + 1 >= 1
# 1 + 1 >= 2
# 2 + 1 >= 3
print(current_weight + 1)