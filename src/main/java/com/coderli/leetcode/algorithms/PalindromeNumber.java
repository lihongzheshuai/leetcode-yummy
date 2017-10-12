package com.coderli.leetcode.algorithms;

/**
 * Determine whether an integer is a palindrome. Do this without extra space.
 *
 * @author li.hzh 2017-10-12
 */
public class PalindromeNumber {

    public static void main(String[] args) {
        PalindromeNumber palindromeNumber = new PalindromeNumber();
        System.out.println(palindromeNumber.isPalindrome(123));
        System.out.println(palindromeNumber.isPalindrome(12321));
        System.out.println(palindromeNumber.isPalindrome(10));
        System.out.println(palindromeNumber.isPalindrome(1));
        System.out.println(palindromeNumber.isPalindrome(11));
        System.out.println(palindromeNumber.isPalindrome(1221));
    }

    public boolean isPalindrome(int x) {
        if (x < 0 || (x != 0 && x % 10 == 0)) {
            return false;
        }
        int temp = 0;
        while (x > temp) {
            temp = temp * 10 + x % 10;
            x = x / 10;
        }
        return temp / 10 == x || temp == x;
    }

}
