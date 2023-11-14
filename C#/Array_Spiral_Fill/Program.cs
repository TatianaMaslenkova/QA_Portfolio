// Заполнить спирально массив 4х4 числами от 1 до 16
Console.Clear();
int rows = 4;
int columns = 3;
int[,] array = new int[rows, columns];
int index = 0;
int currentRow = 0;
int currentColumn = 0;
int changeIndexRow = 0;
int changeIndexColumn = 1;
int steps = columns;
int turn = 0;
while(index < array.Length)
{
    array[currentRow, currentColumn] = index + 1;
    // Console.Write(array[currentRow, currentColumn] + " ");
    index++;
    steps--;
    if(steps == 0)
    {
        // if(turn % 2 == 0)
        //     steps = rows - 1 - turn / 2;
        // else
        //     steps = columns - 1 - turn / 2;
        steps = rows * ((turn + 1) % 2) + columns * (turn % 2) - 1 - turn / 2;
        int temp = changeIndexRow;
        changeIndexRow = changeIndexColumn;
        changeIndexColumn = -temp;
        turn++;
    }
    currentRow += changeIndexRow;
    currentColumn += changeIndexColumn;
}
PrintArray(array);

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