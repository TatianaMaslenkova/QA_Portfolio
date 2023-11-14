// Найти произведение двух матриц
Console.Clear();
Console.Write("Введите количество строк первой матрицы: ");
int rows1 = int.Parse(Console.ReadLine()!);
Console.Write("Введите количество столбцов первой матрицы: ");
int columns1 = int.Parse(Console.ReadLine()!);
int[,] array1 = new int[rows1, columns1];
Console.Write("Введите количество строк второй матрицы: ");
int rows2 = int.Parse(Console.ReadLine()!);
Console.Write("Введите количество столбцов второй матрицы: ");
int columns2 = int.Parse(Console.ReadLine()!);
int[,] array2 = new int[rows2, columns2];
if (columns1 != rows2)
{
    Console.WriteLine("Невозможно перемножить матрицы!");
}
else
{
    FillArray(array1, 0, 7);
    PrintArray(array1);
    FillArray(array2, 0, 7);
    PrintArray(array2);
    int[,] res = new int[rows1, columns2];
    MatrixProd(array1, array2, res);
    PrintArray(res);
    
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
            arr[i, j] = randGenerator.Next(minValue, maxValue);
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
void MatrixProd(int[,] arr1, int[,] arr2, int[,] res)
{
    rows1 = arr1.GetLength(0);
    columns2 = arr2.GetLength(1);
    rows2 = arr2.GetLength(0);
    for (int i = 0; i < rows1; i++)
    {
        for (int j = 0; j < columns2; j++)
        {
            for (int k = 0; k < rows2; k++)
            {
                res[i, j] += arr1[i, k] * arr2[k, j];
            }
        }
    }
}