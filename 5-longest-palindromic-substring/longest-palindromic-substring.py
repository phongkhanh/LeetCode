class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]  # move return here

        result = ""
        for i in range(len(s)):
            sub1 = expand(i, i)     # Odd-length palindromes
            if len(sub1) > len(result):
                result = sub1
            sub2 = expand(i, i+1)   # Even-length palindromes
            if len(sub2) > len(result):
                result = sub2
        return result