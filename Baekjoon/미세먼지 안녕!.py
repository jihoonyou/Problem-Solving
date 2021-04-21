'''
미세먼지 안녕!
https://www.acmicpc.net/problem/17144
'''
import sys
input = sys.stdin.readline
import copy

R,C,T = map(int,input().split())
moves = [(0,1),(0,-1),(1,0),(-1,0)]
fine_dust = [ list(map(int,input().split())) for _ in range(R)]
one = ''
two = ''
for i in range(R):
    if fine_dust[i][0] == -1:
        one = i
        two = i+1 
        break



def bfs(): # 확산
    # 새 보드에 생성
    temp = [[0]*C for _ in range(R)]
    # 전체 순회
    for x in range(R):
        for y in range(C):
            if fine_dust[x][y] == 0:
                continue
            if fine_dust[x][y] == -1:
                temp[x][y] = -1
                continue
            available = []
            for dx,dy in moves:
                nx, ny = x+dx, y+dy
                if nx >= 0 and nx < R and ny >= 0 and ny < C: # (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
                    if fine_dust[nx][ny] != -1: # 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
                        available.append((nx,ny)) # 확산되는 양
            update_value = fine_dust[x][y] // 5

            # 현 위치의 양
            # fine_dust[x][y] -= update_value*len(available)
            temp[x][y] += fine_dust[x][y]
            temp[x][y] -= update_value*len(available)
            for nx,ny in available:
                temp[nx][ny] += update_value
    return temp

def rotate():
    # 시계방향
    # ->
    temp = fine_dust[one][C - 1]
    for i in range(C - 1, 1, - 1):
        fine_dust[one][i] = fine_dust[one][i - 1]
    fine_dust[one][1] = 0

    # 위
    temp_1 = fine_dust[0][C - 1]
    for i in range(one - 1):
        fine_dust[i][C - 1] = fine_dust[i + 1][C - 1]
    fine_dust[one - 1][C - 1] = temp

    # <-
    temp_2 = fine_dust[0][0]
    for i in range(C - 2):
        fine_dust[0][i] = fine_dust[0][i + 1]
    fine_dust[0][C - 2] = temp_1

    # 아래
    for i in range(one - 1, 1, -1):
        fine_dust[i][0] = fine_dust[i - 1][0]
    fine_dust[1][0] = temp_2

    # 반시계빵향
    # ->
    temp = fine_dust[two][C - 1]
    for i in range(C - 1, 1, -1):
        fine_dust[two][i] = fine_dust[two][i - 1]
    fine_dust[two][1] = 0

    # 밑
    temp_1 = fine_dust[R - 1][C - 1]
    for i in range(R - 1, two + 1, -1):
        fine_dust[i][C - 1] = fine_dust[i - 1][C - 1]
    fine_dust[two + 1][C - 1] = temp

    # <-
    temp_2 = fine_dust[R - 1][0]
    for i in range(C - 2):
        fine_dust[R - 1][i] = fine_dust[R - 1][i + 1]
    fine_dust[R - 1][C - 2] = temp_1

    # 위
    for i in range(two + 1, R - 1):
        fine_dust[i][0] = fine_dust[i + 1][0]
    fine_dust[R - 2][0] = temp_2


for _ in range(T):
    fine_dust = bfs()
    rotate()


answer = 2
for li in fine_dust:
    answer += sum(li)
print(answer)
