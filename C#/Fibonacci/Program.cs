// Не используя рекурсию, выведите N первых чисел Фибоначчи. Первые 2 числа: 0 и 1
Console.Clear();
Console.Write("Введите количество чисел Фибоначчи, которое хотите увидеть: ");
int n = int.Parse(Console.ReadLine()!);
double[] array = new double[n];
int first = 0;
int second = 1;
array[0] = first;
array[1] = second;
for (int i = 2; i < array.Length; i++)
{
    array[i] = array[i - 1] + array[i - 2];
}
PrintArray(array);

void PrintArray(double[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        Console.Write(arr[i] + " ");
    }
    Console.WriteLine();
}