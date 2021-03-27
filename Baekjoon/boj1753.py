'''
최단경로
https://www.acmicpc.net/problem/1753
'''
import sys
import heapq

inf = sys.maxsize
V, E = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
adjacency_list = [[] for _ in range(V+1)]
dijkstra_check = [inf]*(V+1)
heap = []

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    adjacency_list[u].append((w,v))

def dijkstra(start):
    dijkstra_check[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        cur_weight, node = heapq.heappop(heap)
        for w, next_node in adjacency_list[node]:
            next_weight = w+cur_weight
            if next_weight < dijkstra_check[next_node]:
                dijkstra_check[next_node] = next_weight
                heapq.heappush(heap, (next_weight, next_node))
dijkstra(start)
for i in dijkstra_check[1:]:
    print(i if i != inf else 'INF')
