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
        System.out.println(maximumSubarray.maxSubArrayByDC(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}));
        System.out.println(maximumSubarray.maxSubArrayByDC(new int[]{-2, -1}));
        System.out.println(maximumSubarray.maxSubArrayByDC(new int[]{1, -3, 2}));
        System.out.println(maximumSubarray.maxSubArrayByDC(new int[]{1, -1, -2, 2}));
    }

    public int maxSubArray(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int maxResult = nums[0];
        int tempSum = maxResult;
        for (int i = 1; i < nums.length; i++) {
            if (tempSum <= 0) {
                tempSum = nums[i];
            } else {
                tempSum = tempSum + nums[i];
            }
            if (tempSum > maxResult) {
                maxResult = tempSum;
            }
        }
        return maxResult;
    }

    public int maxSubArrayByDC(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        return findMaxSubArray(nums, 0, nums.length - 1);

    }

    private int findMaxSubArray(int[] nums, int from, int to) {
        if (from == to) {
            return nums[from];
        }
        int mid = from + (to - from) / 2;
        int maxLeft = findMaxSubArray(nums, from, mid);
        int maxRight = findMaxSubArray(nums, mid + 1, to);
        int midMax = nums[mid];
        //TODO 包含mid的最大值处理

        

        if (maxLeft >= maxRight && maxLeft >= midMax) {
            return maxLeft;
        } else if (maxRight > midMax) {
            return maxRight;
        } else {
            return midMax;
        }
    }
}
