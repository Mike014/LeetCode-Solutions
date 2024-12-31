class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # n is equal to the length of the list
        n = len(nums)
        # if n is odd, there is only one center index
        if n % 2 == 1:
            center_index = (n - 1) // 2
            # iterate through the list to find the two numbers that add up to the target
            for i in range(n):
                for j in range(i + 1, n):
                    if nums[i] + nums[j] == target:
                        return [i, j]
        else:
            # if n is even, there are two center indices
            center_index1 = n // 2 - 1
            center_index2 = n // 2 
            # iterate through the list to find the two numbers that add up to the target
            for i in range(n):
                for j in range(i + 1, n):
                    if nums[i] + nums[j] == target:
                        return [i, j]




        