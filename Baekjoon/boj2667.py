"""
단지번호붙이기
https://www.acmicpc.net/problem/2667
"""
import sys
from collections import deque
N = int(sys.stdin.readline())
apartments = []
apartments_info = []

for _ in range(N):
    apartments.append(list(map(int,list(sys.stdin.readline().rstrip()))))

def dfs(y,x):
    apartments[y][x] = 0
    apartments_info[-1] += 1

    if y > 0 and apartments[y - 1][x] == 1:
        dfs(y-1,x)
    if y + 1 < len(apartments) and apartments[y+1][x] == 1:
        dfs(y+1,x)
    if x > 0 and apartments[y][x - 1] == 1:
        dfs(y, x-1)
    if x + 1 < len(apartments[0]) and apartments[y][x+1] == 1:
        dfs(y,x+1)
    

for i in range(N):
    for j in range(len(apartments[i])):
        if apartments[i][j] == 1:
            apartments_info.append(0)
            dfs(i,j)
apartments_info.sort()
print(len(apartments_info))
for info in apartments_info:
    print(info)