"""
Problem Statement 
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to find the ordering of tasks we should pick to finish all tasks.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish 
before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2] 
Example 2:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: []
Explanation: The tasks have cyclic dependency, therefore they cannot be scheduled.
Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: [0 1 4 3 2 5] 
Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5] 
"""
from collections import deque

def find_order(tasks, prerequisites):
    sortedOrder = []
    adj_list = [[] for _ in range(tasks)]
    in_degree = {i:0 for i in range(tasks)}

    for task in prerequisites:
        pre_task, post_task = task[0], task[1]
        adj_list[pre_task].append(post_task)
        in_degree[post_task] += 1
    
    sources = deque()
    for task in in_degree:
        if in_degree[task] == 0:
            sources.append(task)
    
    while sources:
        current_task = sources.popleft()
        sortedOrder.append(current_task)
        for task in adj_list[current_task]:
            in_degree[task] -= 1
            if in_degree[task] == 0:
                sources.append(task)
    
    if len(sortedOrder) != tasks:
        return []
    return sortedOrder
def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()
