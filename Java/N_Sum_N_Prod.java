/*
 * Вычислить n-ое треугольного число(сумма чисел от 1 до n), n! (произведение чисел от 1 до n)
 */
package HW_1;
import java.util.Scanner;
public class HW1_Task1 {
    public static void main(String[] args) {
        Scanner iScanner = new Scanner(System.in);
        System.out.print("Введите число n: ");
        int number = iScanner.nextInt();
        System.out.println("Сумма чисел от 1 до " + number + " равна " + nSum(number));
        System.out.println("Произведение чисел от 1 до " + number + " равна " + nProd(number));
        iScanner.close();
    }
    
    static int nSum(int number) {
        int sum = 0;
        for (int i = 1; i <= number; i++) {
            if(number==1) {
                sum = 1;
            } else {
                sum += i;
            }
        }
        return sum;
    }

    static int nProd(int number) {
        int prod = 1;
        for (int i = 1; i <= number; i++) {
            if(number==1) {
                prod = 1;
            } else {
                prod *= i;
            }
        }
        return prod;
    }
}
