// Показать натуральные числа от M до N рекурсией, N и M заданы
Console.Clear();
Console.Write("Введите число n: ");
int n = int.Parse(Console.ReadLine()!);
Console.Write("Введите число m: ");
int m = int.Parse(Console.ReadLine()!);
FindMtoN(n, m);
void FindMtoN(int n, int a = 1)
{
    Console.WriteLine(a);
    a++;
    if (a > n)
    {
        return;
    }
    FindMtoN(n, a);
}