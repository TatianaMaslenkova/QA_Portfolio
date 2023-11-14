/*
 * К калькулятору из предыдущего дз добавить логирование.
 */
package HW_2;
import java.util.Scanner;
import java.io.IOException;
import java.util.logging.FileHandler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;
public class HW2_Task2 {
    public static void main(String[] args) throws IOException{
        Logger logger = Logger.getLogger(HW2_Task2.class.getName());
        // logger.setLevel(Level.INFO);
        // logger.setLevel(Level.WARNING);
        FileHandler fh = new FileHandler ("logHW2Task2.txt", true);
        logger.addHandler (fh);
        SimpleFormatter sFormat = new SimpleFormatter ();
        fh.setFormatter (sFormat);
        Scanner iScanner = new Scanner(System.in);
        System.out.println("Добро пожаловать в калькулятор! Нужно ввести по очереди два числа и желаемую операцию.");
        System.out.print("Введите число 1: ");
        double number1 = iScanner.nextDouble();
        logger.info("Первое число: " + String.valueOf(number1));
        System.out.print("Введите число 2: ");
        double number2 = iScanner.nextDouble();
        logger.info("Второе число: " + String.valueOf(number2));
        System.out.print("Введите желаемое действие(+, -, *, /): ");
        char operation = iScanner.next().charAt(0);
        logger.info("Действие: " + String.valueOf(operation));
        double result;
        switch (operation) {
            case '+':
                result = number1 + number2;
                logger.info("Результат: " + (number1 + number2));
                break;
            case '-':
                result = number1 - number2;
                logger.info("Результат: " + (number1 - number2));
                break;
            case '*':
                result = number1 * number2;
                logger.info("Результат: " + (number1 * number2));
                break;
            case '/':
                result = number1 / number2;
                logger.info("Результат: " + (number1 / number2));
                break;
            default:
                System.out.println("Нет такого действия");
                logger.log(Level.WARNING, "Введено неверное действие");
                return;
            }
        System.out.println("Результат:");
        System.out.println(number1 + " " + operation + " " + number2 + " = " + result);
        iScanner.close();
    }
}
