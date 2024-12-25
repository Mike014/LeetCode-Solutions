# Add Two Numbers

## Problem Description

This problem can be found on [LeetCode](https://leetcode.com/problems/add-two-numbers/description/).

You are given two **LinkedLists** representing two non-negative integers. Each digit is stored in a separate node, and the digits are stored in **reverse order**:
- The first node contains the ones place.
- The second node contains the tens place.
- And so on.

You need to compute the sum of these two numbers and return the result as a new **LinkedList**, also in reverse order.

---

## Example

### Input:
```plaintext
l1 = [2, 4, 3]  # Represents the number 342
l2 = [5, 6, 4]  # Represents the number 465
```

### Output:
```plaintext
[7, 0, 8]  # Represents the number 807 (342 + 465 = 807)
```

### Step-by-Step Explanation:
1. Add the digits in the ones place: `2 + 5 = 7` (no carry).
2. Add the digits in the tens place: `4 + 6 = 10` (carry = 1, resulting digit = 0).
3. Add the digits in the hundreds place: `3 + 4 + 1 (carry) = 8` (no carry).

The resulting LinkedList is `[7, 0, 8]`.

---

## Solution

### Process Steps

1. **Initialization**:
   - Create a dummy node (`dummy`) to simplify building the resulting LinkedList.
   - Use a variable `carry` to store the **carry-over** between sums.

2. **Traverse the LinkedLists**:
   - Use a `while` loop to iterate through `l1` and `l2`, continuing as long as there are nodes to process or a carry to handle.
   - For each node:
     - Add the values of the current nodes from `l1` and `l2` (if they exist) and add the `carry`.
     - Compute:
       - The current digit with `sum % 10`.
       - The new `carry` with `sum // 10`.

3. **Create the Result Node**:
   - Append a new node to the resulting LinkedList with the calculated digit (`sum % 10`).
   - Move the pointer to the next node to continue building.

4. **Handle Final Carry**:
   - If there is still a `carry` after processing both lists, add a new node with the carry value.

5. **Return the Result**:
   - The resulting LinkedList starts at `dummy.next`.

## Step-by-Step:
- Iteration 1:
```plaintext
l1.val = 2, l2.val = 5, carry = 0
sum = 2 + 5 + 0 = 7
Resulting Node: 7
carry = 0
```
- Iteration 2:
```plaintext
l1.val = 4, l2.val = 6, carry = 0
sum = 4 + 6 + 0 = 10
Resulting Node: 0
carry = 1
```
-  Iteration 3:
```plaintext
l1.val = 3, l2.val = 4, carry = 1
sum = 3 + 4 + 1 = 8
Resulting Node: 8
carry = 0
```