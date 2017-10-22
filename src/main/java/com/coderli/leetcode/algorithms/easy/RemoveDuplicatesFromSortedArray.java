package com.coderli.leetcode.algorithms.easy;

/**
 * Given a sorted array, remove the duplicates in place such that each element appear only once and
 * return the new length.
 * <p>
 * Do not allocate extra space for another array, you must do this in place with constant memory.
 * <p>
 * For example,
 * Given input array nums = [1,1,2],
 * <p>
 * Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
 * It doesn't matter what you leave beyond the new length.
 *
 * @author li.hzh 2017-10-22 21:24
 */
public class RemoveDuplicatesFromSortedArray {
    
    public static void main(String[] args) {
        RemoveDuplicatesFromSortedArray rdfSortedArray = new RemoveDuplicatesFromSortedArray();
        System.out.println(rdfSortedArray.removeDuplicates(new int[]{1}));
        System.out.println(rdfSortedArray.removeDuplicates(new int[]{1, 1}));
        System.out.println(rdfSortedArray.removeDuplicates(new int[]{1, 1, 2}));
        System.out.println(rdfSortedArray.removeDuplicates(new int[]{1, 1, 2, 2}));
        System.out.println(rdfSortedArray.removeDuplicates(new int[]{1, 1, 1, 2, 2}));
        System.out.println(rdfSortedArray.removeDuplicates(new int[]{1, 1, 2, 2, 3, 3}));
        System.out.println(rdfSortedArray.removeDuplicates(new int[]{1, 2, 2, 3, 4, 4}));
    }
    
    public int removeDuplicates(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int compareValue = nums[0];
        int result = 1;
        for (int i = 1; i < nums.length; i++) {
            if (compareValue < nums[i]){
                compareValue = nums[i];
                nums[result] = compareValue;
                result++;
            }
        }
        return result;
    }
    
}
