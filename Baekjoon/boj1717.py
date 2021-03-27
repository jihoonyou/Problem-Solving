'''
집합의 표현
https://www.acmicpc.net/problem/1717
'''
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [i for i in range(n+1)]

# 부모 노드를 찾는 함수
def find(parents, x):
    if parents[x] == x:
        return x
    parents[x] = find(parents, parents[x])
    return parents[x]

# 두 부모 노드를 합침
def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)

    if a < b:
        parents[b] = a
    else: parents[a] = b


for _ in range(m):
    flag, a, b = map(int,input().split())

    if flag:
        print('YES' if find(parents, a) == find(parents, b) else 'NO')
    else:
        union(parents,a,b)
