package com.coderli.leetcode.algorithms.easy;

/**
 * Implement int sqrt(int x).
 * <p>
 * Compute and return the square root of x.
 * <p>
 * x is guaranteed to be a non-negative integer.
 * <p>
 * <p>
 * Example 1:
 * <p>
 * Input: 4
 * Output: 2
 * <p>
 * <p>
 * Example 2:
 * <p>
 * Input: 8
 * Output: 2
 * Explanation: The square root of 8 is 2.82842..., and since we want to return an integer,
 * the decimal part will be truncated.
 *
 * @author li.hzh 2017-11-08 12:43
 */
public class SqrtX {

    public static void main(String[] args) {
        SqrtX sqrtX = new SqrtX();
        System.out.println(sqrtX.mySqrt(4));
        System.out.println(sqrtX.mySqrt(8));
        System.out.println(sqrtX.mySqrt(2));
        System.out.println(sqrtX.mySqrt(1));
        System.out.println(sqrtX.mySqrt(2147395599));
        System.out.println(sqrtX.mySqrt(2147483647));
    }


    public int mySqrt(int x) {
        if (x == 0) {
            return 0;
        }
        int left = 1;
        int right = x;
        int result = 0;
        for (int mid = left + ((right - left) >> 1); left <= right; mid = left + ((right - left) >> 1)) {
            int temp = x / mid;
            if (temp == mid) {
                return mid;
            } else if (temp > mid) {
                left = mid + 1;
                result = mid;
            } else {
                right = mid - 1;
            }
        }
        return result;
    }
}
