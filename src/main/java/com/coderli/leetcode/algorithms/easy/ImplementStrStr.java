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
        System.out.println(implementStrStr.strStr("abba","ba"));
        System.out.println(implementStrStr.strStr("mississipps","issip"));
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
