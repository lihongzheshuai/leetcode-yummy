package com.coderli.leetcode.algorithms.easy;

/**
 * Implement strStr().
 * <p>
 * Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
 *
 * @author li.hzh 2017-10-26 22:46
 */
public class ImplementStrStr {
    
    public static void main(String[] args) {
    
    }
    
    public int strStr(String haystack, String needle) {
        if (needle == null || haystack == null || needle.length() == 0) {
            return -1;
        }
        int needleIndex = 0;
        int result = -1;
        for (int i = 0; i < haystack.length(); i++) {
            if (needle.charAt(needleIndex) == haystack.charAt(i)) {
                needleIndex++;
                result = i;
            }
        }
        return result;
    }
}
