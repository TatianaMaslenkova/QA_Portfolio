/*
 * Создать список типа ArrayList<String>. Поместить в него как строки, так и целые числа. 
 * Пройти по списку, найти и удалить целые числа.

 */
package Seminar3;
import java.util.ArrayList;
import java.util.Arrays;
public class Task4 {
    public static void main(String[] args) { 
        ArrayList<String> planet = new ArrayList<String>(Arrays.asList(
            "Земля","Марс","5","Сатурн","Уран","4",
        "Нептун","7","Уран","9"));
        System.out.print(planet);
        System.out.println();
        for (int i = 0; i < planet.size(); i++) {
            try {
                Integer.parseInt(planet.get(i));
                planet.remove(i); 

            }catch (Exception e){
                
            }
        }
        System.out.print(planet);
    }    

}