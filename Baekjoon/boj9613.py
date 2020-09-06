"""
GCD 합
https://www.acmicpc.net/problem/9613
"""
import sys

def gcd(x,y):
    while y:
        x,y = y, x%y
    return x

T = int(sys.stdin.readline())

for _ in range(T):
    nums = list(map(int, sys.stdin.readline().split()))[1:]
    gcd_sum = 0
    for idx in range(len(nums)-1):
        for idx2 in range(idx+1,len(nums)):
            gcd_sum += gcd(nums[idx],nums[idx2])
    print(gcd_sum)