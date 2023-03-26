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


        
    }
}