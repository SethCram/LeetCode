namespace LeetCode
{
    using System;

    public class SortedArrSqrs
    {
        /*
            Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
             Non-decreasing so subsequent numbers can be the same

            Approach: Store negative converted to positive numbers in a list, then compare the last one to the next value of the passed in array.
                Whichever value is smaller is squared, placed into the squared array, and its structure index incr'd.
        */
        public int[] SortedSquares(int[] nums) 
        {
            //cache arr size
            int incomingArrLen = nums.Length;

            //declare new arr of same size as incoming one
            int[] sqrdArr = new int[incomingArrLen];

            //declare a new lists
            List<int> negativeList = new List<int>();

            int currNumber;
            int sqrdArrIndex = 0;
            int negativeListIndex = 0;
            int negativeListCurrNumber;
            int numsIndex = 0;

            bool negativeListUseable = false;
            bool numsArrUseable = false;

            int negativeListCount;

            //if highest # is zero or negative
            if(nums[incomingArrLen-1] <= 0)
            {
                //walk thru incoming arr that's in non-decr order
                for(int i = 0; i < incomingArrLen; i++)
                {
                    //fill in the squared arr bc arr in decr order (if positive)
                    sqrdArr[sqrdArrIndex] = nums[incomingArrLen-1-i] * nums[incomingArrLen-1-i];
                    sqrdArrIndex++;
                }

                return sqrdArr;
            }

            //cache useability
            numsArrUseable = numsIndex < incomingArrLen;

            //cache count and useability
            negativeListCount = negativeList.Count();
            negativeListUseable = negativeListIndex < negativeListCount;

            //loop till arr + list no longer useable
            while( numsArrUseable || negativeListUseable )
            {
                //if reg arr unuseable but negative list still useable
                if( negativeListUseable && !numsArrUseable)
                {
                    negativeListCurrNumber = negativeList[negativeListCount-1-negativeListIndex];

                    //fill in the squared arr bc insertion val decided accordingly
                    sqrdArr[sqrdArrIndex] = negativeListCurrNumber * negativeListCurrNumber;
                    sqrdArrIndex++;

                    negativeListIndex++; //(should only incr index w/ inserted)
                }
                //if negative arr useable
                else
                {
                    //cache curr # for ops
                    currNumber = nums[numsIndex];

                    //if curr number negative
                    if( currNumber < 0 )
                    {
                        //add to end of negativeList list once turned positive
                        negativeList.Add(-1 * currNumber);

                        numsIndex++;
                    }
                    //if curr # positive
                    else
                    {
                        //insert val

                        //if list + arr useable
                        if( negativeListUseable && numsArrUseable)
                        {
                            negativeListCurrNumber = negativeList[negativeListCount-1-negativeListIndex];

                            //if curr num has a lower or equal val 
                            if( negativeListCurrNumber >= currNumber )
                            {
                                //fill in the squared arr w/ curr num
                                sqrdArr[sqrdArrIndex] = currNumber * currNumber;
                                sqrdArrIndex++;

                                numsIndex++;
                            }
                            //if negativeList list has a lower val
                            else
                            {
                                //fill in the squared arr bc insertion val decided accordingly
                                sqrdArr[sqrdArrIndex] = negativeListCurrNumber * negativeListCurrNumber;
                                sqrdArrIndex++;

                                negativeListIndex++; //(should only incr index w/ inserted)
                            }
                        }
                        //if only curr nums arr useable
                        else if( numsArrUseable )
                        {
                            //fill in the squared arr w/ curr num
                            sqrdArr[sqrdArrIndex] = currNumber * currNumber;
                            sqrdArrIndex++;

                            numsIndex++;
                        }
                        //if only negativeList list useable
                        else
                        {
                            negativeListCurrNumber = negativeList[negativeListCount-1-negativeListIndex];

                            //fill in the squared arr bc insertion val decided accordingly
                            sqrdArr[sqrdArrIndex] = negativeListCurrNumber * negativeListCurrNumber;
                            sqrdArrIndex++;

                            negativeListIndex++; //(should only incr index w/ inserted)
                        }
                    }

                    //cache useability
                    numsArrUseable = numsIndex < incomingArrLen;
                }

                //cache count and useability
                negativeListCount = negativeList.Count();
                negativeListUseable = negativeListIndex < negativeListCount;

            } 

            return sqrdArr;
        }
    }
}