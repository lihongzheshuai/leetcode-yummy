package com.coderli.leetcode.algorithms.easy;

/**
 * Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
 * <p>
 * For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
 * the contiguous subarray [4,-1,2,1] has the largest sum = 6.
 *
 * @author OneCoder 2017-10-31 23:41
 */
public class MaximumSubarray {

    public static void main(String[] args) {
        MaximumSubarray maximumSubarray = new MaximumSubarray();
        System.out.println(maximumSubarray.maxSubArray(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}));
        System.out.println(maximumSubarray.maxSubArray(new int[]{-2, -1}));
        System.out.println(maximumSubarray.maxSubArray(new int[]{1, -3, 2}));
        System.out.println(maximumSubarray.maxSubArray(new int[]{1, -1, -2, 2}));
    }

    public int maxSubArray(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int maxResult = nums[0];
        int tempSum = maxResult;
        for (int i = 1; i < nums.length; i++) {
            tempSum = tempSum + nums[i];
            tempSum = Math.max(tempSum, nums[i]);
            maxResult = Math.max(tempSum, maxResult);

        }
        return maxResult;
    }

}
