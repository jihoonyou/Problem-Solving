"""
Problem Statement
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
"""
from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_start(head,length):
    pointer1 = head
    pointer2 = head
    while length > 0:
        pointer2 = pointer2.next
        length -= 1
    
    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
        
    return pointer1


def calculate_cycle_num(slow):
    count = 0
    current = slow
    while True:
        current = current.next
        count += 1
        if current == slow:
            break
    return count


def find_cycle_start(head):
    slow, fast = head, head
    cycle_length = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            cycle_length = calculate_cycle_num(slow)
            break
    
    return find_start(head,cycle_length)


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
