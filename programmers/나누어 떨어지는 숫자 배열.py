'''
나누어 떨어지는 숫자 배열
https://programmers.co.kr/learn/courses/30/lessons/12910
'''
def solution(arr, divisor):
    answer = sorted([num for num in arr if num % divisor == 0])
    return [-1] if len(answer) == 0 else answer