'''
먹을 것인가 먹힐 것인가
https://www.acmicpc.net/problem/7795
'''
import sys
T = int(sys.stdin.readline())

def binary_search(target, nums):
    left = 0
    right = len(nums) - 1
    res = -1
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] < target:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res

for _ in range(T):
    N,M = map(int,sys.stdin.readline().split())
    A = sorted(map(int,sys.stdin.readline().split()))
    B = sorted(map(int,sys.stdin.readline().split()))
    count = 0
    for a in A:
        count += binary_search(a,B)+1

    print(count)


