'''
스타트와 링크
https://www.acmicpc.net/problem/14889
'''
import sys

N = int(sys.stdin.readline())
players = [list(map(int,sys.stdin.readline().split()))  for _ in range(N)]
_min = sys.maxsize
joined = [False]*N

def dfs(index, cnt):
    global _min
    if cnt == N//2:
        start = 0
        link = 0
        for i in range(N):
            for j in range(N):
                if joined[i] and joined[j]:
                    start += players[i][j]
                elif not joined[i] and not joined[j]:
                    link += players[i][j]
        _min = min(_min, abs(start-link))
    for i in range(index, N):
        if joined[i]: continue
        joined[i] = True
        dfs(i+1, cnt+1)
        joined[i] = False
dfs(0,0)
print(_min)
