package com.coderli.leetcode.algorithms;

/**
 * There are two sorted arrays nums1 and nums2 of size m and n respectively.<br />
 * Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
 *
 * @author li.hzh
 * @date 2015/9/6 10:42
 */
public class MedianOfTwoSortedArrays {

	public static void main(String[] args) {
		Solution solution = new MedianOfTwoSortedArrays().new Solution();
		int[] arrayOne = new int[]{1, 3, 4, 5, 6};
		int[] arrayTwo = new int[]{3, 4, 5, 6, 7, 8};
		System.out.println(solution.findMedianSortedArrays(arrayOne, arrayTwo));
	}


	public class Solution {

		public double findMedianSortedArrays(int[] nums1, int[] nums2) {
			int lengthOne = nums1.length;
			int lengthTwo = nums2.length;
			// 处理一个数组长度为0的边界情况
			if (lengthOne == 0) {
				if (lengthTwo % 2 == 1) {
					int midIndex = lengthTwo / 2;
					return nums2[midIndex];
				} else {
					int midOne = lengthTwo / 2 - 1;
					int midTwo = lengthTwo / 2;
					return (nums2[midOne] + nums2[midTwo]) / 2;
				}
			}
			if (lengthTwo == 0) {
				if (lengthOne % 2 == 1) {
					int midIndex = lengthOne / 2;
					return nums1[midIndex];
				} else {
					int midOne = lengthOne / 2 - 1;
					int midTwo = lengthOne / 2;
					return (nums1[midOne] + nums1[midTwo]) / 2;
				}
			}
			int totalLength = lengthOne + lengthTwo;


			return 0;
		}
	}
}
