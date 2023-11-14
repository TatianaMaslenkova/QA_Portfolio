// Написать программу, которая в двумерном массиве заменяет строки на столбцы или сообщить, что это 
// невозможно (в случае, если матрица не квадратная).
Console.Clear();
Console.Write("Введите количество строк массива: ");
int rows = int.Parse(Console.ReadLine()!);
Console.Write("Введите количество столбцов массива: ");
int columns = int.Parse(Console.ReadLine()!);
// Random randSize = new Random();
// int rows = randSize.Next(1, 10);
// int columns = randSize.Next(1, 10);
int[,] array = new int[rows, columns];

if (rows == columns)
{
    FillArray(array, -9, 9);
    PrintArray(array);
    ChangeColumnsRows(array);
    Console.WriteLine("Новый массив:");
    PrintArray(array);
}
else
{
    Console.WriteLine("Матрица не квадратная, поэтому невозможно поменять строки и столбцы местами");
}



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

void ChangeColumnsRows(int[,] arr)
{
    int rows = arr.GetLength(0);
    int columns = arr.GetLength(1);
    for (int i = 0; i < rows; i++)
    {
        for (int j = i; j < columns; j++)
        {
            int temp = arr[i, j];
            arr[i, j] = arr[j, i];
            arr[j, i] = temp;
            // (arr[i, j], arr[j, i]) = (arr[j, i], arr[i, j]);
        }
    }
}