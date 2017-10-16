package com.coderli.leetcode.algorithms.medium;

/**
 * Given an integer, convert it to a roman numeral.
 * <p>
 * Input is guaranteed to be within the range from 1 to 3999
 *
 * @author li.hzh
 */
public class IntegerToRoman {

    public static void main(String[] args) {
        IntegerToRoman integerToRoman = new IntegerToRoman();
        System.out.println(integerToRoman.intToRoman(1));
        System.out.println(integerToRoman.intToRoman(10));
        System.out.println(integerToRoman.intToRoman(90));
        System.out.println(integerToRoman.intToRoman(1437));
    }

    public String intToRoman(int num) {
        int times = 1;
        String result = "";
        while (num > 0) {
            int tempIntValue = num % 10;
            num /= 10;
            String tempStrValue = "";
            if (tempIntValue == 5) {
                switch (times) {
                    case 1:
                        result = tempStrValue = "V";
                        break;
                    case 2:
                        result = "L" + result;
                        break;
                    case 3:
                        result = "D" + result;
                        break;
                }
            } else if (tempIntValue % 5 <= 3) {
                int length = tempIntValue;
                switch (times) {
                    case 1:
                        if (tempIntValue > 5) {
                            tempStrValue = "V";
                            length = tempIntValue - 5;
                        }
                        for (int i = 0; i < length; i++) {
                            tempStrValue += "I";
                        }
                        result = tempStrValue + result;
                        break;
                    case 2:
                        if (tempIntValue > 5) {
                            tempStrValue = "L";
                            length = tempIntValue - 5;
                        }
                        for (int i = 0; i < length; i++) {
                            tempStrValue += "X";
                        }
                        result = tempStrValue + result;
                        break;
                    case 3:
                        if (tempIntValue > 5) {
                            tempStrValue = "D";
                            length = tempIntValue - 5;
                        }
                        for (int i = 0; i < length; i++) {
                            tempStrValue += "C";
                        }
                        result = tempStrValue + result;
                        break;
                    case 4:
                        for (int i = 0; i < tempIntValue; i++) {
                            tempStrValue += "M";
                        }
                        result = tempStrValue + result;
                        break;
                }
            } else {
                switch (times) {
                    case 1:
                        result = tempIntValue < 5 ? "IV" + result : "IX" + result;
                        break;
                    case 2:
                        result = tempIntValue < 5 ? "XL" + result : "XC" + result;
                        break;
                    case 3:
                        result = tempIntValue < 5 ? "CD" + result : "CM" + result;
                        break;
                }
            }
            times++;
        }
        return result;
    }

}
