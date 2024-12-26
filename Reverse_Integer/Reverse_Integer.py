class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False

        if x < 0:
            isNegative = True
            x = abs(x)

        # Convert digits to a list
        digits = [int(d) for d in str(x)] 

        # Reverse the digits
        reversed_number = int(''.join([str(d) for d in digits[::-1]]))

        # Add back the sign if the original number was negative
        if isNegative:
            reversed_number = -reversed_number

        # Check if reversed_number fits in a 32-bit signed integer range
        if -(2**31) <= reversed_number < 2**31:
            return reversed_number
        else:
            return 0
