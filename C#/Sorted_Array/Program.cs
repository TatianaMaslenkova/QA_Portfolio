// Написать прогу, кот.задаёт массив из 8 случ.цел.чисел и выводит отсортированный
// по модулю массив
Console.Clear();
int size = 8;
int[] array = new int[size];
FillArray(array, -9, 9);
PrintArray(array);
Sort(array);
PrintArray(array);

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
void Sort(int[] arr)
{
    for(int i = 1; i < arr.Length; i++)
    {
        for(int j = 0; j < arr.Length - 1; j++)   
        {
            if(Math.Abs(arr[j]) > Math.Abs(arr[j + 1]))
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
