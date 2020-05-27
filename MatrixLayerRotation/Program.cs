using System;
using System.Collections.Generic;
using System.Linq;

namespace RotateLeft
{
    public class MatrixRotation
    {
        static void Main(string[] args)
        {
            int[] a = {1,2,3,4,5};
            int[] newArray = new int[a.Length];
            int r= 4;
            for(int i =0; i < a.Length; i++)
            {
                newArray[(i + r) % a.Length] = a[i]; 
            }

            /*foreach(var num in newArray)
            {
                Console.WriteLine(num);
            }*/


            List<List<int>> matrix = new List<List<int>>();
            for(int j = 0; j <4; j++)
            {
                List<int> subList = new List<int>();
                for (int i = 1; i <= 4; i++)
                {
                    subList.Add(i);
                }
                matrix.Add(subList);
            }

            foreach (var sublist in matrix)
            {
                foreach (var value in sublist)
                {
                    Console.Write(value);
                    Console.Write(' ');
                }
                Console.WriteLine();
            }

            /*List<int> output = storeMatrixIn1DArrayCounterClockwise(matrix);

            foreach(var item in output)
            {
                Console.Write(item + ",");
            }*/
        }
        public List<int> storeMatrixIn1DArrayCounterClockwise(List<List<int>> matrix)
        {
            List<int> output = new List<int>();
            int n = matrix[0].Count;
            int m = matrix.Count;

            //Console.WriteLine("cols:"+n);
            //Console.WriteLine("rows:"+m);

            //store elements in array
            if (m > 1 && n > 1)
            {
                List<int> a = new List<int>();
                List<int> b = new List<int>();
                List<int> c = new List<int>();
                List<int> d = new List<int>();
                for (int row = 0; row < m; row++)
                {
                    a.Add(matrix[row][0]);
                }

                for (int col = 1; col < n; col++)
                {
                    b.Add(matrix[m-1][col]);
                }

                for (int row = m - 1; row > 0; row--)
                {
                    c.Add(matrix[row][n - 1]);
                }

                for (int col = n - 2; col > 0; col--)
                {
                    d.Add(matrix[0][col]);
                }

                output = a.Concat(b).Concat(c).Concat(d).ToList();
            }
            else if(n > 1 && m == 1)
            {
                output = matrix[0];
            }
            else if(m > 1 && n == 1)
            {
                List<int> a = new List<int>();
                for (int row = 0; row < m; row++)
                {
                    a.Add(matrix[row][0]);
                }
                output = a;
            }
            return output;
        }
    }
}
