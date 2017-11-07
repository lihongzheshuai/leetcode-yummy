package com.coderli.leetcode.algorithms.easy;

import java.util.stream.IntStream;

/**
 * Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
 * <p>
 * You may assume the integer do not contain any leading zero, except the number 0 itself.
 * <p>
 * The digits are stored such that the most significant digit is at the head of the list.
 *
 * @author li.hzh 2017-11-07 12:48
 */
public class PlusOne {

    public static void main(String[] args) {
        PlusOne plusOne = new PlusOne();
        printArray(plusOne.plusOne(new int[]{9, 7, 6, 5}));
        printArray(plusOne.plusOne(new int[]{9, 9, 9, 9}));
    }

    private static void printArray(int[] ints) {
        IntStream.of(ints).forEach(System.out::print);
        System.out.println();
    }

    public int[] plusOne(int[] digits) {
        boolean needCarry = false;
        for (int i = digits.length - 1; i >= 0; i--) {
            int tempSum = digits[i] + 1;
            if (tempSum != 10) {
                digits[i] = tempSum;
                needCarry = false;
                break;
            } else {
                digits[i] = 0;
                needCarry = true;
            }
        }
        if (needCarry) {
            int[] result = new int[digits.length + 1];
            result[0] = 1;
            return result;
        }
        return digits;
    }
}
