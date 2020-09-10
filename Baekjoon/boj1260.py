"""
DFS와 BFS
https://www.acmicpc.net/problem/1260
"""
import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    adj_list[X].append(Y)
    adj_list[Y].append(X)

for i in range(N+1):
    adj_list[i].sort()


def dfs(current_node, step_trace):
    step_trace.append(current_node)
    for connected_node in adj_list[current_node]:
        if connected_node not in step_trace:
            step_trace = dfs(connected_node, step_trace)
    return step_trace


def bfs(current_node):
    step_trace = []
    visited = [False for _ in range(N+1)]
    deq = deque([current_node])
    visited[current_node] = True
    while deq:
        current_node = deq.popleft()
        step_trace.append(current_node)
        for connected_node in adj_list[current_node]:
            if not visited[connected_node]:
                deq.append(connected_node)
                visited[connected_node] = True
    return step_trace


print(*dfs(V, []))
print(*bfs(V))
