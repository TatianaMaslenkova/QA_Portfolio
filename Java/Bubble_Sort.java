/*
 * Реализуйте алгоритм сортировки пузырьком числового массива, результат после каждой 
 * итерации запишите в лог-файл.
 */
package HW_2;
import java.util.*;
import java.io.IOException;
import java.util.logging.*;
public class HW2_Task1 {
    public static void main(String[] args) throws IOException {
        int[] arr = new int[] {3,9,5,7,8,6,1,4,2};
        int temp;
        Logger logger = Logger.getLogger(HW2_Task1.class.getName());
        logger.setLevel(Level.INFO);
        FileHandler fh = new FileHandler ("logHW2Task1.txt");
        logger.addHandler (fh);
        SimpleFormatter sFormat = new SimpleFormatter ();
        fh.setFormatter (sFormat);
        logger.log(Level.INFO, Arrays.toString(arr));
        for (int i = 0; i < arr.length - 1; i++) {
            for(int j = 0; j < arr.length - i - 1; j++) {
                if(arr[j + 1] < arr[j]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    logger.log(Level.INFO, Arrays.toString(arr));
                }
            }
        }
        System.out.println("Отсортированный массив: " + Arrays.toString(arr));   
    }
}
