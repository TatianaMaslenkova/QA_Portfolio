import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

/*
* Написать программу, определяющую правильность расстановки скобок в выражении.
Пример 1: a+(d*3) - истина
Пример 2: [a+(1*3) - ложь
Пример 3: [6+(3*3)] - истина
Пример 4: {a}[+]{(d*3)} - истина
Пример 5: <{a}+{(d*3)}> - истина
Пример 6: {a+]}{(d*3)} - ложь
*/
public class Task3 {
    public static void main(String[] args) {
        System.out.println(isValidBrackets("(5+{3*3)}"));
    }
    private static boolean isValidBrackets(String input) {
        Map<Character, Character> brackets = new HashMap<>();
        brackets.put(')', '(');
        brackets.put('}', '{');
        brackets.put(']', '['); 
        brackets.put('>', '<');
        Deque<Character> stack = new LinkedList<>();
        for (char c : input.toCharArray()) {
            if (brackets.containsValue(c)) {
                // одна из открывающих скобок
                stack.push(c);
            } else if (brackets.containsKey(c)) {
                // одна из закрывающих скобок
                if (stack.isEmpty() || stack.pop() != brackets.get(c)) {
                    return false;
                }
            }
        }
        // в конце стек должен быть пустым
        return stack.isEmpty(); 
    }
}
