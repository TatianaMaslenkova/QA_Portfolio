/*
 * Даны 2 строки, написать метод, который вернет true, если эти строки являются изоморфными и false, если нет. 
 * Строки изоморфны, если одну букву в первом слове можно заменить на некоторую букву во втором слове, при этом
1. повторяющиеся буквы одного слова меняются на одну и ту же букву с сохранением порядка следования. 
(Например, add - egg изоморфны)
2. буква может не меняться, а остаться такой же. (Например, note - code)
Пример 1:
Input: s = "foo", t = "bar"
Output: false
Пример 2:
Input: s = "paper", t = "title"
Output: true
 */
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
public class Task2 {
    // Определить, являются ли строки 'X' и 'Y' изоморфными или нет
    public static boolean isIsomorphic(String s, String t)
    {
        if (s.length() != t.length() || s == null || t == null) {
            return false;
        }
        // используем карту для хранения сопоставления символов строки 'X' со строкой 'Y'
        Map<Character, Character> map = new HashMap<>();
        // используем set для хранения пула уже сопоставленных символов
        Set<Character> set = new HashSet<>();
 
        for (int i = 0; i < s.length(); i++)
        {
            char x = s.charAt(i);
            char y = t.charAt(i);
            // если 'x' был замечен раньше
            if (map.containsKey(x))
            {   // вернуть false, если первое вхождение `x` сопоставлено
                // другой символ
                if (map.get(x) != y) {
                    return false;
                }
            }
            // если 'x' виден в первый раз (т.е. он еще не отображен)
            else {
                // вернуть false, если 'y' уже сопоставлен с каким-то другим символом в 'X'
                if (set.contains(y)) {
                    return false;
                }
                // сопоставляем 'y' с 'x' и помечаем его как сопоставленный
                map.put(x, y);
                set.add(y);
            }
        }
        return true;
    }
     public static void main(String[] args)
    {
        String s = "foo";
        String t = "bar";
        if (isIsomorphic(s, t)) {
            System.out.println("true");
        }
        else {
            System.out.println("false");
        }
    }
}
