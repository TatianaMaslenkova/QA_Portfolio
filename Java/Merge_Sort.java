/*
 * Реализовать алгоритм сортировки слиянием (Данный алгоритм разбивает список на две части, каждую из них 
 * он разбивает ещё на две и так далее, пока не останутся единичные элементы. Массив из одного элемента 
 * считается упорядоченным. Соседние элементы сравниваются и соединяются вместе. Так происходит до тех 
 * пор, пока все элементы не будут отсортированы. Сортировка осуществляется путём сравнения наименьших 
 * элементов каждого подмассива. Первые элементы каждого подмассива сравниваются первыми. Наименьший 
 * элемент перемещается в результирующий массив. Счётчики результирующего массива и подмассива, откуда был 
 * взят элемент, увеличиваются на один)
 */
package HW_3;
import java.util.*;
import java.io.IOException;
public class HW3_Task1 {
    public static void main(String[] args) throws IOException {
        int[] initialArray = new int[] {3,9,5,7,8,6,1,4,2};
        System.out.println("Изначальный массив:");
        System.out.println(Arrays.toString(initialArray));
        int[] sortedArray = sortArrayByMerger(initialArray);
        System.out.println("Массив, полученный в результате сортировки слиянием:");
        System.out.println(Arrays.toString(sortedArray));
        
    }
    public static int[] sortArrayByMerger(int[] initialArray) {
        int[] firstHalfArray = Arrays.copyOf(initialArray, initialArray.length);
        int[] secondHalfArray = new int[initialArray.length];
        int[] sortingResult = divideArray(firstHalfArray, secondHalfArray, 0, initialArray.length);
        return sortingResult;
    }
    public static int[] divideArray(int[] firstHalfArray, int[] secondHalfArray, int startIndex, int endIndex) {
        if (startIndex >= endIndex - 1) {
            return firstHalfArray;
        }
        int middle = startIndex + (endIndex - startIndex) / 2;
        int[] sortedArray1 = divideArray(firstHalfArray, secondHalfArray, startIndex, middle);
        int[] sortedArray2 = divideArray(firstHalfArray, secondHalfArray, middle, endIndex);
        //для слияния
        int index1 = startIndex;
        int index2 = middle;
        int destIndex = startIndex;
        int[] divisionResult = sortedArray1 == firstHalfArray ? secondHalfArray : firstHalfArray;
        while (index1 < middle && index2 < endIndex) {
            divisionResult[destIndex++] = sortedArray1[index1] < sortedArray2[index2]
                    ? sortedArray1[index1++] : sortedArray2[index2++];
        }
        while (index1 < middle) {
            divisionResult[destIndex++] = sortedArray1[index1++];
        }
        while (index2 < endIndex) {
            divisionResult[destIndex++] = sortedArray2[index2++];
        }
        return divisionResult;
    }
}