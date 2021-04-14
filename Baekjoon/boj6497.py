'''
전력난
https://www.acmicpc.net/problem/6497
'''
import sys
input = sys.stdin.readline

def find(x):
    if cities[x] == x:
        return x
    cities[x] = find(cities[x])
    return cities[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        cities[b] = a
    else:
        cities[a] = b
while True:
    m,n = map(int,input().split())

    if m == 0 and n == 0:
        break
    cities = [i for i in range(m+1)]
    graph = []
    answer = 0

    for _ in range(n):
        x,y,z = map(int,input().split())
        graph.append((z,x,y))
        answer += z

    graph.sort(key = lambda x:x[0])

    for z,x,y in graph:
        if find(x) != find(y):
            union(x,y)
            answer -=z
    print(answer)