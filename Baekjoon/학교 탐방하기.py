'''
학교 탐방하기
https://www.acmicpc.net/problem/13418
'''
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
parents = [i for i in range(N+1)]
graph = []

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a = parents[a]
    b = parents[b]

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for _ in range(M+1):
    A,B,C = map(int, input().split())
    graph.append((C,A,B))

graph.sort()
worst = 0
for i in range(M+1):
    C,A,B = graph[i]
    if find(A) != find(B):
        union(A,B)
        if C == 0:
            worst += 1

graph.sort(reverse=True)
parents = [i for i in range(N+1)]

best = 0
for i in range(M+1):
    C,A,B = graph[i]
    if find(A) != find(B):
        union(A,B)
        if C == 0:
            best += 1

print(worst*worst - best*best)
