"""
N과 M (2)
https://www.acmicpc.net/problem/15650
"""
import sys
r = sys.stdin.readline

N, M = map(int, r().split())

nums = list(range(1, N+1))
visited = [False] * N
answer = []


def dfs(x):
    if len(answer) == M:
        print(*answer)
        return
    for index in range(N):
        if visited[index]:
            continue
        if len(answer) and answer[-1] > nums[index]:
            continue
        answer.append(nums[index])
        visited[index] = True
        dfs(x+1)
        answer.pop()
        visited[index] = False


dfs(0)
