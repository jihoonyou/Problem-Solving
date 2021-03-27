'''
사이클 게임
https://www.acmicpc.net/problem/20040
'''
import sys
n,m = map(int,sys.stdin.readline().split())

parent = [i for i in range(n)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b: 
        parent[b] = a
    else:
        parent[a] = b

result = 1
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    if find(a) == find(b):
        break
    else:
        union(a,b)
        result += 1

if result == m+1:
    result = 0
print(result)
