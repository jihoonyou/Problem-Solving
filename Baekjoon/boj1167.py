"""
트리의 지름
https://www.acmicpc.net/problem/1167
풀이:
1. 루트 node를 기준으로 가장 먼 노드와, 해당 노드까지의 거리를 찾는다.
2. 해당 노드를 기준으로 가장 먼 노드와 거리를 찾는다.
"""
import sys
from collections import deque

r = sys.stdin.readline
V = int(r())
adj_list = [[] for _ in range(V+1)]

for _ in range(V):
    path_info = list(map(int, r().split()))
    node = path_info[0]
    for i in range(1, len(path_info)-1, 2):
        neighbor_node, weight = path_info[i], path_info[i+1]
        adj_list[node].append((neighbor_node, weight))


def bfs(node):
    visited = [False]*(V+1)
    visited[node] = True
    farthest_node, max_weight = node, 0
    q = deque([(node, 0)])

    while q:
        current_node, current_weight = q.popleft()
        if current_weight > max_weight:
            farthest_node = current_node
            max_weight = current_weight
        for info in adj_list[current_node]:
            if not visited[info[0]]:
                visited[info[0]] = True
                q.append((info[0], current_weight + info[1]))

    return [farthest_node, max_weight]


print(bfs(bfs(1)[0])[1])
