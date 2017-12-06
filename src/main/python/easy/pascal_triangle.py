'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

# author li.hzh

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        last_row = [1]
        result = [last_row]
        for row in range(2, numRows + 1):
            cur_row = [last_row[0]]
            for i in range(1, len(last_row)):
                cur_row.append(last_row[i] + last_row[i - 1])
            cur_row.append(last_row[len(last_row) - 1])
            last_row = cur_row
            result.append(cur_row)
        return result

print(Solution().generate(5))