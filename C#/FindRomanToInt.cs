namespace LeetCode
{
    public class FindRomanToInt
    {
        const int iVal = 1;
        const int vVal = 5;
        const int xVal = 10;
        const int lVal = 50;
        const int cVal = 100;
        const int dVal = 500;
        const int mVal = 1000;

        public int RomanToInt(string s) 
        {
            int sum = 0;

            for( int i = 0; i < s.Length; i++ )
            {
                //if not first letter
                if( i != 0)
                {
                    //pass in last char as prev char
                    sum += convertToInt( lastChar: s[i-1], numeral: s[i] );
                }
            else
            {
                    //pass in last char as curr char
                    sum += convertToInt(  numeral: s[i], firstChar: true );
            }
            }

            return sum;
        }

        private int convertToInt( char numeral, char lastChar = '0', bool firstChar = false )
        {
            
            switch (numeral)
            {
            case 'I':
                return iVal;
            case 'V':
                if( lastChar == 'I' && !firstChar )
                {
                return vVal - 2 * iVal;
                }
                return vVal;
            case 'X':
                if( lastChar == 'I' && !firstChar  )
                {
                return xVal - 2 * iVal;
                }
                return xVal;
            case 'L':
                if( lastChar == 'X' && !firstChar  )
                {
                return lVal - 2 * xVal;
                }
                return lVal;
            case 'C':
                if( lastChar == 'X' && !firstChar  )
                {
                return cVal - 2 * xVal;
                }
                return cVal;
            case 'D':
                if( lastChar == 'C' && !firstChar  )
                {
                return dVal - 2 * cVal;
                }
                return dVal;
            case 'M':
                if( lastChar == 'C' && !firstChar  )
                {
                return mVal - 2 * cVal;
                }
                return mVal;
            default:
                return -1;
            } 
            
        }
    }
}
