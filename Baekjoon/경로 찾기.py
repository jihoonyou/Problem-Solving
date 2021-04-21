'''
경로 찾기
https://www.acmicpc.net/problem/11403
'''
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]


def floyd_warshall():
    # k = 거쳐가는노드
    for k in range(N):
        # i = 출발 노드
        for i in range(N):
            # j = 도착노드
            for j in range(N):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
floyd_warshall()

for row in graph:
    print(*row)
