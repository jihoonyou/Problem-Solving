'''
정복자
https://www.acmicpc.net/problem/14950
'''
import sys
input = sys.stdin.readline

N,M,t = map(int,input().split())
parents = [i for i in range(N+1)]
answer = []
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

graph = []
for _ in range(M):
    A,B,C = map(int,input().split())
    graph.append((C,A,B))

graph.sort()

for i in range(len(graph)):
    C,A,B = graph[i]
    if find(A) != find(B):
        union(A,B)
        answer.append(C+len(answer)*t)

print(sum(answer))
