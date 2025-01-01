from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Count the frequency of each element in the list
        frequency = Counter(nums)
        
        # Sort the elements by their frequency in descending order
        # reverse=True means that the elements are sorted in descending order
        # frequency.keys() provides the unique elements, and they are sorted
        # key=lambda x: frequency[x] example for each key 
        # if frequency = {'a': 3, 'b': 1, 'c': 2}, then 
        # x = 'a': frequency['a'] = 3
	    # x = 'b': frequency['b'] = 1
	    # x = 'c': frequency['c'] = 2
        # by their corresponding frequency values in descending order
        sorted_elements = sorted(frequency.keys(), key=lambda x: frequency[x], reverse=True)
        
        # Return the first k elements from the sorted list
        return sorted_elements[:k] 
    
# Time complexity: O(nlogn)
# Space complexity: O(n)
# n = number of elements in the list


# Other way to solve the problemfrom collections import Counter
        # c = Counter(nums)

        # res = [item[0] for item in c.most_common(k)]

        # return res

# Counter(nums) stores all the element with their frequency

# c.most_common(k) returns a list of the k most common elements, along with their frequencies, sorted in descending order of frequency.

# most_common returns a list of (element, frequency) pair, so item[0] return the element.