'''
전기가 부족해
https://www.acmicpc.net/problem/10423
'''
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
power_plant = list(map(int,input().split()))
parents = [i for i in range(N+1)]
graph = []
answer = 0

for _ in range(M):
    u,v,w = map(int,input().split())
    graph.append((w,u,v))

graph.sort(key = lambda x:x[0])

def find(x):
    if x == parents[x]:
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

for i in range(len(power_plant)-1):
    union(power_plant[i],power_plant[i+1])

for (w,u,v) in graph:
    if find(u) != find(v):
        union(u,v)
        answer += w

print(answer)
