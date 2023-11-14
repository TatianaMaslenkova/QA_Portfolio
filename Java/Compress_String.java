/*
 * Напишите метод, который сжимает строку. Пример: вход aaaabbbcdd.
 */
package Seminar2;
public class Task2 {
    public static void main(String[] args) {
        String str = "aaaabbbcdd ";
        String [] string = str.split("");
        int count = 1;
        StringBuilder itogo = new StringBuilder();
        for (int i = 0; i < string.length-1; i++) {
            if (string[i].equals(string[i+1])){
            count++;
            }else{
            if (count > 1) {
            itogo.append(String.valueOf(count));
            }
            itogo.append(string[i]);
            count = 1;
            }
        }
        System.out.println(itogo);
    }
}
