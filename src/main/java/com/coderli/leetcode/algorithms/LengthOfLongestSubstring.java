package com.coderli.leetcode.algorithms;

/**
 * Given a string, find the length of the longest substring without repeating characters.
 * <p>For example, the longest substring without repeating letters for "abcabcbb" is "abc", <br/>
 * which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.</p>
 *
 * @author li.hzh
 * @date 2015-08-27 22:16
 */
public class LengthOfLongestSubstring {

	public static void main(String[] args) {
		Solution solution = new LengthOfLongestSubstring().new Solution();
		String inputOne = "abcabcbb";
		System.out.println(inputOne + ": " + solution.lengthOfLongestSubstring(inputOne));
		String inputTwo = "bbbbb";
		System.out.println(inputTwo + ": " + solution.lengthOfLongestSubstring(inputTwo));
		String inputThree = "abcaabcabbb";
		System.out.println(inputThree + ": " + solution.lengthOfLongestSubstring(inputThree	));
	}

	public class Solution {

		public int lengthOfLongestSubstring(String s) {
			char[] chars = s.toCharArray();
			for (int i = 0; i < chars.length; i++) {

			}
			return 0;
		}

	}


}
