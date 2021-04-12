'''
최소 스패닝 트리
https://www.acmicpc.net/problem/1197
'''
import sys
import heapq

V,E = map(int,sys.stdin.readline().split())
heap = []
for _ in range(E):
    A,B,C = map(int,sys.stdin.readline().split())
    heapq.heappush(heap,(C,A,B))
parents = [i for i in range(0,V+1)]

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

answer = []
while heap:
    C,A,B = heapq.heappop(heap)
    if find(A) != find(B):
        union(A,B)
        answer.append(C)

print(sum(answer))
