'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''


# author li.hzh

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for i in range(rowIndex):
            for index in range(len(result)):
                before = index - 1
                if before < 0:
                    continue
                elif index == 1:
                    result[index] = result[index] + result[before]
                else:
                    ori_val = 1
                    for i in range(1, index):
                        ori_val = result[i] - ori_val
                    result[index] += ori_val
            result.append(1)
        return result


print(Solution().getRow(0))
print(Solution().getRow(1))
print(Solution().getRow(2))
print(Solution().getRow(3))
print(Solution().getRow(4))
