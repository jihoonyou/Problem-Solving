'''
Problem Statement
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.
Example 2:

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
'''
def merge(intervals_a, intervals_b):
  result = []
  a = 0
  b = 0
  start = 0
  end = 1
  while a < len(intervals_a) and b < len(intervals_b):
    interval_a = intervals_a[a]
    interval_b = intervals_b[b]

    a_overlaps_b = interval_a[end] >= interval_b[start] and interval_a[start] <= interval_b[end] 
    b_overlaps_a = interval_b[end] >= interval_a[start] and interval_b[start] <= interval_a[end]

    if a_overlaps_b or b_overlaps_a:
      result.append([max(interval_a[start],interval_b[start]), min(interval_a[end],interval_b[end])])

    if interval_a[end] > interval_b[end]:
      b += 1
    else:
      a += 1

  return result


def main():
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
