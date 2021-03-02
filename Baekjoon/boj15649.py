"""
N과 M (1)
https://www.acmicpc.net/problem/15649
"""
import sys

N, M = map(int, sys.stdin.readline().split())
visited = [False]*N

num_in_series = list(range(1, N+1))
nums = []


def dfs():
    if len(nums) == M:
        print(*nums)
        return

    for i in range(N):
        if visited[i]:
            continue
        nums.append(num_in_series[i])
        visited[i] = True

        dfs()

        nums.pop()
        visited[i] = False

dfs()

# from itertools import permutations
# N, M = map(int, input().split())
# P = permutations(range(1, N+1), M)  # iter(tuple)
# for i in P:
#     print(' '.join(map(str, i)))  # tuple -> str