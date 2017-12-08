# Given an array of integers, every element appears three times except for one, which appears exactly once.
# Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# author li.hzh

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for val in nums:
            result ^= val
        for val in nums:
            result ^= val

        return result


print(Solution().singleNumber([1, 1, 1, 3, 3, 5, 3, 6, 6, 6]))
