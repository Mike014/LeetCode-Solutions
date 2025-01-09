class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Check if the first array is smaller than the second array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        low = 0
        high = len(nums1)

        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (len(nums1) + len(nums2) + 1) // 2 - partition1

            # Check the edge cases
            # variabile = value1 if condition else value2
            # If the partition is empty (on the left): Use -float('inf').
            # If the partition is empty (on the right): Use float('inf').
            # If the partition is in the middle: Use the actual values of the arrays corresponding to the partition.
            maxLeft1 = -float('inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == len(nums1) else nums1[partition1]
            maxLeft2 = -float('inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == len(nums2) else nums2[partition2]

            # Check if we have found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Calculate the median
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                else:
                    return max(maxLeft1, maxLeft2)
            # If we are too far on the right, we need to go to the left
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            else:
                low = partition1 + 1

        # In any other case, we have an invalid input
        raise ValueError("Input arrays are not valid for median calculation.")


if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2])) # 2.0
    print(s.findMedianSortedArrays([1, 2], [3, 4])) # 2.5
    print(s.findMedianSortedArrays([1, 3, 5, 7], [4, 6, 8, 9])) # 5.5



