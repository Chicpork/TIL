import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;

public class problem2 {
    public static void main(String[] args) {
        String[] answer = {};
        String[] orders = {"ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"};
        int[] course = {2,3,5};
        HashSet<String> answerSet = new HashSet<>();
        
        ArrayList<int[]> combination = null;
        HashMap<String, Integer> hashMap = null;
        String combo = "";
        char[] chars;
        int comboCnt = -1;
        int maxComboCnt = -1;
        for (int k = 0; k < course.length; k++) {
            hashMap = new HashMap<>();
            maxComboCnt = -1;
            for (int i = 0; i < orders.length; i++) {
                if (orders[i].length() >= course[k]) {
                    combination = combination(orders[i].length(), course[k]);
                    for (int[] tempComb : combination) {
                        combo = "";
                        for (int j = 0; j < tempComb.length; j++) {
                            combo += orders[i].charAt(tempComb[j]-1);
                        }
                        chars = combo.toCharArray();
                        Arrays.sort(chars);
                        combo = new String(chars);
                        if (hashMap.containsKey(combo)) {
                            comboCnt = hashMap.get(combo) + 1;
                        } else {
                            comboCnt = 1;
                        }
                        hashMap.put(combo, comboCnt);
                        if (maxComboCnt < comboCnt) {
                            maxComboCnt = comboCnt;
                        }
                    }
                }
            }

            for (String str : hashMap.keySet()) {
                if (maxComboCnt >= 2 && hashMap.get(str) == maxComboCnt) {
                    answerSet.add(str);
                }
            }
        }
        answer = new String[answerSet.size()];
        answerSet.toArray(answer);
        Arrays.sort(answer);
        // for (String str : answer) {
        //     System.out.println(str);
        // }
    }

    public static ArrayList<int[]> combination(int n, int r) {
        int[] numbers = new int[n];
        int[] outputs = new int[r];

        for (int i = 0; i < n; i++) {
            numbers[i] = i + 1;
        }

        int counts = (int) Math.pow(2, r) - 1;
        ArrayList<int[]> results = new ArrayList<>(counts);

        // combAll(results, numbers, outputs, 0, 0, r);
        comb(results, numbers, outputs, 0, 0, r);
        return results;
    }

    private static void comb(ArrayList<int[]> results, int[] numbers, int[] outputs, int lastIndex, int depth, int r) {
        if (depth == r) {
            results.add(outputs.clone());
            return;
        }

        for (int i = lastIndex; i < numbers.length; i++) {
            outputs[depth] = numbers[i];
            comb(results, numbers, outputs, i + 1, depth + 1, r);
            outputs[depth] = 0;
        }
    }
}
