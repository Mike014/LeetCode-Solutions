
# Problem: Top K Frequent Elements

## Problem Description

We solved the problem [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/) using Python's **collections** library and the `Counter` class.

### Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

### Example

**Input**: `nums = [1, 1, 1, 2, 2, 3], k = 2`  
**Output**: `[1, 2]`  

**Explanation**:  
- The frequency of `1` is 3, `2` is 2, and `3` is 1.  
- The `k = 2` most frequent elements are `1` and `2`.

---

## Solution Explanation

We solved the problem by following these steps:

1. **Finding Frequencies**:
   - We used the `Counter` class from the `collections` library to count the frequency of each element in the list.
   - This creates a dictionary-like structure where the keys are the elements and the values are their respective frequencies.
   - Example: Given `nums = [1, 1, 1, 2, 2, 3]`, the frequencies are:
     ```
     {1: 3, 2: 2, 3: 1}
     ```
     This means `1` appears 3 times, `2` appears 2 times, and `3` appears once.

2. **Sorting by Frequency**:
   - After finding the frequencies, we sorted the elements by their frequency in descending order:
     ```python
     sorted_elements = sorted(frequency.keys(), key=lambda x: frequency[x], reverse=True)
     ```
   - This ensures that the most frequent elements come first.

3. **Returning the Top K Elements**:
   - Finally, we extracted the top `k` elements using slicing:
     ```python
     return sorted_elements[:k]
     ```
   - Here, `k` is a parameter of the function and represents the number of most frequent elements to return.

---

## Special Case

- The value of `k` is in the range `[1, the number of unique elements in the array]`. Since `k` is a parameter, it must be passed to the function during execution and cannot be dynamically calculated inside the function.

---

## Complexity Analysis

- **Time Complexity**:  
  - Counting frequencies: \(O(n)\), where \(n\) is the size of the list `nums`.
  - Sorting: \(O(m \log m)\), where \(m\) is the number of unique elements.
  - Overall: \(O(n + m \log m)\).

- **Space Complexity**:  
  - \(O(n)\), for storing frequencies and sorted elements.

---

## Conclusion

The solution efficiently solves the problem by leveraging the `Counter` class to calculate frequencies and Python's built-in `sorted()` function for sorting. The top `k` elements are returned based on their frequency in descending order.
