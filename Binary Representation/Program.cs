using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Yitzog_Binary
{
    internal class Program
    {
        public static int HexToDec(string hex)
        {
            int num = 0;
            int place = hex.Length - 1;
            for (int i = 0; i < hex.Length; i++)
            {
                char c = char.ToUpper(hex[i]);
                int value = 0;

                if (char.IsDigit(c))
                    value = c - '0';  // Convert char digit to int
                else if (c >= 'A' && c <= 'F')
                    value = c - 'A' + 10;

                num += value * (int)Math.Pow(16, place);
                place--;
            }
            return num;
        }

        public static string DecToHex(int dec)
        {

        }

        static void Main(string[] args)
        {
            Console.WriteLine(HexToDec("F1"));
            Console.ReadLine();
        }
    }
}
