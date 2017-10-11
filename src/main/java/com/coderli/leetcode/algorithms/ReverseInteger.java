package com.coderli.leetcode.algorithms;

/**
 * Reverse digits of an integer.
 * <p>
 * Example1: x = 123, return 321
 * Example2: x = -123, return -321
 *
 * @author li.hzh
 * @date 2017-10-11 22:07
 */
public class ReverseInteger {
    
    public static void main(String[] args) {
        int x = 123;
        int y = -321;
        int z = 1000000003;
        ReverseInteger instance = new ReverseInteger();
        System.out.println(instance.reverse(x));
        System.out.println(instance.reverse(y));
        System.out.println(instance.reverse(z));
    }
    
    public int reverse(int x) {
        int result = 0;
        int tempResult = 0;
        while (x != 0) {
            int remainder = x % 10;
            result = result * 10 + remainder;
            if ((result - remainder) / 10 != tempResult) {
                return 0;
            }
            tempResult = result;
            x = x / 10;
        }
        return result;
    }
    
}
