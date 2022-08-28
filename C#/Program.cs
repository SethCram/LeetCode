
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

            SortedArrSqrs sortedArrSqrs = new SortedArrSqrs();
            int[] intArr = {-4,-1,0,3,10};
            sortedArrSqrs.SortedSquares( nums: intArr );
        }

    }
}