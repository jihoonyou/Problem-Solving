'''
정수 제곱근
https://www.acmicpc.net/problem/2417
'''
import sys

start = 1
target = int(sys.stdin.readline())
end = target

res = 0
while start <= end:
    mid = (start + end) // 2
    if mid**2 <= target:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)