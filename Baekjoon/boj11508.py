'''
2+1 세일
https://www.acmicpc.net/problem/11508
'''
import sys

N = int(sys.stdin.readline())
C = []
cost = 0
for _ in range(N):
    C.append(int(sys.stdin.readline()))
C.sort(reverse=True)

for i in range(len(C)):
    if i % 3 == 2:
        continue
    cost += C[i]
print(cost)
# 3 2 3 2
# (3,3,2) + (2)
# (4 5 5) (5 5 6) 11 + 10