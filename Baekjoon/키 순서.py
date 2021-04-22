'''
키 순서
https://www.acmicpc.net/problem/2458
'''
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [ [0]*n for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

answer = 0
for i in range(n):
    students = 0
    for j in range(n):
        students += graph[i][j] + graph[j][i]
    if n-1 == students:
        answer +=1

print(answer)
