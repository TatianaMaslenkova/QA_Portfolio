/*
 * Реализуйте очередь с помощью LinkedList со следующими методами:enqueue() - помещает элемент в конец 
 * очереди, dequeue() - возвращает первый элемент из очереди и удаляет его, first() - возвращает первый 
 * элемент из очереди, не удаляя.
 */
package HW_4;
import java.io.IOException;
import java.util.LinkedList;
import java.util.Scanner;
public class Task2 {
    public static void main(String[] args) throws IOException {
        LinkedList<Integer> initialLinkedList = new LinkedList<Integer>();
        initialLinkedList.add(1);
        initialLinkedList.add(2);
        initialLinkedList.add(3);
        initialLinkedList.add(4);
        initialLinkedList.add(5);
        System.out.println("Изначальный список: " + initialLinkedList);

        Scanner iScanner = new Scanner(System.in);
        System.out.print("Введите число: ");
        Integer element = iScanner.nextInt();
        iScanner.close();
        enqueue(initialLinkedList, element);
        System.out.println("Изначальный список после метода enqueue: " + initialLinkedList);

        System.out.println("Применение метода dequeue:");
        System.out.println(dequeue(initialLinkedList));
        System.out.println("Список после метода dequeue: " + initialLinkedList);

        System.out.println("Применение метода first:");
        System.out.println(first(initialLinkedList));
    }

    public static void enqueue(LinkedList<Integer> initList, int number) {
        initList.addLast(number);
    }

    public static int dequeue(LinkedList<Integer> initList) {
        int number = 0;
        number = initList.get(0);
        initList.remove(0);
        return number;
    }

    public static int first(LinkedList<Integer> initList) {
        int number = 0;
        number = initList.get(0);
        return number;
    }
}