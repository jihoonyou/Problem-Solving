'''
나만 안되는 연애
https://www.acmicpc.net/problem/14621
'''
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
univ = [0] + list(input().split())
graph = []
dating = []
parents = [i for i in range(N+1)]

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
    u,v,d = map(int,input().split())
    graph.append((d,u,v))

graph.sort()

for i in range(M):
    d,u,v = graph[i]
    if find(u) != find(v) and univ[u] != univ[v]:
        union(u,v)
        dating.append(d)
if len(dating) == N-1:
    print(sum(dating))
else:
    print(-1)
