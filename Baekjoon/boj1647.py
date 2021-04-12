'''
도시 분할 계획
https://www.acmicpc.net/problem/1647
'''
import sys
import heapq

N,M = map(int,sys.stdin.readline().split())

parents = [i for i in range(0,N+1)]
heap = []
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

for _ in range(M):
    A,B,C = map(int,sys.stdin.readline().split())
    heapq.heappush(heap,(C,A,B))
answer = []
while heap:
    C,A,B = heapq.heappop(heap)
    if find(A) != find(B):
        union(A,B)
        answer.append(C)

print(sum(answer[:-1]))
