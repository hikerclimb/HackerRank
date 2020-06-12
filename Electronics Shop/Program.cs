using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata.Ecma335;

namespace Electronics_Shop
{
    public class Program
    {
        static void Main(string[] args)
        {

        }

        public int getMoneySpent(int[] keyboards, int[] drives, int b)
        {
            List<int> two_Items_Added_Together_List = new List<int>();
            for (int numberOfKeyboards = 0; numberOfKeyboards < keyboards.Length; numberOfKeyboards++)
            {
                for (int numberOfDrives = 0; numberOfDrives < drives.Length; numberOfDrives++)
                {
                    two_Items_Added_Together_List.Add(keyboards[numberOfKeyboards] + drives[numberOfDrives]);
                }
            }
            int orderedList = 0;
            try
            {
                orderedList = two_Items_Added_Together_List.OrderByDescending(x => x).Select(x => x).Where(x => x <= b).Max();
            }
            catch(Exception ex)
            {
                return -1;
            }
            return orderedList;
        }
    }
}
