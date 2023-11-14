/*
 * Заполнить список названиями планет Солнечной системы в произвольном порядке с повторениями. 
 * Вывести название каждой планеты и количество его повторений в списке.
 */

package Seminar3;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
public class Task2 {
    public static void main(String[] args) {
        ArrayList<String> planet = new ArrayList<String>(Arrays.asList("Земля","Марс","Юпитер","Сатурн","Уран","Земля",
        "Нептун","Меркурий","Уран","Земля","Нептун","Меркурий","Юпитер",
        "Сатурн","Уран","Венера","Марс","Юпитер"));
        System.out.println(planet);

        Set<String> uniqueSet = new HashSet<String>(planet);  
        for (String i : uniqueSet) {  
            System.out.println(i + ": " + Collections.frequency(planet, i));  
       } 
    }
}