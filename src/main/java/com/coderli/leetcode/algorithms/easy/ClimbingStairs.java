package com.coderli.leetcode.algorithms.easy;

/**
 * ou are climbing a stair case. It takes n steps to reach to the top.
 * <p>
 * Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
 * <p>
 * Note: Given n will be a positive integer.
 * <p>
 * <p>
 * Example 1:
 * <p>
 * Input: 2
 * Output:  2
 * Explanation:  There are two ways to climb to the top.
 * <p>
 * 1. 1 step + 1 step
 * 2. 2 steps
 * Example 2:
 * <p>
 * Input: 3
 * Output:  3
 * Explanation:  There are three ways to climb to the top.
 * <p>
 * 1. 1 step + 1 step + 1 step
 * 2. 1 step + 2 steps
 * 3. 2 steps + 1 step
 *
 * @author OneCoder 2017-11-08 22:03
 */
public class ClimbingStairs {

    public static void main(String[] args) {
        String s = "a" + "b" + "c" + "d";
        ClimbingStairs climbingStairs = new ClimbingStairs();
        System.out.println(climbingStairs.climbStairsWithRecursion(3));
        System.out.println(climbingStairs.climbStairsWithRecursion(10));
        System.out.println(climbingStairs.climbStairsWithRecursion(44));
        System.out.println(climbingStairs.climbStairs(44));
    }

    public int climbStairsWithRecursion(int n) {
        if (n == 1) {
            return 1;
        } else if (n == 2) {
            return 2;
        } else {
            return climbStairsWithRecursion(n - 1) + climbStairsWithRecursion(n - 2);
        }
    }

    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        int prev = 1;
        int cur = 2;
        for (int i = 3; i <= n; i++) {
            int temp = cur;
            cur += prev;
            prev = temp;
        }
        return cur;
    }
}
