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
        ImplementStrStr implementStrStr = new ImplementStrStr();
        System.out.println(implementStrStr.strStr("abba", "ba"));
        System.out.println(implementStrStr.strStrLikeString("mississipps", "issip"));
        System.out.println(implementStrStr.strStrLikeString("aaaaaaa", "aaaaab"));
    }
    
    /**
     * 模仿String里的indexOf的实现方式
     *
     * @param haystack
     * @param needle
     * @return
     */
    private int strStrLikeString(String haystack, String needle) {
        int targetLength = needle.length();
        int sourceLength = haystack.length();
        if (targetLength == 0) {
            return 0;
        }
        if (targetLength > sourceLength) {
            return -1;
        }
        for (int i = 0; i < sourceLength; i++) {
            if (haystack.charAt(i) != needle.charAt(0)) {
                while (++i < sourceLength && haystack.charAt(i) != needle.charAt(0)) ;
            }
            if (i + targetLength - 1 < sourceLength) {
                // 代表找到第一个可能元素
                int needleIndex = 1;
                for (int j = i + 1; needleIndex < targetLength &&
                                            needle.charAt(needleIndex) == haystack.charAt(j); needleIndex++, j++)
                    ;
                
                if (needleIndex == targetLength) {
                    return i;
                }
            }
        }
        return -1;
    }
    
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0) {
            return 0;
        }
        if (needle.length() > haystack.length()) {
            return -1;
        }
        int haystackIndex = 0;
        for (int i = 0; i < haystack.length(); i++) {
            if (needle.charAt(0) == haystack.charAt(i)) {
                haystackIndex = i;
                if (i + needle.length() > haystack.length()) {
                    return -1;
                }
                boolean found = true;
                for (int j = 1; j < needle.length(); j++) {
                    if (needle.charAt(j) != haystack.charAt(haystackIndex + j)) {
                        found = false;
                        break;
                    }
                }
                if (found) {
                    return haystackIndex;
                }
            }
        }
        return -1;
    }
}
