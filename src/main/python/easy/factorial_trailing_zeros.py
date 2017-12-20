# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.

# author li.hzh
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n >= 5:
            result += n // 5
            n = n // 5
        return result


solution = Solution()
print(solution.trailingZeroes(102))
