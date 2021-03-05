'''
하노이 탑 이동 순서
https://www.acmicpc.net/problem/11729
'''
import sys
N = int(sys.stdin.readline())
start = 1
end = 3
trace = []

def hanoi(n,start,end):
    if n == 1:
        trace.append((start,end))
    else:
        other = 6 - (start+end)
        hanoi(n-1,start, other)
        trace.append((start,end))
        hanoi(n-1,other, end)
hanoi(N,start,end)
print(len(trace))
for move in trace:
    print(*move)
