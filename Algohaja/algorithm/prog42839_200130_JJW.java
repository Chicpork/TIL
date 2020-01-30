import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class prog42839_200130_JJW {
    public static void main(String[] args) {
        System.out.println(solution("011"));
    }

    public static int solution(String numbers) {
        int answer = 0;

        ArrayList<int[]> is = null;
        Set<Integer> number = new HashSet<>();
        String output = "";
        for (int j = 1; j <= numbers.length(); j++) {
            is = permutation(numbers.length(), j);

            output = "";

            for (int[] is2 : is) {
                output = "";
                for (int i = 0; i < is2.length; i++) {
                    output += numbers.substring(is2[i] - 1, is2[i]);
                }
                if (isPrimeNumber(Integer.parseInt(output))) {
                    number.add(Integer.parseInt(output));
                }
            }
        }
        answer = number.size();
        return answer;
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

    public static void perm(ArrayList<int[]> results, int[] numbers, int[] outputs, boolean[] isVisited, int depth,
            int n, int r) {
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

    public static ArrayList<int[]> combination(int n, int r) {
        int[] numbers = new int[n];
        int[] outputs = new int[r];

        for (int i = 0; i < n; i++) {
            numbers[i] = i + 1;
        }

        int counts = (int) Math.pow(2, r) - 1;
        ArrayList<int[]> results = new ArrayList<>(counts);

        comb(results, numbers, outputs, 0, 0, r);
        return results;
    }

    public static void comb(ArrayList<int[]> results, int[] numbers, int[] outputs, int index, int depth, int r) {
        if (depth == r) {
            return;
        }

        for (int i = depth; i < numbers.length; i++) {
            outputs[index] = numbers[i];
            results.add(outputs);
            comb(results, numbers, outputs.clone(), index + 1, numbers[i], r);
        }
    }

    public static boolean isPrimeNumber(int number) {
        int N = (int) Math.sqrt(number);
        if (number <= 1) {
            return false;
        }
        for (int i = 2; i <= N; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}