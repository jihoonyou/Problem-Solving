"""
N과 M (1)
https://www.acmicpc.net/problem/15649
"""
import sys

N, M = map(int, sys.stdin.readline().split())
visited = [False]*N

num_in_series = list(range(1, N+1))
nums = []


def dfs(x):
    if len(nums) == M:
        print(*nums)
        return

    for i in range(N):
        if visited[i]:
            continue
        nums.append(num_in_series[i])
        visited[i] = True

        dfs(x+1)

        nums.pop()
        visited[i] = False


dfs(0)
