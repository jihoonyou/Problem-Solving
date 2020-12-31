'''
소수찾기
https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3
'''
def solution(n):
    answer = 0
    sieve = [False, False] + [True]*(n-1)
    
    for i in range(2, n+1):
        if sieve[i]:
            answer += 1
            for j in range(2*i, n+1, i):
                sieve[j] = False

    return answer
'''
    answer = 0
    sieve = [True]*(n+1)
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i]:
            answer += 1
            for j in range(2*i, n+1, i):
                sieve[j] = False

    return len([i for i in range(2, n+1) if sieve[i]])
'''