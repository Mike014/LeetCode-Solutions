# You are given an integer array `nums` and an integer `target`.
# The goal is to build an expression using the numbers in `nums` by adding either a '+' or '-' sign before each number
# such that the resulting expression evaluates to `target`.

nums = [3, 2, 4, 3, 2, 1]
target = 1 

# Step 1: Calculate the total sum of all elements in the array.
total_sum = sum(nums)
print(f"Total sum is {total_sum}")

# Step 2: Validate the problem
# The problem is valid only if:
# - The total sum is greater than or equal to the target.
# - The difference (total_sum - target) is divisible by 2.
if total_sum >= target and (total_sum - target) % 2 == 0:
    # Step 3: Calculate the partial sum
    # The partial sum represents the sum of the positive subset that we need to achieve.
    partial_sum = (total_sum - target) // 2
    print(f"Partial sum is {partial_sum}")

    # Step 4: Initialize the DP table
    # dp[j] represents the number of ways to achieve the sum `j` using the numbers in `nums`.
    dp = [0] * (partial_sum + 1)
    dp[0] = 1  # There's only one way to achieve sum 0: by using no numbers.

    # Step 5: Update the DP table
    # For each number in `nums`, update the DP table to include combinations that include the current number.
    for num in nums:
        for j in range(partial_sum, num - 1, -1):  # Iterate backwards to avoid overwriting results
            dp[j] += dp[j - num]

    # Step 6: The result is the number of ways to achieve the partial_sum
    print(f"Number of combinations: {dp[partial_sum]}")
else:
    # If the problem is invalid, output 0
    print(0)

# Time complexity: O(n * m), where `n` is the length of `nums` and `m` is the value of `partial_sum`.
# Space complexity: O(m), where `m` is the value of `partial_sum`.