using System;

namespace DrawingBook
{
    public class Program
    {
        static void Main(string[] args)
        {
            
        }

        public int pageCount(int n, int p)
        {
            int totalNumberOfPagesToTurnFromFront = n / 2;
            int numberOfPagesToTurnFromFrontTillYouHitTargetPageCount = p / 2;
            int numberOfPagesToTurnFromBackTillYouHitTargetPageCount = totalNumberOfPagesToTurnFromFront - numberOfPagesToTurnFromFrontTillYouHitTargetPageCount;

            if (numberOfPagesToTurnFromBackTillYouHitTargetPageCount < numberOfPagesToTurnFromFrontTillYouHitTargetPageCount)
            {
                return numberOfPagesToTurnFromBackTillYouHitTargetPageCount;
            }
            else if(numberOfPagesToTurnFromFrontTillYouHitTargetPageCount < numberOfPagesToTurnFromBackTillYouHitTargetPageCount)
            {
                return numberOfPagesToTurnFromFrontTillYouHitTargetPageCount;
            }
            else
            {
                return numberOfPagesToTurnFromBackTillYouHitTargetPageCount;
            }
        }
    }
}
