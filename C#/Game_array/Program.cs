// Дан массив 2х10. В 1-й строке записано кол-во мячей, забитых футбольной командой в той или иной игре,
// во 2-й - кол-во пропущенных мячей в той же игре. а) для кажд.проведенной игры напечатать словесный
// рез-т: "выигрыш", "ничья" или "проигрыш". b) опр-ть кол-во выигрышей данной команды, c) опр-ть 
// кол-во выигрышей и кол-во проигрышей данной команды, d) опр-ть кол-во выигрышей, ничьих и проигр-й
// данной команды, e) опр-ть в ск-их играх разность забитых и пропущенных мячей была >=3, f) опр-ть
// общее число очков, набранных командой (за выигрыш дают 3 очка, ничью - 1, проигрыш - 0)
Console.Clear();
int rows = 2;
int columns = 10;
int[,] array = new int[rows, columns];

FillArray(array, 0, 10);
PrintArray(array);
AResText(array);
BCDRes(array);
FRes(array);

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
            Console.Write(arr[i, j] + "  ");
        }
        Console.WriteLine();
    }
    Console.WriteLine();
}
void AResText(int[,] arr)
{
    int rows = arr.GetLength(0);
    int columns = arr.GetLength(1);
    for (int i = 0; i < columns; i++)
    {
        Console.WriteLine($"Счёт: {arr[0, i]} : {arr[1, i]}");
        if(arr[0, i] > arr[1, i])
        {
            Console.WriteLine($"Победа!");
        }
        else if(arr[0, i] < arr[1, i])
        {
            Console.WriteLine($"Проигрыш!");
        }
        else
        {
            Console.WriteLine($"Ничья!");
        }
    }
}
void BCDRes(int[,] arr)
{
    int rows = arr.GetLength(0);
    int columns = arr.GetLength(1);
    int win = 0;
    int lose = 0;
    int draw = 0;
    for (int i = 0; i < columns; i++)
    {
        if(arr[0, i] > arr[1, i])
        {
            win++;
        }
        else if(arr[0, i] < arr[1, i])
        {
            lose++;
        }
        else
        {
            draw++;
        }
    }
    Console.WriteLine($"Количество побед: {win}");
    Console.WriteLine($"Количество поражений: {lose}");
    Console.WriteLine($"Количество ничьих: {draw}");
}
void FRes(int[,] arr)
{
    int rows = arr.GetLength(0);
    int columns = arr.GetLength(1);
    int win = 0;
    int lose = 0;
    int draw = 0;
    int points = 0;
    for (int i = 0; i < columns; i++)
    {
        if(arr[0, i] > arr[1, i])
        {
            win++;
        }
        else if(arr[0, i] < arr[1, i])
        {
            lose++;
        }
        else
        {
            draw++;
        }
    }
    points = win * 3 + draw;
    Console.WriteLine($"Общее число очков, набранных командой = {points}");
}