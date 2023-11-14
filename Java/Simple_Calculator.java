/*
 * Реализовать простой калькулятор
 */
package HW_1;
import java.util.Scanner;
public class HW1_Task3 {
    public static void main(String[] args) {
        Scanner iScanner = new Scanner(System.in);
        System.out.print("Введите число 1: ");
        double number1 = iScanner.nextDouble();
        System.out.print("Введите число 2: ");
        double number2 = iScanner.nextDouble();
        System.out.print("Введите желаемое действие(+, -, *, /): ");
        char operation = iScanner.next().charAt(0);
        double result;
        switch (operation) {
            case '+':
            result = number1 + number2;
            break;
            case '-':
            result = number1 - number2;
            break;
            case '*':
            result = number1 * number2;
            break;
            case '/':
            result = number1 / number2;
            break;
            default:
            System.out.println("Нет такого действия");
            return;
        }
        System.out.println("Результат:");
        System.out.println(number1 + " " + operation + " " + number2 + " = " + result);
        iScanner.close();
    }
}
