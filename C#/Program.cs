﻿
namespace LeetCode
{
    public class Solution 
    {
        static void Main(string[] args)
        {
            //FindRomanToInt findRomanToInt = new FindRomanToInt();
            //Console.WriteLine( findRomanToInt.RomanToInt("III") );

            //FindIntToRoman findIntToRoman = new FindIntToRoman();
            //Console.WriteLine( findIntToRoman.IntToRoman(3) );

            //SortedArrSqrs sortedArrSqrs = new SortedArrSqrs();
            //int[] intArr = {-10000,-9999,-7,-5,0,0,10000};
            //sortedArrSqrs.SortedSquares( nums: intArr );

            ReverseStringClass reverseStringClass = new ReverseStringClass();
            char[] charArr = {'h','e','l','l','o'};
            reverseStringClass.ReverseStringSol(charArr);
            Console.WriteLine(charArr);

            //string testStr = "Let's take LeetCode contest";
            //ReverseWordsClass reverseWordsClass = new ReverseWordsClass();
            //reverseWordsClass.ReverseWords(testStr);
            //Console.WriteLine(testStr);


        }

    }
}