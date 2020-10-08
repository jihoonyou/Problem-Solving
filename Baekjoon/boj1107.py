"""
리모컨
https://www.acmicpc.net/problem/1107
"""
import sys

N = int(sys.stdin.readline())  # goal
M = int(sys.stdin.readline())

total_pressed = abs(100-N)
broken = [False]*10

for num in map(int, sys.stdin.readline().split()):
    broken[num] = True


def check(n):
    if n == 0:
        if broken[n]:
            return 0
        else:
            return 1
    count = 0
    while n > 0:
        if broken[n % 10]:  # check each digit
            return 0
        n = n//10
        count += 1
    return count


for i in range(1000001):
    new_count = check(i)

    if new_count > 0:
        pressed_count = abs(N - i)
        total_pressed = min(total_pressed, new_count + pressed_count)

print(total_pressed)
