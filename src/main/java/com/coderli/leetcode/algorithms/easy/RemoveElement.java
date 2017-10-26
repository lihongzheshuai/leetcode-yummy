package com.coderli.leetcode.algorithms.easy;

/**
 * Given an array and a value, remove all instances of that value in place and return the new length.
 * <p>
 * Do not allocate extra space for another array, you must do this in place with constant memory.
 * <p>
 * The order of elements can be changed. It doesn't matter what you leave beyond the new length.
 * <p>
 * Example:
 * Given input array nums = [3,2,2,3], val = 3
 * <p>
 * Your function should return length = 2, with the first two elements of nums being 2.
 *
 * @author 2017-10-26
 */
public class RemoveElement {

    public static void main(String[] args) {
        RemoveElement removeElement = new RemoveElement();
        System.out.println(removeElement.removeElement(new int[]{}, 3));
        System.out.println(removeElement.removeElement(new int[]{2, 3, 3, 2}, 3));
        System.out.println(removeElement.removeElementByAddCount(new int[]{2, 3, 3, 2, 4, 1}, 3));
    }

    public int removeElement(int[] nums, int val) {
        int result = nums.length;
        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] == val) {
                result--;
                int temp = nums[result];
                nums[result] = val;
                nums[i] = temp;
            }
        }
        return result;
    }

    public int removeElementByAddCount(int[] nums, int val) {
        int result = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[result++] = nums[i];
            }
        }
        return result;
    }
}
