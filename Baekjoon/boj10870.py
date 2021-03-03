'''
피보나치 수 5
https://www.acmicpc.net/problem/10870
'''
import sys
n = int(sys.stdin.readline())

def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)
print(fibo(n))