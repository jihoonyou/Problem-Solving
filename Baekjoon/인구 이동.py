'''
인구 이동
https://www.acmicpc.net/problem/16234
'''
import sys
from collections import deque
input = sys.stdin.readline

N,L,R = map(int, input().split() )
land = [list(map(int, input().split())) for _ in range(N)]
directions = [(0,1), (0,-1), (1,0), (-1,0)]

def is_in_bound(diff):
    return L <= diff and diff <= R

def get_diff(a,b,c,d):
    return abs(land[a][b]-land[c][d])

def bfs(r,c, total_visited, is_merged):
    total_population = 0
    total_countries = 0
    visited = set([(r,c)])
    queue = deque([(r,c)])

    while queue:
        x, y = queue.popleft()

        total_population += land[x][y]
        total_countries += 1

        for dx,dy in directions:
            nx, ny = x+dx, y+dy
            if nx >= 0 and nx < N and ny >= 0 and ny < N and (nx, ny) not in visited and (nx,ny) not in total_visited:
                diff = get_diff(nx,ny,x,y)

                if is_in_bound(diff):
                    queue.append((nx,ny))
                    visited.add((nx,ny))
                    is_merged[0] = True

    return total_population // total_countries, visited

def main():
    answer = 0
    while True:
        total_visited = set()
        union = []
        is_merged = [False]

        for i in range(N):
            for j in range(N):
                if (i,j) not in total_visited:
                    update, visited = bfs(i,j, total_visited, is_merged)
                    union.append((update,visited))
                    total_visited |= visited
                    
        for update, countries in union:
            for country in countries:
                x,y = country
                land[x][y] = update

        if not is_merged[0]:
            break
        answer += 1
    print(answer)
main()
