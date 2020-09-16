"""
토마토
https://www.acmicpc.net/problem/7576
"""
import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

tomato_box = []

deq = deque()
count_zero = 0
for y in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for x in range(M):
        if row[x] == 1:
            deq.append((y, x))
        if row[x] == 0:
            count_zero +=1
    tomato_box.append(row)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(count_zero):
    days = -1
    while deq:
        length = len(deq)
        for idx in (range(length)):
            curr_y, curr_x = deq.popleft()

            for idx in range(4):
                nxt_y = curr_y + dy[idx]
                nxt_x = curr_x + dx[idx]
                if 0 <= nxt_y < N and 0 <= nxt_x < M:
                    if tomato_box[nxt_y][nxt_x] == 0:
                        tomato_box[nxt_y][nxt_x] = -1
                        deq.append((nxt_y, nxt_x))
                        count_zero -= 1
        days += 1

    if count_zero:
        return -1    
    return days
print(bfs(count_zero))
