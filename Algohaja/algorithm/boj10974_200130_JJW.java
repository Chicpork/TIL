import java.util.ArrayList;
import java.util.Scanner;

public class boj10974_200130_JJW {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        ArrayList<int[]> arrayList = permutation(N, N);

        for (int[] is : arrayList) {
            for (int i = 0; i < is.length; i++) {
                System.out.print(is[i] + " ");
            }
            System.out.println();
        }
    }

    public static ArrayList<int[]> permutation(int n, int r) {
        int[] numbers = new int[n];
        int[] outputs = new int[r];
        boolean[] isVisited = new boolean[n];

        int counts = 1;
        for (int i = 0; i < n; i++) {
            numbers[i] = i + 1;
            counts *= i + 1;
        }

        ArrayList<int[]> results = new ArrayList<>(counts);

        perm(results, numbers, outputs, isVisited, 0, n, r);
        return results;
    }

    public static void perm(ArrayList<int[]> results, int[] numbers, int[] outputs, boolean[] isVisited, int depth, int n,
            int r) {
        if (depth == r) {
            results.add(outputs.clone());
            return;
        }

        for (int i = 0; i < numbers.length; i++) {
            if (!isVisited[i]) {
                isVisited[i] = true;
                outputs[depth] = numbers[i];
                perm(results, numbers, outputs, isVisited, depth + 1, n, r);
                isVisited[i] = false;
            }
        }
    }
}