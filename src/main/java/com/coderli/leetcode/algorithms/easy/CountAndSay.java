package com.coderli.leetcode.algorithms.easy;

/**
 * The count-and-say sequence is the sequence of integers with the first five terms as following:
 * <p>
 * 1.     1 <br>
 * 2.     11<br>
 * 3.     21<br>
 * 4.     1211<br>
 * 5.     111221<br>
 * 1 is read off as "one 1" or 11.<br>
 * 11 is read off as "two 1s" or 21.<br>
 * 21 is read off as "one 2, then one 1" or 1211.<br>
 * Given an integer n, generate the nth term of the count-and-say sequence.
 * <p>
 * Note: Each term of the sequence of integers will be represented as a string.
 * <p>
 * Example 1:
 * <p>
 * Input: 1
 * Output: "1"
 * <p>
 * Example 2:
 * <p>
 * Input: 4
 * Output: "1211"
 *
 * @author li.hzh 2017-10-30 13:06
 */
public class CountAndSay {

    public static void main(String[] args) {
        System.out.println(new CountAndSay().countAndSay(1));
        System.out.println(new CountAndSay().countAndSay(2));
        System.out.println(new CountAndSay().countAndSay(3));
        System.out.println(new CountAndSay().countAndSay(4));
        System.out.println(new CountAndSay().countAndSay(5));

    }

    public String countAndSay(int n) {
        String result = "1";
        for (int i = 1; i < n; i++) {
            StringBuilder builder = new StringBuilder();
            char pre = result.charAt(0);
            int count = 0;
            for (int k = 0; k < result.length(); k++) {
                if (result.charAt(k) == pre) {
                    count++;
                } else {
                    builder.append(count);
                    builder.append(pre);
                    count = 1;
                    pre = result.charAt(k);
                }
            }
            builder.append(count);
            builder.append(pre);
            result = builder.toString();
        }
        return result;
    }
}
