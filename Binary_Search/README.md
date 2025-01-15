# Principle of binary search
### Main requirement: The list must be ordered.

```python
list.sort()
```

### Start by looking at the item in the **middle of the list**.
```python
mid = (low + high) // 2  
# low = 0
# high = len(list) - 1
```
### This process continues until the value is found or the possibilities are exhausted.
### If the value you are looking for is smaller, the top half of the list is discarded.
### If the value is larger, the lower half is discarded.
```python
while low <= high:
    mid = (low + high) // 2 
    if nums[mid] < target:
        low = mid + 1
    elif nums[mid] > target:
        high = mid - 1 
    else:
        return mid
```




