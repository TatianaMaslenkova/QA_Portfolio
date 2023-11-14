/*
 * Реализуйте структуру телефонной книги с помощью HashMap, учитывая, что 1 человек может иметь несколько телефонов.
 */
package HW_5;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
public class Task1 {
    public static void main(String[] args) {
        Map<String, List<String>> phoneBook = new HashMap<>();
        phoneBook.put("Иванов", List.of("+7(999)111-11-11", "+7(888)222-22-22", "+7(123)-321-12-31")); 
        phoneBook.put("Петрова", List.of("+7(777)333-33-33", "+7(666)444-44-44")); 
        phoneBook.put("Юрин", List.of("+7(555)555-55-55", "+7(444)666-66-66", "+7(987)-789-89-97")); 
        phoneBook.put("Савина", List.of("+7(333)777-77-77", "+7(222)888-88-88")); 
        phoneBook.put("Мечников", List.of("+7(111)000-00-00", "+7(000)999-99-99", "+7(456)-654-45-64"));
        Scanner iScanner = new Scanner(System.in, "cp866");
        System.out.print("Введите фамилию абонента, чей номер хотите найти: ");
        String lastName = iScanner.nextLine();
        iScanner.close();
        findContact(phoneBook, lastName);
    }

    public static void findContact(Map<String, List<String>> phoneBook, String lastName) {          
            System.out.printf("%s: %s", lastName, phoneBook.get(lastName));
    }
}
