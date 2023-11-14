/*
 * Напишите метод, который принимает на вход строку (String) и определяет является ли строка палиндромом 
 * (возвращает boolean значение).
 */
package Seminar2;
public class Task3 {
    public static void main(String[] args) {
        System.out.println(poli("шалаш"));
    }
    public static boolean poli(String string) {
    StringBuilder myString = new StringBuilder(string);
    return string.equals(myString.reverse().toString());
    }
}
