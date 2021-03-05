'''
https://www.acmicpc.net/problem/14888
'''
import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
add, sub, mul, div = map(int,sys.stdin.readline().split())

_min, _max = 1e9, -1e9

def dfs(index, result, add, sub, mul, div):
    global _min, _max 
    if index == len(nums):
        _min = min(_min, result)
        _max = max(_max, result)
        return
    else:
        if add:
            dfs(index+1, result+nums[index], add-1, sub, mul, div)
        if sub:
            dfs(index+1, result-nums[index], add, sub-1, mul, div)
        if mul:
            dfs(index+1, result*nums[index], add, sub, mul-1, div)
        if div:
            dfs(index+1, int(result/nums[index]), add, sub, mul, div-1)

dfs(1, nums[0], add,sub,mul,div)
print(_max)
print(_min)
