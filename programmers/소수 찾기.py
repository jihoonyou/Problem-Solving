'''
소수 찾기
https://programmers.co.kr/learn/courses/30/lessons/42839
'''
from itertools import permutations
def solution(numbers):
    answer = 0
    perms = set()
    for i in range(len(numbers)):
        perms |= set(map(int,map(''.join, permutations(list(numbers), i + 1))))
    
    sieve = [False, False] + [True]*(max(perms)-1)

    for i in range(2,len(sieve)):
        if sieve[i]:
            for j in range(2*i, len(sieve), i):
                sieve[j] = False
    
    for num in perms:
        if sieve[num]:
            answer += 1
    
    return answer