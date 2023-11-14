// В двумерном массиве заменить элементы, у которых оба индекса чётные на их квадраты
Console.Clear();
Console.Write("Введите количество строк массива: ");
int rows = int.Parse(Console.ReadLine()!);
Console.Write("Введите количество столбцов массива: ");
int columns = int.Parse(Console.ReadLine()!);
// Random randSize = new Random();
// int rows = randSize.Next(1, 10);
// int columns = randSize.Next(1, 10);
double[,] array = new double[rows, columns];

FillArray(array, -9, 9);
PrintArray(array);
FindEvenIndex(array);
PrintArray(array);

void FillArray(double[,] arr,
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
void PrintArray(double[,] arr)
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

void FindEvenIndex(double[,] arr)
{
    int rows = arr.GetLength(0);
    int columns = arr.GetLength(1);
    for (int i = 0; i < rows; i+=2)
    {
        for (int j = 0; j < columns; j+=2)
        {
            if(i % 2 == 0 && j % 2 == 0)
            {
                arr[i, j] = Math.Pow(arr[i, j], 2);
            }
        }
    }
}