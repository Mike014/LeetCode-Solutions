class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        print(f"Current array: {nums}")  # Debug

        # Base case: If the array has one or no elements, it's already sorted
        if len(nums) <= 1:
            print(f"Base case reached with array: {nums}")  # Debug
            return nums

        # Select the pivot using the median-of-three strategy
        low = 0
        high = len(nums) - 1
        mid = len(nums) // 2

        first = nums[low]
        middle = nums[mid]
        last = nums[high]

        pivot_candidates = [first, middle, last]
        pivot_candidates.sort()

        pivot = pivot_candidates[1]  # Median of three
        print(f"Selected pivot: {pivot}")  # Debug

        # In-place partitioning
        i = low
        k = high
        j = low

        print(f"Starting partitioning with pivot: {pivot}")  # Debug

        # The following block partitions the array into three sections:
        # 1. Elements less than the pivot are moved to the left (indices < i).
        # 2. Elements equal to the pivot remain in the middle (between i and k).
        # 3. Elements greater than the pivot are moved to the right (indices > k).
        # This ensures all elements are rearranged in a single traversal of the array.
        while j <= k:
            if nums[j] < pivot:  # Element is less than the pivot
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > pivot:  # Element is greater than the pivot
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:  # Element is equal to the pivot
                j += 1
            print(f"Partitioning step: {nums}, i: {i}, j: {j}, k: {k}")

        # Recursively sort the left and right sections
        print(f"Sorting left part: {nums[low:i]}")  # Debug
        left_sorted = self.sortArray(nums[low:i])  # Elements < pivot

        print(f"Sorting right part: {nums[k+1:high+1]}")  # Debug
        right_sorted = self.sortArray(nums[k+1:high+1])  # Elements > pivot

        # Combine the results
        sorted_array = left_sorted + nums[i:k+1] + right_sorted  # Includes elements equal to pivot
        print(f"Combined result: {sorted_array}")  # Debug
        return sorted_array

# Test cases
solution = Solution()
print("Final sorted array:", solution.sortArray([5, 2, 3, 1]))  # Output: [1, 2, 3, 5]
# print("Final sorted array:", solution.sortArray([3, 2, 3, 5]))  # Output: [2, 3, 3, 5]

# Time complexity: O(n log n)
# LeetCode: 912. Sort an Array - Medium https://leetcode.com/problems/sort-an-array/submissions/1495242416/

# divide-et-impera approach
# class Solution(object):
#     def sortArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """

#         if len(nums) == 1:
#             return nums
#         mid = len(nums)//2
#         L = nums[:mid]
#         R = nums[mid:]

#         self.sortArray(L)
#         self.sortArray(R)

#         i = j = k = 0
        
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 nums[k] = L[i]
#                 i+=1
#             else:
#                 nums[k] = R[j]
#                 j+=1
#             k+=1
        
#         while i<len(L):
#             nums[k] = L[i]
#             i+=1
#             k+=1
#         while j<len(R):
#             nums[k] = R[j]
#             j+=1
#             k+=1

#         return nums