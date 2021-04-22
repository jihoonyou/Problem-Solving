'''
배열 돌리기 1
https://www.acmicpc.net/problem/16926
'''
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
arr = [ input().split() for _ in range(n)]

def rotate(r,inner):
    for _ in range(r): # 회전 숫자
        for t in range(inner):
            temp = arr[t][t]
            for x in range(t+1, n-t) :
                arr[x][t], temp = temp, arr[x][t]
            for y in range(t+1, m-t) :
                arr[n-1-t][y], temp = temp, arr[n-1-t][y]
            for x in range(n-1-t-1,t-1,-1) :
                arr[x][m-1-t], temp = temp, arr[x][m-1-t]
            for y in range(m-1-t-1, t-1, -1) :
                arr[t][y], temp = temp, arr[t][y]

rotate(r, min(n,m)//2)

for l in arr:
    print(*l)
