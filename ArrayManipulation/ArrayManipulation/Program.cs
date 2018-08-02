using System.IO;
using System.Linq;
using System;
using System.Text;

class Solution
{

    // Complete the arrayManipulation function below.
    static long arrayManipulation(int n, int[,] queries)
    {
        int[,] array = new int[queries.GetLength(0), n];
        Console.WriteLine("queries:" + queries.GetLength(0));
        for (int summationNumber = 0; summationNumber < queries.GetLength(0); summationNumber++)
        {
            if (summationNumber > 0)
            {
                Console.WriteLine("startIndex:" + queries[summationNumber, 0]);
                Console.WriteLine("endIndex:" + queries[summationNumber, 1]);
                for (int x = queries[summationNumber, 0] - 1; x <= queries[summationNumber, 1] - 1; x++)
                {
                    Console.WriteLine("x:" + x);
                    Console.WriteLine(queries[summationNumber, 2]);
                    array[summationNumber, x] = array[summationNumber - 1, x] + queries[summationNumber, 2];
                }
                Console.WriteLine();
            }
            else
            {
                for (int x = queries[summationNumber, 0] - 1; x <= queries[summationNumber, 1] - 1; x++)
                {
                    array[summationNumber, x] = queries[summationNumber, 2];
                }
            }
        }
        Print(array, n);
        return array.Cast<int>().Max();
    }

    public static void Print(int[,] array, int n)
    {
        var csv = new StringBuilder();
        for(int row = 0; row < array.GetLength(0); row++)
        {
            for(int col = 0; col < n; col++)
            {
                csv.Append(array[row, col] + ",");
            }
            csv.Append("\n");
        }
        File.WriteAllText(@"C:\Users\Aniket\Documents\Java How To Program Third Edition Covers Java 2 Introducing Swing\Chapter 4 Questions\ArrayManipulation\ArrayManipulation\output.csv", csv.ToString());
    }

    static void Main(string[] args)
    {
        //TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        string[] nm = Console.ReadLine().Split(' ');

        int n = Convert.ToInt32(nm[0]);

        int m = Convert.ToInt32(nm[1]);

        Console.WriteLine("n:" + n);
        Console.WriteLine("m:" + m);

        int[,] queries = new int[m,3];

        String input = File.ReadAllText(@"C:\Users\Aniket\Documents\Java How To Program Third Edition Covers Java 2 Introducing Swing\Chapter 4 Questions\ArrayManipulation\ArrayManipulation\arraymanipulation.txt");

        int i = 0, j = 0;
        foreach (var row in input.Split('\n'))
        {
            j = 0;
            foreach (var col in row.Trim().Split(' '))
            {
                queries[i, j] = Convert.ToInt32(col.Trim());
                //Console.WriteLine(queries[i, j]);
                j++;
            }
            //Console.WriteLine();
            i++;
        }
        //Console.ReadLine();
        long result = arrayManipulation(n, queries);

        Console.WriteLine(result);
        Console.ReadLine();
        //textWriter.WriteLine(result);

        //textWriter.Flush();
        //textWriter.Close();
    }
}