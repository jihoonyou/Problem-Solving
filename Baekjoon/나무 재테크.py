'''
나무 재테크
https://www.acmicpc.net/problem/16235
'''
import sys
input = sys.stdin.readline
moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
N,M,K = map(int,input().split())

current_food = [ [5]*N for _ in range(N)]
add_food = [list(map(int,input().split())) for _ in range(N)]
land = [ [[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int,input().split())
    land[x-1][y-1].append(z)

def spring_and_summer():
    for i in range(N):
        for j in range(N):
            if land[i][j]:
                land[i][j].sort() #  하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 
                _land = []
                dead_food = 0
                for age in land[i][j]:
                    if age <= current_food[i][j]: # 자신의 나이만큼 양분을 먹고
                        _land.append(age+1) # 봄에는 나무가 자신의 나이만큼 양분을 먹고, 
                        current_food[i][j] -= age # 나이가 1 증가한다. 
                    else: # 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다
                        dead_food += age // 2
                # 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다.
                current_food[i][j] += dead_food
                land[i][j] = _land

def autumn(): # 가을에는 나무가 번식한다. 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.    
    for i in range(N):
        for j in range(N):
            if land[i][j]:
                for age in land[i][j]:
                    if age % 5 == 0:
                        for dx, dy in moves:
                            nx, ny = i+dx, j+dy
                            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                                land[nx][ny].append(1)
def winter(): # 겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가
    for i in range(N):
        for j in range(N):
            current_food[i][j] += add_food[i][j]

for _ in range(K):
    spring_and_summer()
    autumn()
    winter()

count = 0
for i in range(N):
    for j in range(N):
        count += len(land[i][j])

print(count)
