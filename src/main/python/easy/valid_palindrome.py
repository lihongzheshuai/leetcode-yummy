'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''

# author li.hzh

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        front_index, end_index = 0, len(s) - 1
        while front_index < end_index:
            if not s[front_index].isalnum():
                front_index += 1
                continue
            if not s[end_index].isalnum():
                end_index -= 1
                continue
            if s[front_index].lower() != s[end_index].lower():
                return False
            else:
                front_index += 1
                end_index -= 1
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))