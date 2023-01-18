/// <summary>
/// Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:
/// Starting with any positive integer, replace the number by the sum of the squares of its digits.
/// Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
/// Those numbers for which this process ends in 1 are happy.
/// Return true if n is a happy number, and false if not.
/// </summary>
public class HappyNumber
{
    /// <summary>
    /// 
    /// Speed: O(M) (linear)
    /// Space: O(M) where M = number of intermediate numbers till loop or 1 found
    ///     could be O(1) if tortoise + hair alg used to find loop instead w/ 2 pntrs cross
    /// </summary>
    /// <param name="n"></param>
    /// <returns></returns>
    public bool IsHappy(int n) {

        Dictionary<int, bool> history = new Dictionary<int, bool>();

        while(true)
        {
           int sqrOfDigits = 0;

           Console.WriteLine(n);

            while(n > 0)
            {
                int remainder = n % 10;

                Console.WriteLine(remainder.ToString());

                int remainderSqrd = remainder*remainder;

                sqrOfDigits += remainderSqrd;

                double nDivTen = n / 10; //floor funct must take double, not a float

                //Console.WriteLine($"{n} div'd by 10 {nDivTen.ToString()}");

                n = (int)Math.Floor( nDivTen );

                Console.WriteLine($"New n is {n.ToString()}");
            }

            if( sqrOfDigits == 1)
            {
                return true;
            }

            //if havent already seen number
            if( !history.TryGetValue(sqrOfDigits, out bool value)  )
            {
                //add number to history
                history.Add(sqrOfDigits, true);

                n = sqrOfDigits;
            }
            //not happy number bc loop repeating 
            else
            {
                return false;
            }   
        }
        
    }
}
