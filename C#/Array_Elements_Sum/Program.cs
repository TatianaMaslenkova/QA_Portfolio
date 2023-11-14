// Задать массив из 12 элементов, заполненных числами из [-9,9]. Найти сумму 
// положительных/отрицательных элементов массива
Console.Clear();
int size = 12;
int[] array = new int[size];
FillArray(array, -9, 9);
PrintArray(array);
Console.WriteLine($"Сумма положит. элементов массива равна {PositiveNumSum(array)}");
Console.WriteLine($"Сумма отриц. элементов массива равна {NegativeNumSum(array)}");

void FillArray(int[] arr,
               int minValue = 0,
               int maxValue = 100)
{
    maxValue++;

    Random randGenerator = new Random();
    for (int i = 0; i < array.Length; i++)
    {
        array[i] = randGenerator.Next(minValue, maxValue);
    }
}
void PrintArray(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        Console.Write(arr[i] + " ");
    }
    Console.WriteLine();
}
int PositiveNumSum (int[] arr)
{
    int pSum = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        if(arr[i] > 0)
        pSum += arr[i];
    }
    return pSum;
}
int NegativeNumSum(int[] arr)
{
    int nSum = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        if(arr[i] < 0)
        nSum += arr[i];
    }
    return nSum;
}