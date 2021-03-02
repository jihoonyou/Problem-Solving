'''
N과 M (8)
https://www.acmicpc.net/problem/15657
'''
import sys

N,M = map(int,sys.stdin.readline().split())
num_in_series = sorted(map(int, sys.stdin.readline().split()))
nums = []

def find_combinations(start):
    if len(nums) == M:
        print(*nums)
        return
    for i in range(start, N):
        nums.append(num_in_series[i]) 
        find_combinations(i)
        nums.pop()


find_combinations(0)
