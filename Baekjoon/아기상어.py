'''
아기상어
https://www.acmicpc.net/problem/16236
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
space = [list(map(int,input().split())) for _ in range(N)]
moves = [(-1,0), (0,-1), (0,1), (1,0)] # 위, 좌, 우, 하
baby_shark = None
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            baby_shark = [i,j]
            space[i][j] = 0
            break

def bfs(baby_shark):
    q = deque([baby_shark])
    visited = set([(baby_shark[0],baby_shark[1])])
    size = 2
    eat_so_far = 0
    eaten = False
    answer = 0
    time = 0

    while q:
        length = len(q)
        q = deque(sorted(q))

        for _ in range(length):
            x,y = q.popleft()
            fish = space[x][y]

            if fish != 0 and fish < size:
                eat_so_far += 1
                if size == eat_so_far:
                    size += 1
                    eat_so_far = 0
                space[x][y] = 0
                eaten = True
                q = deque()
                visited = set([(x,y)])
                answer = time
            
            for dx,dy in moves:
                nx, ny = x+dx, y+dy
                if nx >= 0 and nx < N and ny >= 0 and ny < N and (nx,ny) not in visited:
                    if space[nx][ny] <= size:
                        visited.add((nx,ny))
                        q.append((nx,ny))

            if eaten:
                eaten = False
                break
        time += 1        
    return answer

print(bfs(baby_shark))
