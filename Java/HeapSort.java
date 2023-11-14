/*
 * Реализовать алгоритм пирамидальной сортировки (HeapSort).
 * Алгоритм сегментирует массив на отсортированный и неотсортированный. Неотсортированный сегмент преобразовывается 
 * в кучу (heap), что позволяет эффективно определить самый большой элемент. Процедура преобразования в кучу 
 * (процедура heapify) может быть применена к узлу, только если его дочерние узлы уже преобразованы. Таким образом, 
 * преобразование должно выполняться снизу вверх.
 */
package HW_5;
import java.util.Arrays;
import java.util.Random;
public class Task3 {
    public static void main(String args[]) {
        Random randomGenerator = new Random();
        Integer[] initialArray = new Integer[10];
        for (int i = 0; i < initialArray.length; i++) {
            initialArray[i] = randomGenerator.nextInt(100);
        }
        System.out.println("Изначальный массив:");
        System.out.println(Arrays.toString(initialArray));

        Task3 pyramidSorting = new Task3();
        pyramidSorting.sortArray(initialArray);
        
        System.out.println("Итоговый массив после применения пирамидальной сортировки:");
        System.out.println(Arrays.toString(initialArray));
    }
    public void sortArray(Integer[] initialArray) {
        int n = initialArray.length;
        for (int i = n / 2 - 1; i >= 0; i--) {// перегруппируем массив - построим кучу
            heapify(initialArray, n, i);
        }
        for (int i=n-1; i>=0; i--) { // извлечем элементы из кучи
            int temp = initialArray[0];
            initialArray[0] = initialArray[i];
            initialArray[i] = temp;
            heapify(initialArray, i, 0);
        }
    }
    void heapify(Integer[] initialArray, int n, int i) { // преобразуем в двоичную кучу поддерева с корневым узлом i, кот.явл.индексом в arr[], n - размер кучи
        int max = i; // Инициализируем наибольший элемент как корень
        int left = 2*i + 1;
        int right = 2*i + 2;
        if (left < n && initialArray[left] > initialArray[max]) {
            max = left;
        }
        if (right < n && initialArray[right] > initialArray[max]) {
            max = right;
        }
        if (max != i) {
            int tempVar = initialArray[i];
            initialArray[i] = initialArray[max];
            initialArray[max] = tempVar;
            heapify(initialArray, n, max);
        }
    }
}
