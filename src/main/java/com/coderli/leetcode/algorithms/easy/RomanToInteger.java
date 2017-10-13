package com.coderli.leetcode.algorithms.easy;

import java.util.HashMap;
import java.util.Map;

/**
 * Given a roman numeral, convert it to an integer.
 * <p>
 * Input is guaranteed to be within the range from 1 to 3999.
 *
 * @author li.hzh 2017-10-13 12:00
 */
public class RomanToInteger {

    public static void main(String[] args) {
        RomanToInteger romanToInteger = new RomanToInteger();
        System.out.println(romanToInteger.romanToInt("III"));
        System.out.println(romanToInteger.romanToInt("VI"));
        System.out.println(romanToInteger.romanToInt("XIX"));
        System.out.println(romanToInteger.romanToInt("MCDXXXVII"));
    }


    public int romanToInt(String s) {
        int pre = 0, result = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            int value = 0;
            switch (c) {
                case 'M':
                    value = 1000;
                    break;
                case 'D':
                    value = 500;
                    break;
                case 'C':
                    value = 100;
                    break;
                case 'L':
                    value = 50;
                    break;
                case 'X':
                    value = 10;
                    break;
                case 'V':
                    value = 5;
                    break;
                case 'I':
                    value = 1;
                    break;
            }
            if (pre == 0) {
                result = pre = value;
            } else {
                result = value >= pre ? result + value : result - value;
                pre = value;
            }
        }
        return result;
    }
}
