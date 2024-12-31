
# Problem: Merge Intervals

## Problem Description

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

### Example 1:

**Input:** `[[1, 3], [2, 6], [8, 10], [15, 18]]`

**Output:** `[[1, 6], [8, 10], [15, 18]]`

**Explanation:**
- The first two intervals `[1, 3]` and `[2, 6]` overlap, so they are merged into `[1, 6]`.
- The intervals `[8, 10]` and `[15, 18]` do not overlap, so they remain unchanged.

### Example 2:

**Input:** `[[1, 4], [4, 5]]`

**Output:** `[[1, 5]]`

**Explanation:**
- The two intervals `[1, 4]` and `[4, 5]` overlap, so they are merged into `[1, 5]`.

## Solution Explanation

The solution to this problem involves checking whether two consecutive intervals in the sorted list overlap. If they do, we merge them into one interval that covers the entire range.

### Steps:
1. **Sort the intervals**: First, we sort the intervals by their starting value. This makes it easier to check whether two consecutive intervals overlap.
   
2. **Check for overlap**: Once the intervals are sorted, we iterate through the list and check if the end of the current interval is greater than or equal to the start of the next interval. If this condition is true, the intervals overlap and should be merged.
   
3. **Merge overlapping intervals**: If two intervals overlap, we update the end of the current interval to the maximum of the two intervals' end points. This ensures that we keep the full range covered by the merged interval.

4. **Return the merged intervals**: Once all the intervals have been processed, we return the list of non-overlapping intervals.

### Time Complexity:
- **O(n log n)**: Sorting the intervals takes O(n log n) time, where `n` is the number of intervals.
- **O(n)**: Merging the intervals takes O(n) time, as we only iterate through the list once.

### Space Complexity:
- **O(n)**: We use additional space to store the merged intervals.

## Conclusion

This solution effectively merges all overlapping intervals by sorting them first and then iterating through the list to check for overlaps. It runs efficiently with a time complexity of O(n log n) due to the sorting step, and handles all possible cases of overlapping intervals.
