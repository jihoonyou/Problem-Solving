"""
순열 사이클
https://www.acmicpc.net/problem/10451
"""
import sys
from collections import deque

T = int(sys.stdin.readline())


def bfs(V, visited, adj_list):
    visited[V] = True
    deq = deque([V])
    while deq:
        current_node = deq.popleft()
        for connected_node in adj_list[current_node]:
            if not visited[connected_node]:
                visited[connected_node] = True
                deq.append(connected_node)

for _ in range(T):
    N = int(sys.stdin.readline())
    adj_list = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    N_in_list = list(range(1, N+1))
    given_list = list(map(int, sys.stdin.readline().split()))
    count = 0

    for X, Y in zip(N_in_list, given_list):
        adj_list[X].append(Y)
        adj_list[Y].append(X)

    for i in range(1, N+1):
        if not visited[i]:
            count += 1
            bfs(i, visited, adj_list)
    print(count)

# def dfs(V):
#     visited[V] = True
#     connected_node = given_list[V]
#     if not visited[connected_node]:
#         dfs(connected_node)

# for _ in range(T):
#     N = int(sys.stdin.readline())
#     visited = [False] * (N+1)
#     given_list = [0] + list(map(int, sys.stdin.readline().split()))
#     count = 0
#     for i in range(1, N+1):
#         if not visited[i]:
#             count += 1
#             dfs(i)
#     print(count)
