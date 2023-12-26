using System;
namespace HomeworkPI
{
    public class HomeworkPI
    {
        static void Main(string[] args)
        {
            int n = 666;
            Zeroing(ref n);

            Console.WriteLine($"Обнуление разряда десятков: {n}");

            Console.WriteLine($"Минимум = {DoubleMin(12.625, 666)}")
        }


        /// <summary>
        /// Обнуляет разряд десятков в трехзначном числе.
        /// </summary>
        /// <param name="n"></param>
        /// <returns></returns>
        public static int Zeroing(ref int n)
        {
            if (n < 99 || n > 999)
            {
                throw new ArgumentException("Число не трехзначное");
            }

            n = n / 100 * 100 + n % 10;
            return n;
        }

        /// <summary>
        /// Возвращает минимум из двух переданных вещественных чисел
        /// </summary>
        /// <param name="a"></param>
        /// <param name="b"></param>
        /// <returns></returns>
        public static double DoubleMin(double a, double b) => Math.Min(a, b);
    }
}