'''
N과 M (7)
https://www.acmicpc.net/problem/15656
'''
import sys

N,M = map(int,sys.stdin.readline().split())
num_in_series = sorted(map(int, sys.stdin.readline().split()))
nums = []

def find_combinations():
    if len(nums) == M:
        print(*nums)
        return
    for i in range(N):
        nums.append(num_in_series[i]) 
        find_combinations()
        nums.pop()


find_combinations()
