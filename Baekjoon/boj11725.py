"""
트리의 부모 찾기
https://www.acmicpc.net/problem/11725
"""
import sys
from collections import deque
N = int(sys.stdin.readline())

parents = [0]*(N+1)
parents[1] = 1

tree = {}

for line in sys.stdin:
    if line == '\n':
        break
    X, Y = map(int,line.split())
    if X not in tree:
        tree[X] = [Y]
    else:
        tree[X].append(Y)
    if Y not in tree:
        tree[Y] = [X]
    else:
        tree[Y].append(X)

queue = deque([1])

while queue:
    length = len(queue)
    for _ in range(length):
        parent = queue.popleft()
        for child in tree[parent]:
            if parents[child] == 0:
                queue.append(child)
                parents[child] = parent

for idx in range(2,len(parents)):
    print(parents[idx])
