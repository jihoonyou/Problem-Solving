'''
구슬 탈출 2
https://www.acmicpc.net/problem/13460
'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

maze = [ [0 for _ in range(M)] for _ in range(N) ]
hole_pos = []
red_pos = []
blue_pos = []
for i in range(N):
    line = input()
    for j in range(M):
        maze[i][j] = line[j]
        print(line[j])
        if line[j] == 'R':
            red_pos.append([i,j])
        if line[j] == 'B':
            blue_pos.append([i,j])
        if line[j] == 'O':
            hole_pos.append([i,j])
print(maze)
print(hole_pos,red_pos, blue_pos)