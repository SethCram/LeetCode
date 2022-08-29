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

        public string IntToRoman(int num ) 
        {
            string currResult = "";

            //while any number left
            while(num > 0)
            {
                
                //if rslt greater than or equal to 0
                if( num - mVal >= 0 )
                {
                    //subtr m val
                    num -= mVal;

                    //append M to result str
                    currResult += 'M';
                }
                //if rslt greater than or equal to 0
                else if( num - (mVal - cVal) >= 0)
                {
                    //subtr number divisible by
                    num -= mVal - cVal;

                    //add chars
                    currResult += "CM";
                }
                else if( num - dVal >= 0 )
                {
                    //subtr val
                    num -= dVal;

                    //append letter to result str
                    currResult += 'D';
                }
                else if( num - (dVal - cVal) >= 0)
                {
                    //subtr number divisible by
                    num -= dVal - cVal;

                    //add chars
                    currResult += "CD";
                }
                //if number divisible by val
                else if( num - cVal >= 0 )
                {
                    //subtr val
                    num -= cVal;

                    //append letter to result str
                    currResult += 'C';
                }
                else if( num - (cVal - xVal) >= 0)
                {
                    //subtr number divisible by
                    num -= cVal - xVal;

                    //add chars
                    currResult += "XC";
                }
                //if number divisible by val
                else if( num - lVal >= 0 )
                {
                    //subtr val
                    num -= lVal;

                    //append letter to result str
                    currResult += 'L';
                }
                //if divisible by subtr rslt
                else if( num - (lVal - xVal) >= 0)
                {
                    //subtr number divisible by
                    num -= lVal - xVal;

                    //add chars
                    currResult += "XL";
                }
                //if number divisible by val
                else if( num - xVal >= 0 )
                {
                    //subtr val
                    num -= xVal;

                    //append letter to result str
                    currResult += 'X';
                }
                //if divisible by subtr rslt
                else if( num - (xVal - iVal) >= 0)
                {
                    //subtr number divisible by
                    num -= xVal - iVal;

                    //add chars
                    currResult += "IX";
                }
                //if number divisible by val
                else if( num - vVal >= 0 )
                {
                    //subtr val
                    num -= vVal;

                    //append letter to result str
                    currResult += 'V';
                }
                //if divisible by subtr rslt
                else if( num - (vVal - iVal) >= 0)
                {
                    //subtr number divisible by
                    num -= vVal - iVal;

                    //add chars
                    currResult += "IV";
                }
                //if number divisible by val
                else if( num - iVal >= 0 )
                {
                    //subtr val
                    num -= iVal;

                    //append letter to result str
                    currResult += 'I';
                }
            }
            

            return currResult;
        }


    }
}