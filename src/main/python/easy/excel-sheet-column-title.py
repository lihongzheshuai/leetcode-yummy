# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB

# author li.hzh
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        remainder, result = 0, ""
        while n > 26:
            remainder = (n - 1) % 26
            n = (n - 1) // 26
            result = (chr(65 + remainder)) + result
        result = (chr(64 + n)) + result
        return result


solution = Solution()
print(solution.convertToTitle(1))
print(solution.convertToTitle(26))
print(solution.convertToTitle(27))
print(solution.convertToTitle(30))
print(solution.convertToTitle(52))
print(solution.convertToTitle(53))
print(solution.convertToTitle(54))
print(solution.convertToTitle(676))
print(solution.convertToTitle(677))
print(solution.convertToTitle(702))
print(solution.convertToTitle(703))
print(solution.convertToTitle(728))
