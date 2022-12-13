/// <summary>
/// You are given an array of strings words. Each element of words consists of two lowercase English letters. Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once. Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0. A palindrome is a string that reads the same forward and backward.
/// </summary>
public class LongestPalindromeByConcat2LetterWords
{
    public int LongestPalindrome(string[] words)
    {
        Dictionary<char, int> letterCountDict = new Dictionary<char, int>();

        int unpaired = 0;
        int palindromeLength = 0;

        //walk thru words
        for (int i = 0; i < words.Length; i++)
        {
            //walk thru letters
            for (int j = 0; j < words[i].Length; j++)
            {
                //cache curr letter
                char currLetter = words[i][j];

                //if dict has letter
                if (letterCountDict.TryGetValue(currLetter, out int currLetterCount))
                {
                    //if adding to even number of nums
                    if(currLetterCount % 2 == 0)
                    {
                        //unpaired letter found
                        unpaired++;
                    }
                    //if adding to odd number of nums
                    else
                    {
                        //pair found for letter
                        unpaired--;
                        //so, 2 letters added to palindrome
                        palindromeLength += 2;
                    }

                    //incr letter count 
                    letterCountDict[currLetter] = currLetterCount + 1;
                }
                //if dict doesnt have letter
                else
                {
                    //init its count to 1
                    letterCountDict[currLetter] = 1;
                    //unpaired letter
                    unpaired++;
                }
            }
        }

        //if any unpaired letters left
        if(unpaired > 0)
        {
            //account for it being added to the middle of palindrome
            palindromeLength += 1;
        }

        return palindromeLength;

    }
}