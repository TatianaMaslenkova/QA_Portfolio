/*
 * Реализовать консольное приложение, которое:
 * 1. Принимает от пользователя и “запоминает” строки.
 * 2. Если введено print, выводит строки так, чтобы последняя введенная была первой в списке, 
 * а первая - последней.
 * 3. Если введено revert, удаляет предыдущую введенную строку из памяти.
 */
import java.util.Scanner;
import java.util.Stack;
public class Task2 {
    public static void main(String[] args) {
        Stack<String> stack = new Stack<>();
        String str = "";
        Scanner iScanner = new Scanner(System.in);
        for (int i = 0; i < 5; i++) {
            System.out.println("строка");
            str = iScanner.nextLine();
            stack.push(str);
        }
        System.out.println("команда");
        str = iScanner.nextLine();
        System.out.println();
        if (str.equals("print")) {
            for (int i = 0; i < 5; i++) {
                System.out.println(stack.pop());
        }
        }else{
            if (str.equals("revert")) {
                stack.remove(stack.size()-1);
            }
        System.out.println(stack);
        }
    }     
}
