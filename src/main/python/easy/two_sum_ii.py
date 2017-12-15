# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution and you may not use the same element twice.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

# author li.hzh
class Solution:

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        index = 1
        for val in numbers:
            other = target - val
            if other in map:
                return [map.get(other), index]
            map[val] = index
            index += 1

    def twoSum_without_extra_space(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        head, tail = 0, -1
        cur_sum = numbers[head] + numbers[tail]
        while cur_sum != target:
            if cur_sum < target:
                head += 1
            else:
                tail -= 1
            cur_sum = numbers[head] + numbers[tail]
        return [head + 1, len(numbers) + tail + 1]

