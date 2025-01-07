
# Target Sum Problem

## Problem Description
The task is to solve the **Target Sum Problem** as described on [LeetCode](https://leetcode.com/problems/target-sum/description/?utm_source=chatgpt.com).

Given an array of integers (`nums`) and a target value (`target`), the goal is to calculate the number of ways to assign a `+` or `-` sign to each element in the array such that the resulting expression equals the target.

---

## Approach

1. **Partial Sum Calculation**:
   - First, calculate the **total sum** of the array: `total_sum = sum(nums)`.
   - Next, compute the **partial sum** using the formula:
     \[
     	ext{partial_sum} = rac{	ext{total_sum} - 	ext{target}}{2}
     \]
   - The problem is valid only if:
     - \( 	ext{total_sum} \geq 	ext{target} \)
     - \( (	ext{total_sum} - 	ext{target}) \% 2 == 0 \)

2. **Dynamic Programming Table (DP)**:
   - Once the partial sum is determined, initialize a DP table of size \( 	ext{partial_sum} + 1 \).
   - The DP table represents the number of ways to achieve each sum up to \( 	ext{partial_sum} \) using elements from the array.

3. **Combination Calculation**:
   - For each number in the array, update the DP table to include combinations that use the current number.
   - The key is to divide the main array into two subarrays:
     - One subarray with **positive values**.
     - The other subarray with **negative values**.
   - The sum of these two subarrays must equal the target.

4. **Final Result**:
   - The value at \( dp[	ext{partial_sum}] \) gives the number of valid combinations to achieve the target.

---

## Summary
This approach utilizes the concept of dynamic programming to efficiently calculate the number of combinations by dividing the array into two subarrays with specific constraints. By iterating through the array and updating the DP table, the solution identifies all valid ways to achieve the target sum.

For more details, visit the [problem page](https://leetcode.com/problems/target-sum/description/?utm_source=chatgpt.com).