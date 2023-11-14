// Написать прогу, кот.принимает на вход координаты 2 точек и находит расстояние 
// между ними в пространстве 3D
Console.Clear();
Console.Write("Введите координату x точки А: ");
int x1 = int.Parse(Console.ReadLine()!);

Console.Write("Введите координату y точки А: ");
int y1 = int.Parse(Console.ReadLine()!);

Console.Write("Введите координату z точки А: ");
int z1 = int.Parse(Console.ReadLine()!);

Console.Write("Введите координату x точки B: ");
int x2 = int.Parse(Console.ReadLine()!);

Console.Write("Введите координату y точки B: ");
int y2 = int.Parse(Console.ReadLine()!);

Console.Write("Введите координату z точки B: ");
int z2 = int.Parse(Console.ReadLine()!);

int a = x2 - x1;
int b = y2 - y1;
int c = z2 - z1;

double distance = Math.Sqrt(a * a + b * b + c * c);
distance = Math.Round(distance, 2);
Console.WriteLine($"Расстояние между точками: {distance}");

