# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.

#author li.hzh
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = len(nums) // 2
        if target == 0:
            return nums[0]
        map = {}
        for val in nums:
            if val in map:
                map[val] += 1
                if map[val] > target:
                    return val
            else:
                map[val] = 1

    def majorityElement_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]

print(Solution().majorityElement_sort([8,8,7,7,7]))