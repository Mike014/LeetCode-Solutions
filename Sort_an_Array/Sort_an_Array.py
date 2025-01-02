class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Calculate the length of the list manually
        length = 0
        for i in nums:
            length += 1

        # Base case: If the list has one or no elements, it's already sorted
        if length <= 1:
            return nums
        
        # Ensure the constraints are met
        if (1 <= length <= 5 * 10**4) and all(-5 * 10**4 <= i <= 5 * 10**4 for i in nums):
            # Select the pivot (e.g., first element of the list)
            pivot = nums[0]

            # Partition the list into 'less' and 'greater'
            # 'less' contains elements smaller than or equal to the pivot
            less = [x for x in nums[1:] if x <= pivot]
            # 'greater' contains elements larger than the pivot
            greater = [x for x in nums[1:] if x > pivot]

        # Recursively sort 'less' and 'greater', then combine with the pivot
        return self.sortArray(less) + [pivot] + self.sortArray(greater)

# Example usage
solution = Solution()
print(solution.sortArray([5, 2, 3, 1, 4]))  # Output: [1, 2, 3, 4, 5]

# Time complexity: O(n log n)
# LeetCode: 912. Sort an Array - Medium https://leetcode.com/problems/sort-an-array/submissions/1495242416/

# Tim Sort algorithm
# arr = [4, 2, 8, 6, 1, 5, 9, 3, 7]

# runs = []  # Lista per memorizzare le run
# current_run = []  # Lista temporanea per una run

# for i in range(len(arr) - 1):  # Fino al penultimo elemento
#     current_run.append(arr[i])  # Aggiungi l'elemento alla run

#     # Se l'elemento successivo è minore del corrente, la run finisce
#     if arr[i] > arr[i + 1]:
#         runs.append(current_run)  # Aggiungi la run alla lista delle runs
#         current_run = []  # Resetta la run temporanea per la prossima

# # Aggiungi l'ultimo elemento alla lista
# current_run.append(arr[-1])
# runs.append(current_run)

# # Risultato finale
# print("Runs:", runs)