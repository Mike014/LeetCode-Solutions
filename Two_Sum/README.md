
# Two Sum Problem - Solution

## Problem Description

Given an array of integers `nums` and an integer `target`, you need to find two numbers in the array that add up to the `target` and return their indices. It is assumed that each input will have exactly one solution, and you cannot use the same element twice.

### Examples:
1. **Input:** `nums = [2, 7, 11, 15]`, `target = 9`
   - **Output:** `[0, 1]`
   - **Explanation:** The sum of `nums[0]` (2) and `nums[1]` (7) is equal to 9, so the solution is `[0, 1]`.

2. **Input:** `nums = [3, 2, 4]`, `target = 6`
   - **Output:** `[1, 2]`
   - **Explanation:** The sum of `nums[1]` (2) and `nums[2]` (4) is equal to 6, so the solution is `[1, 2]`.

3. **Input:** `nums = [3, 3]`, `target = 6`
   - **Output:** `[0, 1]`
   - **Explanation:** The sum of `nums[0]` (3) and `nums[1]` (3) is equal to 6, so the solution is `[0, 1]`.

## Solution

### Steps:
1. **Find the center of the array**:
   - If the array has an odd number of elements, calculate the center as `center_index = (n - 1) // 2`.
   - If the array has an even number of elements, take the two centers: `center_index1 = n // 2 - 1` and `center_index2 = n // 2`.

2. **Compare the central indices with the adjacent values**:
   - Compare the values at the centers with the adjacent values (left and right) to check if their sum is equal to `target`.

3. **Return the indices**:
   - If the sum of two numbers is equal to the `target`, return their indices.

## Complexity:
- **Time:** O(n^2), where `n` is the length of the array. We explore all possible pairs in the array to find the one that satisfies the sum `target`.
- **Space:** O(1), as we do not use significant additional memory besides the indices.


