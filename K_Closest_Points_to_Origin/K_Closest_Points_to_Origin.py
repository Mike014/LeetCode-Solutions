import heapq
import math

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        if not (1 <= k <= len(points) <= 104):
            raise ValueError("k and the number of points must satisfy 1 <= k <= len(points) <= 104")
        
        for x, y in points:
            if not (-104 <= x <= 104 and -104 <= y <= 104):
                raise ValueError("Each coordinate must satisfy -104 <= xi, yi <= 104")

        min_heap = []

        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(min_heap, (dist, [x, y]))

        return [heapq.heappop(min_heap)[1] for _ in range(k)]
    
points = [[3,3],[5,-1],[-2,4]]
k = 2
output = Solution()
print(output.kClosest(points, k))

# The solution is to find the k closest points to the origin. For example, if k is two, then we need to find the two closest points to the origin.
# Using Heaps in this case, a tree data structure, Heaps are a complete binary tree data structure used to maintain the order of elements based on priority.
# Since we are looking for the closest points to the origin, we use the heapq.heappush function to insert the points into the heap based on their distance from the origin.
# The distance is calculated using the Euclidean distance formula sqrt(x^2 + y^2). Once all the points have been inserted into the heap,
# we use heapq.heappop to extract the k points with the minimum distance. This allows us to efficiently obtain the k closest points to the origin.
