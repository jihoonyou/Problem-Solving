"""
Problem Statement
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""
def length_of_longest_substring(str, k):
  window_start = 0
  max_length = 0
  alphabet_dict = {}
  max_repeat_letter_count = 0
  
  for window_end in range(len(str)):
    if str[window_end] not in alphabet_dict:
      alphabet_dict[str[window_end]] = 1
    else:
      alphabet_dict[str[window_end]] += 1
    max_repeat_letter_count = max(max_repeat_letter_count,alphabet_dict[str[window_end]])

    if window_end - window_start + 1 - max_repeat_letter_count > k:
      alphabet_dict[str[window_start]] -= 1
      window_start += 1
    max_length = max(max_length, window_end-window_start+1)
  return max_length

# end-start+1-maxCount == 0, then then the window is filled with only one character
