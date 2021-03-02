'''
N과 M (5)
https://www.acmicpc.net/problem/15654
'''
import sys

N,M = map(int,sys.stdin.readline().split())
num_in_series = sorted(map(int, sys.stdin.readline().split()))
visited = [False]*N
nums = []

def find_permutation():
    if len(nums) == M:
        print(*nums)
        return
    for i in range(N):
        if visited[i]:
            continue
        nums.append(num_in_series[i])
        visited[i] = True

        find_permutation()

        nums.pop()
        visited[i] = False

find_permutation()
