# problem-solving

## Algorithm 정리

### Sliding window
> array가 주어졌을 때, continuous한 subarray에 관한 계산에 사용 가능
- window size = `end - start + 1`
- Maximum Sum Subarray of Size K
```
def max_sub_array_of_size_k(k, arr):
  start, max_sum = 0, 0
  window_sum = 0
  for end in range(len(arr)):
    window_sum += arr[end]
    if end >= k - 1:
      max_sum = max(max_sum, window_sum)
      window_sum -= arr[start]
      start += 1
  return max_sum
```
- Smallest Subarray with a given sum
```
def smallest_subarray_with_given_sum(s, arr):
  start = 0
  window_sum = 0
  min_len = len(arr) + 1
  for end in range(len(arr)):
    window_sum += arr[end]
    while window_sum >= s:
      window_len = end - start + 1
      min_len = min(min_len, window_len)
      window_sum -= arr[start]
      start += 1
  # edge case
  if min_len == len(arr) + 1:
    return 0
  return min_len
```
- Longest Substring with K Distinct Characters
```
def longest_substring_with_k_distinct(str1, k):
  alphabet_dict = {}
  max_len = 0
  start = 0

  for end in range(len(str1)):
    end_char = str1[end]
    if end_char not in alphabet_dict:
      alphabet_dict[end_char] = 0
    alphabet_dict[end_char] += 1

    while len(alphabet_dict) > k:
      start_char = str1[start]
      alphabet_dict[start_char] -= 1
      if alphabet_dict[start_char] == 0:
        del alphabet_dict[start_char]
      start += 1
    max_len = max(max_len, end-start + 1)
  return max_len
```
- Fruits into Baskets
```
def fruits_into_baskets(fruits):
  basket = {}
  start = 0
  max_len = 0

  for end in range(len(fruits)):
    fruit = fruits[end]
    if fruit not in basket:
      basket[fruit] = 0
    basket[fruit] += 1

    while len(basket) > 2:
      fruit = fruits[start]
      basket[fruit] -= 1
      if basket[fruit] == 0:
        del basket[fruit]
      start += 1
    max_len = max(max_len, end - start + 1)

  return max_len
```