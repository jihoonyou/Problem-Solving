'''
N과 M (6)
https://www.acmicpc.net/problem/15655
'''
import sys

N,M = map(int,sys.stdin.readline().split())
num_in_series = sorted(map(int, sys.stdin.readline().split()))
visited = [False]*N
nums = []
def find_combinations():
    if len(nums) == M:
        print(*nums)
        return
    for i in range(N):
        if visited[i]:
            continue
        if len(nums) and nums[-1] > num_in_series[i]:
            continue
        nums.append(num_in_series[i]) 
        visited[i] = True

        find_combinations()

        nums.pop()
        visited[i] = False

find_combinations()
