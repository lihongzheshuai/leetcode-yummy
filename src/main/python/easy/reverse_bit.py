# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
#
# Follow up:
# If this function is called many times, how would you optimize it?

# author li.hzh
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = str(bin(n))
        pad = (32 - len(res) + 2) * "0"
        # print res
        return int(res[0:2] + res[2:][::-1] + pad, 2)
        result = 0
        digits = 0
        while digits < 32:
            temp = n & 1
            result <<= 1
            result |= temp
            n >>= 1
            digits += 1
        return result

solution = Solution()
print(solution.reverseBits(43261596))