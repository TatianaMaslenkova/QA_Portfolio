// Задать двумерный массив, найти сумму элементов главной диагонали
Console.Clear();
Console.Write("Введите количество строк массива: ");
int rows = int.Parse(Console.ReadLine()!);
Console.Write("Введите количество столбцов массива: ");
int columns = int.Parse(Console.ReadLine()!);
// Random randSize = new Random();
// int rows = randSize.Next(1, 10);
// int columns = randSize.Next(1, 10);
int[,] array = new int[rows, columns];

FillArray(array, -9, 9);
PrintArray(array);
int res = FindDiagElementsSum(array);
Console.WriteLine($"Сумма элементов главной диагонали равна {res}");

void FillArray(int[,] arr,
               int minValue = 0,
               int maxValue = 100)
{
    maxValue++;
    Random randGenerator = new Random();
    int rows = arr.GetLength(0);
    int columns = arr.GetLength(1);
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            array[i, j] = randGenerator.Next(minValue, maxValue);
        }
    }
}
void PrintArray(int[,] arr)
{
    int rows = arr.GetLength(0);
    int columns = arr.GetLength(1);
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            Console.Write(arr[i, j] + "\t");
        }
        Console.WriteLine();
    }
    Console.WriteLine();
}

int FindDiagElementsSum(int[,] arr)
{
    int sum = 0;
    int rows = arr.GetLength(0);
    int columns = arr.GetLength(1);
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            if(i == j)
            {
                sum+=arr[i, j];
            }
        }
    }
    return sum;
}