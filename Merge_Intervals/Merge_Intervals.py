class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # intervals where intervals[i] = [starti, endi]
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            # if mmerged is empty, or the end of the previous interval is less than the start of the current interval
            # append the current interval to the merged list
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise if the current interval does overlap with the previous,
                # we merge the current and previous intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
    
# Test
s = Solution()
print(s.merge([[1,4],[4,5]]))  # [[1, 5]]
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))  # [[1, 6], [8, 10], [15, 18]]