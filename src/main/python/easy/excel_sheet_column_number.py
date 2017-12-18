# Related to question Excel Sheet Column Title
#
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28

# author li.hzh
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for val in s:
            result = result * 26 + ord(val) - 64
        return result


solution = Solution()
print(solution.titleToNumber("A"))
print(solution.titleToNumber("Z"))
print(solution.titleToNumber("BZ"))
print(solution.titleToNumber("ZZ"))
print(solution.titleToNumber("AAA"))