/*
 * Пусть дан список сотрудников:Иван Иванов
Светлана Петрова
Кристина Белова
Анна Мусина
Анна Крутова
Иван Юрин
Петр Лыков
Павел Чернов
Петр Чернышов
Мария Федорова
Марина Светлова
Мария Савина
Мария Рыкова
Марина Лугова
Анна Владимирова
Иван Мечников
Петр Петин
Иван Ежов
Написать программу, которая найдет и выведет повторяющиеся имена с количеством повторений. 
Отсортировать по убыванию популярности.
 */
package HW_5;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.stream.Collectors;
public class Task2 {
    public static void main(String[] args) {
        String[] employeeList = new String[] {"Иван Иванов", "Светлана Петрова", "Кристина Белова", "Анна Мусина", 
        "Анна Крутова", "Иван Юрин", "Петр Лыков", "Павел Чернов", "Петр Чернышов", "Мария Федорова", "Марина Светлова", 
        "Мария Савина", "Мария Рыкова", "Марина Лугова", "Анна Владимирова", "Иван Мечников", "Петр Петин", "Иван Ежов"};
        ArrayList<String> namesList = new ArrayList<>();
        for (String fullName : employeeList) {
            String [] namesOnly = fullName.split(" ");
            namesList.add(namesOnly[0]);
        }
        Map<String, Integer> namesFrequency = new HashMap<>();  
        for (String i : namesList) {  
            namesFrequency.put(i, Collections.frequency(namesList, i));
        }
        Map<String, Integer> sortedNamesList = namesFrequency.entrySet().stream().sorted(Collections.reverseOrder(Map.Entry.comparingByValue()))
        .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue, (a, b) -> {throw new AssertionError();},
        LinkedHashMap::new)); 
        for (Map.Entry<String, Integer> entry: sortedNamesList.entrySet()){
            String key = entry.getKey();
            Integer value = entry.getValue();
            System.out.println(value + ":" + key);
        }
    }
}
