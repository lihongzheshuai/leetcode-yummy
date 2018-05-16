# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.
#
# Example 1:
#
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
#
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
#
# Input: s = "paper", t = "title"
# Output: true

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        temp_s_t_map = {}
        temp_t_s_map = {}
        for idx in range(len(s)):
            if temp_s_t_map.get(s[idx]) is None and temp_t_s_map.get(t[idx]) is None:
                temp_s_t_map[s[idx]] = t[idx]
                temp_t_s_map[t[idx]] = s[idx]
            elif temp_s_t_map.get(s[idx]) is not t[idx] or temp_t_s_map.get(t[idx]) is not s[idx]:
                return False
        return True


s = Solution()
print(s.isIsomorphic("egg","add"))
print(s.isIsomorphic("foo","bar"))
print(s.isIsomorphic("paper","title"))
print(s.isIsomorphic("ab","aa"))
zipped = zip("foo","bar")
print(set(zipped))
print(set("foo"))