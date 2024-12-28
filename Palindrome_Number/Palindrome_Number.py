class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x is negative, return False
        if x < 0:
            return False  
        # Initialize the original number and reversed number, original number is x itself, reversed number is 0
        # Reverse the number by using the while loop, and check if the reversed number is equal to the original number
        original_number = x
        reversed_number = 0

        # Checking if the number is within the 32-bit signed integer range, if not, return False, if it is, reverse the number
        if -2**31 <= x <= 2**31 - 1:
            while x != 0:
                # While x is not equal to 0, reverse the number 
                # by multiplying the reversed number by 10 and adding the remainder of x divided by 10
                reversed_number = reversed_number * 10 + x % 10
                x = x // 10

        # Return True if the reversed number is equal to the original number, otherwise return False
        return reversed_number == original_number

