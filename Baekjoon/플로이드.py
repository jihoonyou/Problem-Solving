'''
플로이드
https://www.acmicpc.net/problem/11404
'''
import sys
input = sys.stdin.readline
INF = float('inf')

n = int(input())
m = int(input())
graph = [[INF]*n for _ in range(n)]

for _ in range(m):
    i,j,c = map(int,input().split())
    if graph[i-1][j-1] > c:
        graph[i-1][j-1] = c
# 대각선 처리
for i in range(n):
    graph[i][i] = 0

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph [k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
floyd_warshall()

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0

for row in graph:
    print(*row)
