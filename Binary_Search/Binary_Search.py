class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Optional: Sort the list 
        # nums.sort()  
        # print(nums)

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2  

            if nums[mid] < target:
                low = mid + 1  
            elif nums[mid] > target:
                high = mid - 1 
            else:
                return mid 
        return -1  
    

s = Solution()
print(s.search([4,5,6,7,0,1,2], 4))  
  
  












