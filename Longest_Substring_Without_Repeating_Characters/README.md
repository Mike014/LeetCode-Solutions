# Longest Substring Without Repeating Characters

## Problem Description

This exercise is available on [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/).

Given a **string `s`**, find the length of the **longest substring** without repeating characters.

## Examples

### Example 1:
- **Input**: `s = "abcabcbb"`
- **Output**: `3`
- **Explanation**: The longest substring without repeating characters is `"abc"`, with a length of 3.

### Example 2:
- **Input**: `s = "bbbbb"`
- **Output**: `1`
- **Explanation**: The longest substring without repeating characters is `"b"`, with a length of 1.

### Example 3:
- **Input**: `s = "pwwkew"`
- **Output**: `3`
- **Explanation**: The longest substring without repeating characters is `"wke"`, with a length of 3.
  Note that `"pwke"` is a subsequence, not a substring.

## Solution: Sliding Window + Set

To solve this problem efficiently, I used the **Sliding Window** technique combined with a **set** to track unique characters in the current substring.

### **Sliding Window**
- A sliding window helps dynamically analyze substrings by moving two pointers:
  - **`start`**: Marks the beginning of the window.
  - **`end`**: Marks the end of the window.

- When a duplicate character is found, we **shrink the window** by moving the `start` pointer and removing characters from the set until the window becomes valid.

### **Set**
- A set is used to store characters in the current substring.
- It ensures quick lookups for duplicates and efficient removal of characters.



