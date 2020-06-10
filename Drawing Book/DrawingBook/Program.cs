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
            //front
            int counterFront = 0;
            for(int i = 1; i <=n; i++)
            {
                if(i % 2 == 0)
                {
                    counterFront++;
                }
                if(i == p)
                {
                    break;
                }
            }
            //back
            int counterBack = 0;
            for (int i = n; i >=1; i--)
            {
                if (i == p || p == (n - 1))
                {
                    if (i % 2 == 0)
                    {
                        counterBack++;
                    }
                    break;
                }
            }

            if(counterBack < counterFront)
            {
                return counterBack;
            }
            else if(counterFront < counterBack)
            {
                return counterFront;
            }
            else
            {
                return counterFront;
            }
        }
    }
}
