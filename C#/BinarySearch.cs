namespace LeetCode
{
    //Unfinished
    public class BinarySearch
    {

        public int DirtySearch(int[] nums, int target) 
        {
            for( int i = 0; i < nums.Length; i++ )
            {
                //quick and dirty
                if( nums[i] == target )
                {
                    return i;
                }


            }

            return -1;
        }


        /*
        public int FailedQuickSearch(int[] nums, int target)
        {
            int halfwayIndex;
            int halfwayInt;
            int numsLength;
            
            while( nums != null )
            {
            numsLength = nums.Length;
            halfwayIndex = numsLength / 2;
            halfwayInt = nums[halfwayIndex];
            
            if( halfwayInt == target )
            {
                return halfwayIndex;
            }
            else if( halfwayInt > target )
            {
                //take lower half inclusive
                nums = nums[0:halfwayInt];
            }
            else if( halfwayInt < target )
            {
                //take upper half inclusive
                nums = nums[halfwayInt:numsLength];
            }
            
            }
        }
        */
    }
}