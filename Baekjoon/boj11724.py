from collections import deque
"""
연결 요소의 개수
https://www.acmicpc.net/problem/11724s
"""
import sys
sys.setrecursionlimit(10000)
N, M = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    adj_list[X].append(Y)
    adj_list[Y].append(X)


def bfs_to_find_connected_component():
    count = 0
    deq = deque()
    for node in range(1, N+1):
        if not visited[node]:
            visited[node] = True
            deq.append(node)
            count += 1
        while deq:
            curr_node = deq.popleft()
            for connected_node in adj_list[curr_node]:
                if not visited[connected_node]:
                    visited[connected_node] = True
                    deq.append(connected_node)
    print(count)


bfs_to_find_connected_component()

# def dfs(v):
#     visited[v] = True
#     for connected_node in adj_list[v]:
#         if not visited[connected_node]:
#             dfs(connected_node)
# count = 0
# for i in range(1,N+1):
#     if not visited[i]:
#         count += 1
#         dfs(i)
# print(count)
