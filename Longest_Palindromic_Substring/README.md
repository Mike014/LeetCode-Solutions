# Longest Palindromic Substring Solution

This repository contains the solution to the [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/description/) problem from LeetCode. The problem involves finding the longest substring within a given string that reads the same forwards and backwards.

## Approach: Expand from the Center

The solution utilizes the **Expand from the Center** technique to identify palindromic substrings efficiently. Here's an explanation of the method:

### Technique Explanation

1. **Finding the Palindromic Centers**: 
    - Every palindromic substring has a center. 
    - For odd-length palindromes, the center is a single character (e.g., "aba" has the center at 'b').
    - For even-length palindromes, the center consists of two adjacent characters (e.g., "abba" has the center between the two 'b's).

2. **Using Two Pointers**:
    - We use two pointers, `left` and `right`, to expand outwards from the center.
    - Starting from the center, these pointers move one position to the left and right, respectively, and compare the characters they point to.
    - If the characters are equal, the substring is a palindrome, and we continue expanding.
    - If they are not equal, the expansion stops.

3. **Iterating Over All Possible Centers**:
    - For every character (and pair of adjacent characters) in the string, consider it as a potential center.
    - Expand outwards and track the longest palindromic substring found.

### Example Walkthrough

#### Input String: `Hello`

- The string has a length of 5 (odd), so its palindromic center can be any single character.
- Starting from the center 'l' (at index 2):
  - **First Expansion**: Compare characters at positions `left=1` ('e') and `right=3` ('o'). They are not equal, so stop expansion.
  - The palindrome at this center is "l".

- Expanding from all other centers yields no longer palindromes, so the result is "l".

#### Input String: `Java`

- The string has a length of 4 (even), so it has two-character centers as well.
- Starting from the center "av" (between indexes 1 and 2):
  - **First Expansion**: Compare characters at positions `left=0` ('J') and `right=3` ('a'). They are not equal, so stop expansion.
  - The palindrome at this center is "ava".
