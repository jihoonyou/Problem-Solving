"""
마법사 상어와 파이어볼
https://www.acmicpc.net/problem/20056
"""
import sys
from collections import deque

input = sys.stdin.readline

position = deque()
n,m,k = map(int, input().split())
directions = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
grid = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r,c,m,s,d = map(int, input().split()) # mass, speed, direction
    grid[r-1][c-1].append([m,s,d])
    position.append([r-1,c-1])


def move():
    length = len(position)
    next_grid = []
    # 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다
    for _ in range(length):
        x,y = position.popleft()
        for _ in range(len(grid[x][y])):
            mass, speed, dir = grid[x][y].popleft()

            dx,dy = directions[dir]
            nx,ny = (x+speed*dx)%n, (y+speed*dy)%n
            position.append([nx,ny])
            next_grid.append([nx,ny,mass,speed,dir])

    for _r, _c, _m, _s, _d in next_grid:
        grid[_r][_c].append([_m,_s,_d])

    for i in range(n):
        for j in range(n):
            # 2개 이상의 파이어볼이 있는 칸
            if len(grid[i][j]) > 1:
                odd, even = False, False
                total_mass = 0
                total_speed = 0
                # 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
                for mass, speed, dir in grid[i][j]:
                    total_mass += mass
                    total_speed += speed
                    if dir % 2 == 0:
                        even = True
                    else:
                        odd = True
                # 파이어볼은 4개의 파이어볼로 나누어진다
                new_mass = total_mass // 5 # 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.`
                new_speed = total_speed // len(grid[i][j]) # 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
                grid[i][j] = deque()
                if new_mass > 0: # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
                    if even and not odd or not even and odd:
                        grid[i][j].append([new_mass,new_speed,0])
                        grid[i][j].append([new_mass, new_speed, 2])
                        grid[i][j].append([new_mass, new_speed, 4])
                        grid[i][j].append([new_mass, new_speed, 6])
                    else:
                        grid[i][j].append([new_mass, new_speed, 1])
                        grid[i][j].append([new_mass, new_speed, 3])
                        grid[i][j].append([new_mass, new_speed, 5])
                        grid[i][j].append([new_mass, new_speed, 7])
                # 질량이 0인 파이어볼은 소멸되어 없어진다.


for _ in range(k):
    move()
answer = 0
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            for mass, _, _ in grid[i][j]:
                answer += mass
print(answer)
