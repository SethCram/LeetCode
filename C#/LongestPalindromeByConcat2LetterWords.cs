/// <summary>
/// You are given an array of strings words. Each element of words consists of two lowercase English letters. Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once. Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0. A palindrome is a string that reads the same forward and backward.
/// </summary>
public class LongestPalindromeByConcat2LetterWords
{
    public int LongestPalindrome(string[] words)
    {
        Dictionary<string, int> letterCountDict = new Dictionary<string, int>();

        int unpaired = 0;
        int palindromeLength = 0;

        //walk thru words
        for (int i = 0; i < words.Length; i++)
        {
            string currWord = words[i];

            bool lettersSame = (currWord[0] == currWord[1]);

            string currWordReverse = String.Concat(currWord[1], currWord[0]);

            bool currWordPresent = letterCountDict.TryGetValue(currWord, out int currWordCount);

            //if dict has word reverse
            bool reverseWordPresent = letterCountDict.TryGetValue(currWordReverse, out int reverseWordCount);

            //if reverse word present + curr word missing or enough left to pair
            if(reverseWordPresent && (!currWordPresent || reverseWordCount > currWordCount) )
            {
                //4 letters added to palindrome
                palindromeLength += 4;
            }

            //if curr word present
            if(currWordPresent)
            {
                //incr count of it
                letterCountDict[currWord] = currWordCount + 1;

                //if same letters and odd count of them
                if(lettersSame && currWordCount % 2 != 0)
                {
                    unpaired -= 1;

                    //4 letters added to palindrome
                    palindromeLength += 4;
                }
                //if same letters w/ even count
                else if(lettersSame)
                {
                    unpaired += 1;
                }
            }
            //curr word missing
            else
            {
                //init its count to 1
                letterCountDict[currWord] = 1;

                if(lettersSame)
                {
                    unpaired += 1;
                }
            }
        }

        //if any unpaired words left
        if(unpaired > 0)
        {
            //account for it being added to the middle of palindrome
            palindromeLength += 2;
        }

        return palindromeLength;
    }
}