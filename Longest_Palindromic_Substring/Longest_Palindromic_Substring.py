class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""

        for i in range(len(s)):
            # Odd-length palindromes
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(longest):
                    longest = s[left:right + 1]
                left -= 1
                right += 1

            # Even-length palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len(longest):
                    longest = s[left:right + 1]
                left -= 1
                right += 1

        return longest
    
# Test
if __name__ == "__main__":
    s = "even"
    sol = Solution()
    print(sol.longestPalindrome(s))