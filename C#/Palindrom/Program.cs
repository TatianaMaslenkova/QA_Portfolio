// Программа проверяет является ли пятизначное число палиндромом

Console.Clear();
Console.Write("Введите пятизначное число: ");
int num = int.Parse(Console.ReadLine()!);
if (num > 9999 && num < 100000)
{
    int currNum = num;
    int result = 0;

    while (currNum > 0)
    {
        int digit = currNum % 10;
        result = result * 10 + digit;
        currNum /= 10;
        Console.WriteLine(result);
    }
    if (num == result)
    {
        Console.WriteLine($"Число {num} является палиндромом");
    }
    else
    {
        Console.WriteLine($"Число {num} НЕ является палиндромом");
    }
}
else
{
    Console.WriteLine("Введите пятизначное число!!!");
}
