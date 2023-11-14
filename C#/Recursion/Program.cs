// На вход подаётся поговорка “без труда не выловишь и рыбку из пруда”. Используя рекурсию, подсчитайте, сколько в 
// поговорке гласных букв.
Console.Clear();
string phrase = "без труда не выловишь и рыбку из пруда";
char[] alphabet = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'};
// int count = 0;
// foreach (char letter in phrase)
// {
//     bool contain = alphabet.Contains(letter);
//     if(contain) count++;
//     Console.WriteLine($"Буква {letter} гласная: {contain}");
// }
// Console.WriteLine($"В поговорке {count} гласных букв");
int CountOfVowelLetters(
                    string phrase, 
                    char[] alphabet, 
                    int count = 0, 
                    int index = 0)
{
    if(index == phrase.Length) return count;
    bool contain = alphabet.Contains(phrase[index]);
    if(contain) count++;
    index++;
    return CountOfVowelLetters(phrase, alphabet, count, index);
}
Console.WriteLine($"В поговорке {CountOfVowelLetters(phrase, alphabet)} гласных букв");