import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;

public class boj11724_200214_JJW {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] input = bf.readLine().split(" ");

        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        ArrayList<HashSet<Integer>> sets = new ArrayList<>(N);
        for (int i = 0; i < N; i++) {
            sets.add(i, null);
        }

        String[] temp = null;
        int l, r, setSize = 0;
        HashSet<Integer> tempSet1, tempSet2;
        for (int i = 0; i < M; i++) {
            temp = bf.readLine().split(" ");
            l = Integer.parseInt(temp[0]) - 1;
            r = Integer.parseInt(temp[1]) - 1;
            tempSet1 = sets.get(l);
            tempSet2 = sets.get(r);
            if (tempSet1 != null && tempSet2 != null) {
                if (tempSet1 == tempSet2) {
                    continue;
                }
                tempSet1.addAll(tempSet2);
                for (Integer integer : tempSet2) {
                    sets.set(integer, tempSet1);
                }
                setSize--;
            } else if (tempSet1 != null) {
                tempSet1.add(r);
                sets.set(r, tempSet1);
            } else if (tempSet2 != null) {
                tempSet2.add(l);
                sets.set(l, tempSet2);
            } else {
                tempSet1 = new HashSet<>();
                tempSet1.add(l);
                tempSet1.add(r);
                sets.set(r, tempSet1);
                sets.set(l, tempSet1);
                setSize++;
            }
        }
        for (int i = 0; i < N; i++) {
            if (sets.get(i) == null) {
                setSize++;
            }
        }
        System.out.println(setSize);
    }
}