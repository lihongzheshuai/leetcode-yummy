package com.coderli.leetcode.algorithms.easy;

/**
 * Given a sorted array and a target value, return the index if the target is found.
 * If not, return the index where it would be if it were inserted in order.
 * <p>
 * You may assume no duplicates in the array.
 * <p>
 * Here are few examples.
 * [1,3,5,6], 5 → 2
 * [1,3,5,6], 2 → 1
 * [1,3,5,6], 7 → 4
 * [1,3,5,6], 0 → 0
 *
 * @author li.hzh 2017-10-29 21:58
 */
public class SearchInsertPosition {
    
    public static void main(String[] args) {
        SearchInsertPosition searchInsertPosition = new SearchInsertPosition();
        System.out.println(searchInsertPosition.searchInsert(new int[]{1, 3, 5, 6}, 5));
        System.out.println(searchInsertPosition.searchInsert(new int[]{1, 3, 5, 6}, 2));
        System.out.println(searchInsertPosition.searchInsert(new int[]{1, 3, 5, 6}, 7));
        System.out.println(searchInsertPosition.searchInsert(new int[]{1, 3, 5, 0}, 0));
    }
    
    public int searchInsert(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] >= target) {
                return i;
            }
        }
        return nums.length;
    }
    
    public int searchInsertByBinarySearch(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left < right - 1) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] < target) {
                left = mid;
            } else {
                right = mid;
            }
        }
        if (target <= nums[left]) {
            return left;
        }
        if (nums[right] >= target && nums[left] <= target) {
            return right;
        }
        return right + 1;
    }
    
}
