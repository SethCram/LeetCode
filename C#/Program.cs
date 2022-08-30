
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

            reverseStringClass.ReverseString(charArr);

            Console.WriteLine(charArr);
        }

    }
}