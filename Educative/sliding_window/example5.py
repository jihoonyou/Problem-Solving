"""
Problem Statement
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
"""
def non_repeat_substring(str):
    window_start = 0
    max_length = 0
    alphabet_dict = {}

    for window_end in range(len(str)):
        if str[window_end] not in alphabet_dict:
            alphabet_dict[str[window_end]] = 1
            max_length = max(max_length, window_end-window_start+1)
        else:
            alphabet_dict[str[window_end]] += 1
        while alphabet_dict[str[window_end]] != 1:
            alphabet_dict[str[window_start]] -= 1
            if alphabet_dict[str[window_start]] == 0:
                del alphabet_dict[str[window_start]]
            window_start += 1
    return max_length

"""
def non_repeat_substring(str1):
  window_start = 0
  max_length = 0
  char_index_map = {}

  # try to extend the range [windowStart, windowEnd]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    # if the map already contains the 'right_char', shrink the window from the beginning so that
    # we have only one occurrence of 'right_char'
    if right_char in char_index_map:
      # this is tricky; in the current window, we will not have any 'right_char' after its previous index
      # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
      window_start = max(window_start, char_index_map[right_char] + 1)
    # insert the 'right_char' into the map
    char_index_map[right_char] = window_end
    # remember the maximum length so far
    max_length = max(max_length, window_end - window_start + 1)
  return max_length
"""