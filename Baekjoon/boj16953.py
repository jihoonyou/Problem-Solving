'''
A → B
https://www.acmicpc.net/problem/16953
'''
import sys
from collections import deque
A,B = map(int, sys.stdin.readline().split())
count = 1
queue = deque([A])

while queue:
    current_size = len(queue)
    for _ in range(current_size):
        node = queue.popleft()
        if node == B:
            print(count)
            sys.exit()
        candidate_1 = node*2
        candidate_2 = node*10+1
        if candidate_1 <= B:
            queue.append(candidate_1)
        if candidate_2 <= B:
            queue.append(candidate_2)

    count += 1
print(-1)

# 거꾸로 하면 더 빠르게 연산 가능
