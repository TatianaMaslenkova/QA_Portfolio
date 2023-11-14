// В двумерном массиве целых чисел удалить строку и столбец, на пересечении которых расположен наименьший элемент 
Console.Clear();
Random randSize = new Random();
int rows = randSize.Next(1, 10);
int columns = randSize.Next(1, 10);
int[,] array = new int[rows, columns];
FillArray(array, -100, 100);
PrintArray(array);

int min = array[0, 0];
int i_min = 0;
int j_min = 0;
for (int i = 0; i < rows; i++)
{
    for (int j = 0; j < columns; j++)
    {
        if (array[i, j] < min)
        {
            min = array[i, j];
            i_min = i;
            j_min = j;
        }
    }
}
Console.WriteLine($"N[{i_min + 1}, {j_min + 1}] = {min}");

int rowsRes = rows - 1;
int columnsRes = columns - 1;
int[,] result = new int[rowsRes, columnsRes];
int bias_i = 0;
int bias_j = 0;
for (int i = 0; i < rowsRes; i++)
{
    if (i == i_min) bias_i++;
    bias_j = 0;
    for (int j = 0; j < columnsRes; j++)
    {
        if (j == j_min) bias_j++;
        result[i, j] = array[i + bias_i, j + bias_j];
    }
}
Console.WriteLine();
PrintArray(result);
// 2-й способ:
for (int i = 0; i < rows; i++)
{
    if (i != i_min)
    {
        for (int j = 0; j < columns; j++)
        {
            if (j != j_min)
            Console.Write(array[i, j] + "\t");
        }
        Console.WriteLine();
    }
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