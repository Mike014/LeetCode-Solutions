# Palindrome Number Solution

This repository contains the solution for the problem [Palindrome Number](https://leetcode.com/problems/palindrome-number/description/) on LeetCode.

## Problem Description

The goal is to determine if a given integer `x` is a palindrome. A palindrome is a number that reads the same backward as forward.

### Example:

- Input: `121`  
  Output: `true`

- Input: `-121`  
  Output: `false`

- Input: `10`  
  Output: `false`


### Formula Used:
The essential formula for reversing the number is:
```python
reversed_number = reversed_number * 10 + (x % 10)
```

```plaintext
reversed_number = reversed_number * 10 + (x mod 10)
```

### Explanation 
For base 10, the modulo operation extracts the last digit of x. For example, in the case of 1257, the last digit is 7. Once the last digit is obtained, it is added to the value of reversed_number, which is multiplied by 10 to shift its digits to the left. This process continues, cycle by cycle, until the value of x is fully reduced to zero.

```plaintext
x = 1257
rev = 0
rev = rev * 10 + (x mod 10)
```

```plaintext
Start the cycle
1# 

x = 1257
x mod 10 = 7
rev = 0 * 10 + 7
x = 125

2#

x = 125 
x mod 10 = 5
rev = 7 * 10 + 5 = 75
x = 12

3# 

x = 12
x mod 10 = 2
rev = 75 * 10 + 2 = 752
x = 1

4#

x = 1
x mod 10 = 1
rev = 752 * 10 + 1 = 7521
x = 0
```
## Key Notes
Once the loop completes, the original number (x) is compared to the reversed number. Negative numbers CANNOT be palindromes, as their reversed representation would include a negative sign at the end, making it unequal to the original number.