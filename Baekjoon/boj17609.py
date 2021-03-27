'''
회문
https://www.acmicpc.net/problem/17609
'''
import sys
N = int(sys.stdin.readline())
result = []
PALINDROME = 0
PSUEDO_PALIDROME = 1
NON_PALINDROME = 2

def is_palindrome(left, right):
    while left < right:
        if word[left] != word[right]:
            skip_left = is_psudo_palindrome(left+1, right)
            skip_right = is_psudo_palindrome(left, right - 1)
            if skip_left or skip_right:
                return PSUEDO_PALIDROME
            else:
                return NON_PALINDROME
        else:
            left += 1
            right -= 1
    return PALINDROME 


def is_psudo_palindrome(left,right):
    while left < right:
        if word[left] != word[right]:
            return False
        left +=1
        right -=1
    return True

for _ in range(N):
    word = sys.stdin.readline().strip()
    left, right = 0, len(word) - 1
    print(is_palindrome(left,right))
