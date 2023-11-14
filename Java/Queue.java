import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

/*
 * 1) Написать метод, который принимает массив элементов, помещает их в стэк и выводит на консоль 
 * содержимое стэка.
 * 2) Написать метод, который принимает массив элементов, помещает их в очередь и выводит на консоль 
 * содержимое очереди.
 */
public class Task3 {
    public static void main(String[] args) {

        String[] arrStr = {"dom","try","pip","dun","sup"};
        Stack<String> stack = new Stack<>();
        for (int i = 0; i < arrStr.length; i++) {
            stack.push(arrStr[i]);
        }
        System.out.println(stack);
        
        Queue<String> queue = new LinkedList<String>();
        for (int i = 0; i < arrStr.length; i++) {
            queue.add(arrStr[i]);
        }
        System.out.println(queue);
    }
}
