# Median of Two Sorted Arrays

This repository contains the solution for the problem [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) on LeetCode.

## Problem Description

The task is to return the median of two sorted arrays combined. The solution must achieve a time complexity of \( O(\log(m+n)) \).

---

## Explanation of the Algorithm

### Partitioning the Arrays
Given two arrays, where the first array must be shorter than the second, the goal is to return the combined median. To achieve this, we define two variables:
- `low`: Initialized to 0.
- `high`: Initialized to the length of the first array.

The key idea is to divide the two arrays into two partitions, treating them as a single combined array split into two halves.

---

### Steps
1. **Calculate Partitions:**
   - `partition1 = (low + high) // 2`
   - `partition2 = (len(nums1) + len(nums2) + 1) // 2 - partition1`

2. **Handling Partition Borders:**
   Using these rules:
   1. If the left partition is empty: use `-float('inf')`.
   2. If the right partition is empty: use `float('inf')`.
   3. If the partition is in the middle: use the actual array values.

   Example:
   ```python
   maxLeft1 = -float('inf') if partition1 == 0 else nums1[partition1 - 1]
   minRight1 = float('inf') if partition1 == len(nums1) else nums1[partition1]
   maxLeft2 = -float('inf') if partition2 == 0 else nums2[partition2 - 1]
   minRight2 = float('inf') if partition2 == len(nums2) else nums2[partition2]
   ```

3. **Check Partition Validity:**
   After managing the borders, check if the partition is valid:
   ```python
   if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
   ```

4. **Calculate the Median:**

   #### Formula for Calculating the Median:
   - **Array with an even number of elements:**
     The median is the average of the two central elements:
     ```python
     median = (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
     ```
   - **Array with an odd number of elements:**
     The median is the central value:
     ```python
     median = max(maxLeft1, maxLeft2)
     ```

   These formulas rely on the combined partitions dividing the arrays correctly.

5. **Adjust Low and High:**
   If the partitions are invalid:
   - If the right partition is invalid (`maxLeft1 > minRight2`), move left by reducing `high`.
   - Otherwise, move right by increasing `low`.

---

## Formula for Median in a Single Array

If the problem required calculating the median of a single sorted array:

1. **If the number of elements is even:**
   - Calculate the central index (`mid`):
     ```python
     mid = (low + high) // 2
     ```
   - The median is the average of the two middle elements:
     ```python
     median = (arr[mid] + arr[mid - 1]) / 2
     ```

2. **If the number of elements is odd:**
   - Calculate the central index (`mid`):
     ```python
     mid = (low + high) // 2
     ```
   - The median is the value of the central element:
     ```python
     median = arr[mid]
     ```

---

## Key Difference for This Problem

In the “Median of Two Sorted Arrays” problem, merging the arrays into a single sorted array would violate the time complexity requirement of \( O(\log(m+n)) \). Instead, the partitioning technique ensures that the median is found efficiently without explicitly merging the arrays.

# Other way to calculate the median
```python
arr = [1, 2, 3, 4, 5]  # Sorted Array

if len(arr) % 2 == 0:  # Check if the length of the array is even
    center_index = len(arr) // 2
    center_element = (arr[center_index] + arr[center_index - 1]) / 2  # Average of two middle elements
else:  # If the length of the array is odd
    center_index = len(arr) // 2
    center_element = arr[center_index]  # Single middle element

print("Center element:", center_element)
```




