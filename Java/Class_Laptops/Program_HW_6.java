/*
 * Написать метод, который будет запрашивать у пользователя критерий (или критерии) фильтрации 
 * и выведет ноутбуки, отвечающие фильтру. Критерии фильтрации можно хранить в Map. 
 * Например: “Введите цифру, соответствующую необходимому критерию: 1 - ОЗУ 2 - Объем ЖД
 * 3 - Операционная система 4 - Цвет … Далее нужно запросить минимальные значения для указанных 
 * критериев - сохранить параметры фильтрации можно также в Map. Отфильтровать ноутбуки 
 * из первоначального множества и вывести проходящие по условиям.
 */
package HW_6_Final;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
public class Program_HW_6 {
    public static void main(String[] args) throws IOException{
        // #region
        Laptops lap1 = new Laptops(20230301, "ASUS", "TUF Gaming A15", "Intel Core i5", 
        15.6, 8, 512, "Windows 11", "серый", 70000);
        Laptops lap2 = new Laptops(20230302, "LENOVO", "IdeaPad 5 15ITL05", "Intel Core i5", 
        17.3, 16, 256, "Windows 10", "синий", 45000);
        Laptops lap3 = new Laptops(20230303, "XIAOMI", "RedmiBook 15", "Intel Core i3", 
        16.1, 8, 256, "Windows 11", "белый", 35000);
        Laptops lap4 = new Laptops(20230304, "Hp", "dw1495nia 6J5C0EA", "Intel Celeron N4120", 
        15.6, 4, 1024, "Windows 10", "черный", 20000);
        Laptops lap5 = new Laptops(20230305, "APPLE", "MacBook Air MLY33", "Apple M2 M2", 
        13.6, 8, 512, "macOS", "серый", 150000);
        Laptops lap6 = new Laptops(20230306, "Asus", "ABC123", "Intel Core i3", 
        16.1, 16, 1024, "Windows 7", "белый", 50000);
        Laptops lap7 = new Laptops(20230307, "Lenovo", "Idea20ITL08", "Intel Core i3", 
        15.6, 8, 512, "Windows 11", "бежевый", 55000);
        Laptops lap8 = new Laptops(20230308, "Xiaomi", "Book 30", "Intel Core i5", 
        17.1, 16, 512, "Windows 8", "красный", 47000);
        Laptops lap9 = new Laptops(20230309, "HP", "8J7C5EA", "Intel Celeron N4120", 
        16.1, 8, 512, "Windows 11", "белый", 28000);
        Laptops lap10 = new Laptops(20230310, "Apple", "MacBook Air MLY44", "Apple M3 M3", 
        13.3, 16, 256, "macOS", "серый", 124000);
        //#endregion

        Set<Laptops> laptopsList = new HashSet<>();
        laptopsList.add(lap1);
        laptopsList.add(lap2);
        laptopsList.add(lap3);
        laptopsList.add(lap4);
        laptopsList.add(lap5);
        laptopsList.add(lap6);
        laptopsList.add(lap7);
        laptopsList.add(lap8);
        laptopsList.add(lap9);
        laptopsList.add(lap10);     
        
        Scanner scanner = new Scanner(System.in,"ibm866");
        System.out.println("Приветствуем в нашем онлайн-магазине ноутбуков!");
        System.out.println();
        // Если нужно вывести полный список ноутбуков:
        System.out.println("Всего в наличии " + laptopsList.size() + " ноутбуков:");
        System.out.println();
        System.out.println(laptopsList);
        Map<Integer, String> filters = new HashMap<>();
        Integer[] filterNumbers = new Integer[]{1,2,3,4,5,6,7,8,9};
        System.out.println();
        System.out.println("Выберем фильтры, по которым будем выбирать ноутбук:");
        System.out.println();
        for (int i: filterNumbers) {
            String filterCriterion;
            switch (i){
                case 1: {
                    System.out.println("Введите бренд (в наличии есть: Asus, Lenovo, Xiaomi, HP, Apple) или s, чтобы пропустить: ");
                    filterCriterion = scanner.nextLine();
                    fillFiltersMap(filters, filterCriterion, 1);
                    continue;
                }
                case 2: {
                    System.out.println("Введите модель (в наличии есть: TUF Gaming A15, IdeaPad 5 15ITL05, RedmiBook 15, dw1495nia 6J5C0EA, MacBook Air MLY33, ABC123, Idea20ITL08, Book 30, 8J7C5EA, MacBook Air MLY44) или s, чтобы пропустить: ");
                    filterCriterion = scanner.nextLine();
                    fillFiltersMap(filters, filterCriterion, 2);
                    continue;
                }
                case 3: {
                    System.out.println("Введите процессор (в наличии есть: Intel Core i5, Intel Core i3, Intel Celeron N4120, Apple M2 M2, Apple M3 M3) или s, чтобы пропустить: ");
                    filterCriterion = scanner.nextLine();
                    fillFiltersMap(filters, filterCriterion, 3);
                    continue;
                }
                case 4: {
                    System.out.println("Введите минимальную диагональ (в дюймах) или s, чтобы пропустить: ");
                    filterCriterion = scanner.nextLine();
                    fillFiltersMap(filters, filterCriterion, 4);
                    continue;
                }
                case 5: {
                    System.out.println("Введите минимальную оперативную память (в Гб) или s, чтобы пропустить: ");
                    filterCriterion = scanner.nextLine();
                    fillFiltersMap(filters, filterCriterion, 5);
                    continue;
                }
                case 6: {
                    System.out.println("Введите минимальный объём жесткого диска (в Гб) или s, чтобы пропустить: ");
                    filterCriterion = scanner.nextLine();
                    fillFiltersMap(filters, filterCriterion, 6);
                    continue;
                }
                case 7: {
                    System.out.println("Введите ОС (в наличии есть: Windows 7, Windows 8, Windows 10, Windows 11, macOS) или s, чтобы пропустить: ");
                    filterCriterion = scanner.nextLine();
                    fillFiltersMap(filters, filterCriterion, 7);
                    continue;
                }
                case 8: {
                    System.out.println("Введите цвет (в наличии есть: серый, синий, белый, черный, бежевый, красный) или s, чтобы пропустить: ");
                    filterCriterion = scanner.nextLine();
                    fillFiltersMap(filters, filterCriterion, 8);
                    continue;
                }
                case 9: {
                    System.out.println("Введите максимальную цену (в наличии ноутбуки от 20 000 до 150 000 руб.) или s, чтобы пропустить: ");
                    filterCriterion = scanner.nextLine();
                    fillFiltersMap(filters, filterCriterion, 9);
                }
                continue;
            }
        }
        System.out.println("Запрашиваемые для поиска фильтры получились следующие:");
        System.out.println();
        filters.forEach((key,value)-> {
            if (!value.equals("null")){
                switch (key){
                    case 1: {
                        System.out.print(value + ", ");
                        break;
                    }
                    case 2: {
                        System.out.printf("Бренд: %s ", value);
                        break;
                    }
                    case 3: {
                        System.out.printf("Модель: %s ", value);
                        break;
                    }
                    case 4: {
                        System.out.printf("Процессор: %s ", value);
                        break;
                    }
                    case 5: {
                        System.out.printf("Минимальная диагональ (в дюймах): %f ", value);
                        break;
                    }
                    case 6: {
                        System.out.printf("Минимальная оперативная память (в Гб): %d ", value);
                        break;
                    }
                    case 7: {
                        System.out.printf("Минимальный объём жесткого диска (в Гб): %d ", value);
                        break;
                    }
                    case 8: {
                        System.out.printf("ОС: %s ", value);
                        break;
                    }
                    case 9: {
                        System.out.printf("Цвет: %s ", value);
                        break;
                    }
                    case 10: {
                        System.out.printf("Максимальная цена: %d ", value);
                        break;
                    }
                }
            }
        });
        System.out.println("Найдены следующие ноутбуки:");
        System.out.println();
        for (Laptops element:laptopsList) {
            if ((filters.get(1).equals("null") || element.getBrand().equals(filters.get(1)))
            &&  (filters.get(2).equals("null") || element.getModel().equals(filters.get(2)))
            &&  (filters.get(3).equals("null") || element.getCpu().equals(filters.get(3)))
            &&  (filters.get(4).equals("null") || element.getScreenDiagonal() >= Integer.parseInt(filters.get(4)))
            &&  (filters.get(5).equals("null") || element.getRam() >= Integer.parseInt(filters.get(5)))
            &&  (filters.get(6).equals("null") || element.getSsdCapacity() >= Integer.parseInt(filters.get(6)))
            &&  (filters.get(7).equals("null") || element.getOS().equals(filters.get(7)))
            &&  (filters.get(8).equals("null") || element.getColor().equals(filters.get(8)))
            &&  (filters.get(9).equals("null") || element.getPrice() <= Integer.parseInt(filters.get(9)))) {
                System.out.println(element);
            }
        }
    }
    public static void fillFiltersMap(Map<Integer, String> filters, String filterCriterion, Integer i) {
        if (filterCriterion.equals("s")) {
            filters.put(i,"null");
        } else {
            filters.put(i,filterCriterion);
        }
    }
}