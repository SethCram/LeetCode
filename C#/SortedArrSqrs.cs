namespace LeetCode
{
    using System;

    public class SortedArrSqrs
    {
        /*
            Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
             Non-decreasing so subsequent numbers can be the same
        */
        public int[] SortedSquares(int[] nums) 
        {
            //cache arr size
            int incomingArrLen = nums.Length;

            //declare new arr of same size as incoming one
            int[] sqrdArr = new int[incomingArrLen];

            //declare a new lists
            List<int> unorderedList = new List<int>();
            List<int> replaceNumberList = new List<int>();

            int phNumber;
            int currNumber;
            int sqrdArrIndex = 0;
            int unorderedListIndex = 0;
            int unorderedCurrNumber;
            int replaceNumberListIndex = 0;
            int insertionVal;
            int replacementCurrNumber;

            bool unorderedListUseable = false;
            bool replaceNumberListUseable = false;

            int unorderedCount;//= 0; //shouldn't need initing?
            int replaceCount;

            //bool unorderedNull;
            //bool replaceNull;

            //Possible sorts: Quick Sort, Bubble Sort

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

            //walk thru incoming arr that's in non-decr order (and has positives in it)
            for(int i = 0; i < incomingArrLen; i++)
            {
                //cache curr # for ops
                currNumber = nums[i];

                //if curr number negative
                if( currNumber < 0 )
                {
                    //add to end of unordered list once turned positive
                    unorderedList.Add(-1 * currNumber);
                }
                //if curr # positive
                else
                {
                    //cache count and useability of each list

                    unorderedCount = unorderedList.Count();
                    unorderedListUseable = unorderedCount > 0 && unorderedListIndex < unorderedCount;

                    replaceCount = replaceNumberList.Count();
                    replaceNumberListUseable = replaceCount > 0 && replaceNumberListIndex < replaceCount;
                    
                    //insert val

                    //if both lists useable
                    if( unorderedListUseable && replaceNumberListUseable)
                    {
                        //cache curr replacement val
                        replacementCurrNumber = replaceNumberList[replaceNumberListIndex];
                        //cache curr unordered list val
                        unorderedCurrNumber = unorderedList[unorderedCount-1-unorderedListIndex];

                        //if replacement list has a lower or equal val 
                        if( unorderedCurrNumber >= replacementCurrNumber )
                        {
                            //if curr number is greater than the insertion val
                            if( currNumber > replacementCurrNumber )
                            {
                                //add replaced number to the replacement list
                                replaceNumberList.Add( currNumber );

                                //fill in the squared arr bc insertion val decided accordingly
                                sqrdArr[sqrdArrIndex] = replacementCurrNumber * replacementCurrNumber;
                                sqrdArrIndex++;

                                replaceNumberListIndex++; //(should only incr index w/ inserted)
                            }
                            //if curr number is less than or equal to insertion val
                            else
                            {
                                //fill in the squared arr
                                sqrdArr[sqrdArrIndex] = currNumber * currNumber;
                                sqrdArrIndex++;
                            }
                        }
                        //if unordered list has a lower val
                        else
                        {

                            if( currNumber > unorderedCurrNumber )
                            {
                                //add replaced number to the replacement list
                                replaceNumberList.Add( currNumber );

                                //fill in the squared arr bc insertion val decided accordingly
                                sqrdArr[sqrdArrIndex] = unorderedCurrNumber * unorderedCurrNumber;
                                sqrdArrIndex++;

                                unorderedListIndex++; //(should only incr index w/ inserted)
                            }
                            //if curr number is less than or equal to insertion val
                            else
                            {
                                //fill in the squared arr
                                sqrdArr[sqrdArrIndex] = unorderedCurrNumber * unorderedCurrNumber;
                                sqrdArrIndex++;
                            }
                        }
                    }
                    //if unordered list useable
                    else if( unorderedListUseable )
                    {
                        //cache curr unordered list val
                        unorderedCurrNumber = unorderedList[unorderedCount-1-unorderedListIndex];

                        if( currNumber > unorderedCurrNumber )
                        {
                            //add replaced number to the replacement list
                            replaceNumberList.Add( currNumber );

                            //fill in the squared arr bc insertion val decided accordingly
                            sqrdArr[sqrdArrIndex] = unorderedCurrNumber * unorderedCurrNumber;
                            sqrdArrIndex++;

                            unorderedListIndex++; //(should only incr index w/ inserted)
                        }
                        //if curr number is less than or equal to insertion val
                        else
                        {
                            //fill in the squared arr
                            sqrdArr[sqrdArrIndex] = unorderedCurrNumber * unorderedCurrNumber;
                            sqrdArrIndex++;
                        }
                    }
                    //if replace # list useable
                    else if( replaceNumberListUseable )
                    {
                        //cache curr replacement val
                        replacementCurrNumber = replaceNumberList[replaceNumberListIndex];

                        if( currNumber > replacementCurrNumber )
                        {
                            //add replaced number to the replacement list
                            replaceNumberList.Add( currNumber );

                            //fill in the squared arr bc insertion val decided accordingly
                            sqrdArr[sqrdArrIndex] = replacementCurrNumber * replacementCurrNumber;
                            sqrdArrIndex++;

                            replaceNumberListIndex++; //(should only incr index w/ inserted)
                        }
                        //if curr number is less than or equal to insertion val
                        else
                        {
                            //fill in the squared arr
                            sqrdArr[sqrdArrIndex] = currNumber * currNumber;
                            sqrdArrIndex++;
                        }
                    }
                    //if neither list useable for number insertions
                    else
                    {
                        //we're done so break out of loop
                        break;
                    }
                }
            }

            return sqrdArr;
        }

        /*
        private void something(int currNumber, int insertionVal)
        {
            //if curr number is greater than the insertion val
            if( currNumber > insertionVal )
            {
                //add replaced number to the replacement list
                replaceNumberList.Add( currNumber );
                
                //replace num w/ insertion number
                //nums[i] = insertionVal;

                //place inserted val into the og arr
                //nums[shiftIndex] = insertionVal;
                //shiftIndex++;

                //fill in the squared arr bc insertion val decided accordingly
                sqrdArr[sqrdArrIndex] = insertionVal * insertionVal;
                sqrdArrIndex++;
            }
            //if curr number is less than or equal to insertion val
            else
            {
                //fill in the squared arr
                sqrdArr[sqrdArrIndex] = currNumber * currNumber;
                sqrdArrIndex++;
            }
        }
        */
    }
}