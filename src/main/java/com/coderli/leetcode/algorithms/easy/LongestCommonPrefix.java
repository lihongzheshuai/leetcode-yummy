package com.coderli.leetcode.algorithms.easy;

import java.util.Arrays;

/**
 * Write a function to find the longest common prefix string amongst an array of strings.
 *
 * @author li.hzh
 */
public class LongestCommonPrefix {

    public static void main(String[] args) {
        LongestCommonPrefix longestCommonPrefix = new LongestCommonPrefix();
        System.out.println(longestCommonPrefix.longestCommonPrefix(new String[]{"a"}));
        System.out.println(longestCommonPrefix.longestCommonPrefix(new String[]{"a", "ab", "abc"}));
        System.out.println(longestCommonPrefix.longestCommonPrefix(new String[]{"abc", "ab", "abc"}));
        System.out.println(longestCommonPrefix.longestCommonPrefix(new String[]{"abd", "ab", "abc"}));
        System.out.println(longestCommonPrefix.longestCommonPrefix(new String[]{"a", "b", "c"}));
    }

    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        if (strs.length == 1) {
            return strs[0];
        }
        String result = strs[0];
        for (int i = 1; i < strs.length; i++) {
            String currentStr = strs[i];
            int findLength = Math.min(result.length(), currentStr.length());
            int commonLength = 0;
            for (int j = 0; j < findLength; j++) {
                char charInResult = result.charAt(j);
                char charInCurrent = currentStr.charAt(j);
                if (charInResult == charInCurrent) {
                    commonLength++;
                } else {
                    break;
                }
            }
            result = result.substring(0,commonLength);
        }
        return result;
    }

    public String longestCommonPrefixBySortFirst(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        if (strs.length == 1) {
            return strs[0];
        }
        Arrays.sort(strs);
        String first = strs[0];
        String second = strs[strs.length - 1];
        String result = first;
        int commonLength = 0;
        for (int j = 0; j < first.length(); j++) {
            char charInFirst = result.charAt(j);
            char charInSecond = second.charAt(j);
            if (charInFirst == charInSecond) {
                commonLength++;
            } else {
                break;
            }
        }
        result = result.substring(0,commonLength);
        return result;
    }

}
