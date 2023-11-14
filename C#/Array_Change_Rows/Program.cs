// Написать программу, которая обменивает элементы первой строки и последней строки
Console.Clear();
Random randSize = new Random();
int rows = randSize.Next(1, 10);
int columns = randSize.Next(1, 10);
int[,] array = new int[rows, columns];

FillArray(array, -9, 9);
PrintArray(array);
ChangeRows(array);
Console.WriteLine("Новый массив:");
PrintArray(array);

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

void ChangeRows(int[,] arr)
{
    int rows = arr.GetLength(0);
    int columns = arr.GetLength(1);
    int maxIndex = rows - 1;
    for (int j = 0; j < columns; j++)
    {
        (arr[0, j], arr[maxIndex, j]) = (arr[maxIndex, j], arr[0, j]);
    }
}