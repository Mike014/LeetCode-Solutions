class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove any leading whitespace
        s = s.strip()
        i = 0
        # Check if the character to the the posistion s[i] is a sign (+ or -) or a number, then move to the next character
        while i < len(s) and (s[i].isdigit() or (i == 0 and s[i] in "+-")):
            i += 1
        # Extract the numeric part of the string
        numeric_part = s[:i]
        # Check if the numeric part is empty or if it's just a sign (+ or -)
        if not numeric_part or numeric_part in "+-":
            return 0
        # Convert the numeric part to an integer
        result = int(numeric_part)
        return result

# Testing with assert and printing the results
# tests = [
#     ("42", 42),
#     ("   -42", -42),
#     ("1337c0d3", 1337),
#     ("0-1", 0),
#     ("words and 987", 0),
# ]

# for test_input, expected_output in tests:
#     try:
#         assert Solution().myAtoi(test_input) == expected_output
#         print(f"Test passed for input '{test_input}' with output {expected_output}")
#     except AssertionError:
#         print(f"Test failed for input '{test_input}'")