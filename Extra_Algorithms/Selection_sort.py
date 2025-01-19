play_counts = [8, 9, 25, 77, 2, 3, 55, 88, 76, 341, 1653, -1]

new_list = []

while play_counts:
    max_value = max(play_counts)
    new_list.append(max_value)
    play_counts.remove(max_value)

print("New list:", new_list[::-1])  
print("Remaining list:", play_counts)

# Give an array, find tha max value and append it to a new list, then remove it from the original list.
# Repeat the process until the original list is empty.
# Return the new list in descending order and the original list.

# Second version using selection sort.
# The selection sort algorithm sorts an array by repeatedly finding the maximum element (considering ascending order) from unsorted part and putting it at the beginning.
# The algorithm maintains two subarrays in a given array.
# 1. The subarray which is already sorted.
# 2. Remaining subarray which is unsorted.
# In every iteration of selection sort, the maximum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

play_counts = [8, 9, 25, 77, 2, 3, 55, 88, 76, 341, 1653, -1]

for i in range(len(play_counts)):
    max_index = i
    for j in range(i + 1, len(play_counts)):
        if play_counts[j] < play_counts[max_index]:
            min_index = j
    play_counts[i], play_counts[max_index ] = play_counts[max_index], play_counts[i]

print("Second Remaining list:", play_counts)