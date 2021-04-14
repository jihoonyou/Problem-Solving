'''
세부
https://www.acmicpc.net/problem/13905
'''
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N,M = map(int,input().split())
s,e = map(int,input().split())

graph = []
parents = [i for i in range(N+1)]
weight_limit = 1000001

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

for _ in range(M):
    h1,h2,k = map(int,input().split())
    graph.append((k,h1,h2))

graph.sort(reverse=True)
is_conneceted = False

for i in range(len(graph)):

    k,h1,h2 = graph[i]
    if find(h1) != find(h2):
        union(h1,h2)
        weight_limit = min(weight_limit,k)
        if find(s) == find(e):
            is_conneceted = True
            break

if is_conneceted:
    print(weight_limit)
else:
    print(0)
