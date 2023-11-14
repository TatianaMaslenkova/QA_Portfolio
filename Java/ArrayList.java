/*
 * Задан целочисленный список ArrayList. Найти минимальное, максимальное и среднее из этого списка.
 */
package HW_3;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;
public class HW3_Task3 {
    public static void main(String[] args) {
        Random randomGenerator = new Random();
        ArrayList<Integer> initialList = new ArrayList<>();        
        for (int i = 0; i < 10; i++) {
            initialList.add(randomGenerator.nextInt(100));  
        }
        System.out.println("Изначальный список:");
        System.out.println(initialList);     
        System.out.println("Максимальное значение:");
        System.out.println(Collections.max(initialList));
        System.out.println("Минимальное значение:");
        System.out.println(Collections.min(initialList));
        System.out.println("Среднее значение:");
        double average = getAverage (initialList);
        System.out.println(average);

    }
    public static double getAverage (ArrayList<Integer> initialList) {
        double sum = 0;
        for(int i=0;i<initialList.size();i++) {
            sum+=initialList.get(i);
        }
        return sum/initialList.size();
    }
}
