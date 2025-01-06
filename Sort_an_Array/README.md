
# Sorting Algorithm: QuickSort with Median-of-Three Partitioning

## Overview

This project implements a sorting algorithm based on the QuickSort paradigm. The algorithm sorts an array of integers in ascending order using an optimized approach with in-place partitioning and the "median-of-three" strategy for pivot selection.

---

## How It Works

1. **Pivot Selection (Median-of-Three)**:
    - The algorithm selects the pivot using the "median-of-three" strategy.
    - It considers the first, middle, and last elements of the array.
    - The median of these three values is chosen as the pivot.
    - This reduces the likelihood of unbalanced partitions.

2. **Partitioning**:
    - The array is divided into three segments:
        - Elements **less than the pivot** are moved to the left.
        - Elements **equal to the pivot** remain in the middle.
        - Elements **greater than the pivot** are moved to the right.
    - Partitioning is performed in-place to optimize space complexity.
    - The use of three pointers (`i`, `j`, and `k`) facilitates efficient partitioning:
        - `i`: Tracks the boundary of elements less than the pivot.
        - `j`: Iterates through the array.
        - `k`: Tracks the boundary of elements greater than the pivot.

3. **Recursive Sorting**:
    - The left and right segments are sorted recursively.
    - The results are combined to produce the final sorted array.

---

## Code Explanation

### Pivot Selection

```python
first = nums[low]
middle = nums[mid]
last = nums[high]

pivot_candidates = [first, middle, last]
pivot_candidates.sort()
pivot = pivot_candidates[1]  # Median of three
```

The pivot is selected as the median of the first, middle, and last elements.

---

### Partitioning Logic

```python
while j <= k:
    if nums[j] < pivot:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j += 1
    elif nums[j] > pivot:
        nums[j], nums[k] = nums[k], nums[j]
        k -= 1
    else:
        j += 1
```

The partitioning ensures:
- Elements less than the pivot are placed before index `i`.
- Elements greater than the pivot are placed after index `k`.

---

### Combining Results

```python
sorted_array = left_sorted + nums[i:k+1] + right_sorted
```

The final sorted array includes:
- Recursively sorted left segment.
- Elements equal to the pivot.
- Recursively sorted right segment.

---

## Complexity

- **Time Complexity**: `O(n log n)` on average. The use of the median-of-three pivot selection helps maintain balanced partitions, minimizing the chance of worst-case scenarios (`O(n^2)`).
- **Space Complexity**: `O(log n)` due to recursive calls. The in-place partitioning reduces additional space requirements.

---

## Example Usage

```python
solution = Solution()
print(solution.sortArray([5, 2, 3, 1]))  # Output: [1, 2, 3, 5]
```

---

## Why We Used `k`

The variable `k` ensures that elements greater than the pivot are placed correctly at the end of the array during the partitioning process. This is critical for maintaining in-place partitioning without additional arrays.

---

## Constraints

- `1 <= nums.length <= 50,000`
- `-50,000 <= nums[i] <= 50,000`

This algorithm adheres to these constraints while meeting the requirements for time and space complexity.

---

