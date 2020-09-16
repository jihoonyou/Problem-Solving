"""
미로 탐색
https://www.acmicpc.net/problem/2178
"""
import sys
from collections import deque 

N,M = map(int,sys.stdin.readline().split())
maze = []

for _ in range(N):
    maze.append(list(map(int,list(sys.stdin.readline().rstrip()))))


def bfs():
    deq = deque([(0,0)])
    step = 1
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    destination = False
    
    while deq:
        length = len(deq)
        for _ in range(length):
            y,x = deq.popleft()
            maze[y][x] = 0
            for move_y, move_x in directions:
                new_y = y + move_y
                new_x = x + move_x
                if 0 <= new_y < len(maze) and 0 <= new_x < len(maze[0]) and maze[new_y][new_x] == 1:
                    maze[new_y][new_x] = 0
                    deq.append((new_y,new_x))
                if new_y == N - 1 and new_x == M - 1:
                    destination = True
                    break
            if destination:
                break
        step += 1
        if destination:
            return step
    
print(bfs())