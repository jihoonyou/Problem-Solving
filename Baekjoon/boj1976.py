'''
여행 가자
https://www.acmicpc.net/problem/1976
'''
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [i for i in range(N+1)]

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

for start in range(1, N+1):
    maps = list(map(int,input().split()))
    for x in range(1, len(maps) + 1):
        if maps[x-1] == 1:
            union(start, x)

plan = list(map(int,input().split()))
result = set([find(city) for city in plan])

if len(result) == 1:
    print('YES')
else:
    print("NO")
