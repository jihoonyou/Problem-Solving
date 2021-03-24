'''
게임을 만든 동준이
https://www.acmicpc.net/problem/2847
'''
import sys
N = int(sys.stdin.readline())
scores = []
count = 0
for _ in range(N):
    scores.append(int(sys.stdin.readline()))

for i in range(N-1, 0, -1):
    if scores[i] <= scores[i-1]:
        diff = scores[i-1] - scores[i] + 1
        scores[i-1] -= diff
        count += diff
print(count)