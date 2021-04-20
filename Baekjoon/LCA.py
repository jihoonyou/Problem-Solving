'''
LCA
https://www.acmicpc.net/problem/11437
'''
import sys
from functools import lru_cache
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
parents = [0]*(N+1)
depths = [0]*(N+1)
visited = [False]*(N+1)

for _ in range(N-1):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(x, depth):
    visited[x] = True
    depths[x] = depth
    for y in graph[x]:
        if visited[y]:
            continue
        parents[y] = x
        dfs(y, depth+1)

dfs(1,0)

@lru_cache(maxsize=32)
def LCA(x,y):
    while depths[x] != depths[y]:
        if depths[x] < depths[y]:
            y = parents[y]
        else:
            x = parents[x]
    
    while x != y:
        x = parents[x]
        y = parents[y]
    
    return x

M = int(input())

for _ in range(M):
    x,y = map(int,input().split())
    print(LCA(x,y))
