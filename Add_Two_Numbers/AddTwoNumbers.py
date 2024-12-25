# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        carry = 0
        dummy = ListNode()
        current = dummy

        while l1 or l2 or carry: 
            sum = 0 
            if l1: 
                sum += l1.val 
                l1 = l1.next 
            if l2:
                sum += l2.val
                l2 = l2.next

            sum += carry
            carry = sum // 10
            sum = sum % 10

            current.next = ListNode(sum)
            current = current.next

        return dummy.next
    
# Test
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
sol = Solution()
result = sol.addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next




        