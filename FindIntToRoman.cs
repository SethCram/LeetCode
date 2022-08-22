namespace LeetCode
{
    //Unfinished
    public class FindIntToRoman
    {
        const int iVal = 1;
        const int vVal = 5;
        const int xVal = 10;
        const int lVal = 50;
        const int cVal = 100;
        const int dVal = 500;
        const int mVal = 1000;

        public string IntToRoman(int num) 
        {
            //if number visible by val of M
            if( num % mVal == 0 )
            {
                num -= mVal;
                return "M";
            }

            return "-1";
        }
    }
}