"""
Problem Statement
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish 
before '2' can be scheduled. A possible sceduling of tasks is: [0, 1, 2] 
Example 2:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: false
Explanation: The tasks have cyclic dependency, therefore they cannot be sceduled.
Example 3:

Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: true
Explanation: A possible sceduling of tasks is: [0 1 4 3 2 5] 
"""
from collections import deque
def is_scheduling_possible(tasks, prerequisites):
    schedule = []
    adj_list = [[] for _ in range(tasks)]
    in_degree_count = {i: 0 for i in range(tasks)}

    for courses in prerequisites:
        pre_course, post_course = courses[0], courses[1]
        adj_list[pre_course].append(post_course)
        in_degree_count[post_course] += 1
    
    source = deque()
    for course in in_degree_count:
        if in_degree_count[course] == 0:
            source.append(course)

    while source:
        subject = source.popleft()
        schedule.append(subject)
        for post_course in adj_list[subject]:
            in_degree_count[post_course] -= 1
            if in_degree_count[post_course] == 0:
                source.append(post_course)
    return len(schedule) == tasks


def main():
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(4, [[0, 1], [1, 2], [2, 0], [3,2]])))

main()
