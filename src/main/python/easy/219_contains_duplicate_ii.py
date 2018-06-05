# Given an array of integers and an integer k, find out whether there are two distinct indices i and j
# in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
#
# Example 1:
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        temp_dict = {}
        for idx in range(len(nums)):
            if nums[idx] in temp_dict:
                if idx - temp_dict.get(nums[idx]) <= k:
                    return True
            temp_dict[nums[idx]] = idx
        return False

