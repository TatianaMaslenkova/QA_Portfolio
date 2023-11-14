// Двумерный массив размером 5х5 заполнен случайными нулями и единицами. Игрок может ходить только по полям,
// заполненным единицами. Проверьте, существует ли путь из точки [0, 0] в точку [4, 4] (эти поля требуется 
// принудительно задать равными единице).
Console.Clear();
int rows = 12;
int columns = 12;
int[,] map = new int[rows, columns];

FillArray(map, 0, 1);
int i_max = rows - 1;
int j_max = columns - 1;
map[0, 0] = 1;
map[i_max, j_max] = 1;
// PrintArray(map);
bool exit = false;
while(!exit)
{
    FillArray(map, 0, 1);
    FindPath(map);
}
PrintArray(map);
if (exit) Console.WriteLine("Выход есть");
else Console.WriteLine("нет");
//PrintArray(map);

void FillArray(int[,] arr,
               int minValue = 0,
               int maxValue = 1)
{
    maxValue++;
    Random randGenerator = new Random();
    int rows = arr.GetLength(0);
    int columns = arr.GetLength(1);
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            map[i, j] = randGenerator.Next(minValue, maxValue);
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

void FindPath(int[,] arr, int i = 0, int j = 0)
{
    if (i < 0
        || i > i_max
        || j < 0
        || j > j_max
        || map[i, j] == 0
        || map[i, j] == 2)
    {
        return;
    }
    map[i, j] = 2;
    if (i == i_max && j == j_max)
    {
        exit = true;
        return;
    }
    FindPath(map, i + 1, j);
    FindPath(map, i - 1, j);
    FindPath(map, i, j + 1);
    FindPath(map, i, j - 1);
    // FindPath(map, i + 1, j + 1);
    // FindPath(map, i - 1, j - 1);
    // FindPath(map, i + 1, j - 1);
    // FindPath(map, i - 1, j + 1);
}

// Начало бродилки:
// int x = 0;
// int y = 0;
// bool isPlaying = true;
// string player = "@";
// while (isPlaying)
// {
// Console.Clear();
// Console.SetCursorPosition(x, y);
// Console.Write(player);
// ConsoleKeyInfo keyInfo = Console.ReadKey();
// Console.CursorVisible = false;
// if(keyInfo.Key == ConsoleKey.DownArrow)
// {
//     y++;
// }
// if(keyInfo.Key == ConsoleKey.UpArrow)
// {
//     y--;
// }
// if(keyInfo.Key == ConsoleKey.LeftArrow)
// {
//     x--;
// }
// if(keyInfo.Key == ConsoleKey.RightArrow)
// {
//     x++;
// }
// if(keyInfo.Key == ConsoleKey.E)
// {
//     isPlaying = false;
//     Console.Clear();
//     Console.WriteLine("Спасибо за игру!");
// }