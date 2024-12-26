# Reverse Integer Solution

## Problem Overview
The problem asks us to reverse the digits of a given 32-bit signed integer. If the reversed integer exceeds the 32-bit signed integer range `[-2^31, 2^31 - 1]`, the function should return `0`. 

You can find the full problem description here:  
[Reverse Integer on LeetCode](https://leetcode.com/problems/reverse-integer/description/)

## Solution Explanation

This solution uses a combination of mathematical operations and list manipulation to reverse the integer. Here's a step-by-step explanation:

1. **Convert the Number to Positive (if Negative):**
   - A flag variable `isNegative` is set to `True` if the input integer `x` is negative.
   - If `x` is negative, its absolute value is computed using `abs(x)`.

2. **Convert Digits to a List:**
   - Convert the integer `x` into a string and then break it into a list of digits using a list comprehension:  
     ```python
     digits = [int(d) for d in str(x)]
     ```

3. **Reverse the List of Digits:**
   - Use slicing with `[::-1]` to reverse the order of the digits:
     ```python
     reversed_digits = digits[::-1]
     ```

4. **Construct the Reversed Integer:**
   - Convert the reversed digits back into a single integer:
     ```python
     reversed_number = int(''.join([str(d) for d in reversed_digits]))
     ```

5. **Reapply the Negative Sign (if Necessary):**
   - If the original number was negative, reapply the negative sign:
     ```python
     if isNegative:
         reversed_number = -reversed_number
     ```

6. **Check for 32-bit Integer Range:**
   - Before returning the result, check if the reversed number is within the 32-bit signed integer range:
     ```python
     if -(2**31) <= reversed_number < 2**31:
         return reversed_number
     else:
         return 0
     ```

## Key Points
	•	This solution effectively handles negative numbers by converting them to positive, reversing the digits, and reapplying the negative sign.
	•	The check -(2**31) <= reversed_number < 2**31 ensures the reversed integer fits within the 32-bit signed integer range.
	•	List slicing [::-1] provides an efficient way to reverse the digits.

