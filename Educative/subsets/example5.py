"""
Problem Statement
For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

Example 1:

Input: N=2
Output: (()), ()()
Example 2:

Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()
"""
from collections import deque


class Parentheses_String:
    def __init__(self, string, open_count, close_count):
        self.string = string
        self.open_count = open_count
        self.close_count = close_count


def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(Parentheses_String('',0,0))

    while queue:
        current_parentheses = queue.popleft()
        if current_parentheses.open_count == num and current_parentheses.close_count == num:
            result.append(current_parentheses.string)
        else:
            if current_parentheses.open_count < num:
                queue.append(Parentheses_String(current_parentheses.string + '(', current_parentheses.open_count + 1, current_parentheses.close_count))
            if current_parentheses.open_count > current_parentheses.close_count:
                queue.append(Parentheses_String(current_parentheses.string + ')', current_parentheses.open_count, current_parentheses.close_count+1))


    return result


def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


main()
