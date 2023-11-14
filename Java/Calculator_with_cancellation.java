/*
 * В калькулятор добавьте возможность отменить последнюю операцию.
 */
package HW_4;
import java.io.IOException;
import java.util.Scanner;
import java.util.Stack;
public class Task3 {
    public static void main(String[] args) throws IOException {
        Stack<String> calcStack = new Stack<>();
        String inputData = "";
        Scanner iScanner = new Scanner(System.in);
        double result;
        
        while (calcStack.size() <= 3){
            if (calcStack.size() < 1){
                System.out.print("Введите число 1: ");
            } else if (calcStack.size() < 2){
                System.out.print("Введите число 2 или команду отмены (cancel): ");
            } else if (calcStack.size() < 3){
                System.out.print("Введите желаемое действие(+, -, *, /) или команду отмены (cancel): ");
            } else if (calcStack.size() == 3){
                System.out.print("Введите start для начала или команду отмены (cancel): ");
            }
            inputData = iScanner.nextLine();
            if (inputData.equals("cancel")) {
                calcStack.remove(calcStack.size()-1);
            }else{
                calcStack.push(inputData);      
            }
        }    
        
        if (inputData.equals("start")) {
            calcStack.pop();
            System.out.print("Результат: ");
        }                   

        switch (calcStack.pop()) {
            case "+":
                result = Double.parseDouble(calcStack.pop()) + Double.parseDouble(calcStack.pop());
                System.out.println(result);
                break;
            case "-":
                result = - Double.parseDouble(calcStack.pop()) + Double.parseDouble(calcStack.pop());
                System.out.println(result);
                break;
            case "*":
                result = Double.parseDouble(calcStack.pop()) * Double.parseDouble(calcStack.pop());
                System.out.println(result);
                break;
            case "/":
                Double temp = Double.parseDouble(calcStack.pop());
                result = Double.parseDouble(calcStack.pop())/temp;
                System.out.println(result);
                break;
            default:
                System.out.println("Нет такого действия");
                return;
        }
        iScanner.close();
    }
}
